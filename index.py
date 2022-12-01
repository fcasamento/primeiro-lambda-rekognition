import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')
### (1) Listar e popular imagens no S3 para treino
def lista_imagens():
    imagens=[]
    bucket = s3.Bucket('fc-imagens')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    print(imagens)
    return imagens
### (2) Indexar já existentes no S3
def index_colecao (imagens):
    for i in imagens:
        response = client.index_faces(
            CollectionId='faces',
            DetectionAtrributes=[],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'fc-imagens',
                    'Name': i,
                }
            }
        )

### Retorno do (1)
imagens = lista_imagens()
### Retorno do (2)
index_colecao(imagens)