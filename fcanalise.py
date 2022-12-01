import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')
### (1) Indexar nova imagem para depois comparar
def detecta_faces():
    face_detectada = client.index_faces(
        CollectionId='faces',
        DetectionAtrributes=['DEFAULT'],
        ExternalImageId=i['Verificar'],
        Image={
            'S3Object': {
                'Bucket': 'fc-imagens',
                'Name': '_verificar.png',
            }
        }
    )
    return face_detectada
### (2) Obter Id nova imagem para depois comparar
def cria_list_faceId_detecta(face_detectada):
    faceId_detectada=[]
    for imagem in range(len(face_detectada['FaceRecords'])):
        faceId_detectada.append(face_detectada['FaceRecords'][imagem]['Face']['FaceId'])
    return faceId_detectada
### (3) Comparar os Ids
def compara_imagem(faceId_detectada):
    resultado_compara=[]
    for ids in faceId_detectada:
        resultado_compara.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=ids,
                FaceMatchThreshoul=80,
                MaxFaces=10,
            )
        )
        return resultado_compara
### (4) Resultado da comparação
def gera_json(resultado_compara):
    dados_json=[]
    for face_matches in resultado_compara:
        if(len(face_matches.get('FaceMatches'))) >=1:
            perfil = dict(nome=face_matches['FaceMatches'][0]['ExternalImageId'],
                          faceMatch=round(face_matches['FaceMatches'][0]['Similarity'], 2)
            )
            dados_json.append(perfil)
    return dados_json
### (5) Gerar arquivo, mostra no site
def envia_dados(dados_json):
    arquivo = s3.Object('fc-site', 'dados.json')
    arquivo.put(Body=json.dumps(dados_json))

### (6) Deleta ID detectados
def del_imagem_colecao(faceId_detectada):
    client.delete_faces(
        CollectionId='faces',
        FaceIds=faceId_detectada,
    )

def main (event, context):
    ### Retorno do (1)
    face_detectada = detecta_faces()
    # print(json.dumps(face_detectada, indent=4))
    ### Retorno do (2)
    faceId_detectada = cria_list_faceId_detecta(faceId_detectada)
    # print(faceId_detectada)
    ### Retorno do (3)
    resultado_compara = compara_imagem(faceId_detectada)
    # print(json.dumps(resultado_compara, indent=4))
    ### Retorno do (4)
    dados_json = gera_json(resultado_compara)
    ### Retorno do (5)
    envia_dados(dados_json)
    ### Retorno do (6)
    del_imagem_colecao(faceId_detectada)
    print(json.dumps(dados_json, indent=4))