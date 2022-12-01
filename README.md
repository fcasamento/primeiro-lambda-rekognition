# Criação do Primeiro Lambda com Rekognition e S3
Objetivo: esse é um código inicial utilizando a integração desses três serviços da AWS, onde esse código serve para fazer o reconhecimento de um primeiro bucket ontem inserimos algumas imagens de modelo (arquivo index.py) serve para essa função, e depois disso as proximas imagens (_verificar.png) que inserimos será feito a comparação com as primeiras do modelo.
- Utilizando Python 3;
- Alterando politica entre bucktes para somente entre eles ter o acesso:
https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/example-bucket-policies.html
Restringir o acesso a um indicador HTTP específico
- Necessário também permissionar o Lambda ter acesso para o Rekognition;
- No bucket S3 onde temos a página estática precisamos alterar em permissões o CORS configuration na linha DE `<AllowedHeade>Auhotization</AllowedHeade>` PARA `<AllowedHeade>*</AllowedHeade>`;
- Necessário dentro do arquivo do `fa-sites\js\importa-dados.js` alterar os caminho do S3; 

