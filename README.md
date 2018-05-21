# Applicação usando o redis para marcar deploy

## ferrmentas instaladas
- docker
- docker-compose
- terraform



## Usage
Antes da aplicação subir a aplicação 
buildar o app local
docker build -t basic-api:master-v1 .

executar api no pipeline 
 docker-compose up -d 

criar uma ec2

Entrar na pasta do terraform 

Antes de tudo setar suas chaves no arquivo variables.tf

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

Executar o shell
./create-ec2-destroy.sh


Executa 
curl -H "Content-Type: application/json" -X POST -d '{"projeto":"teste"}' https://localhost:8080/api/inicio

curl -H "Content-Type: application/json" -X POST -d '{"projeto":"teste"}' https://localhost:8080/api/fim

Lista o deploy detalhado de acordo com o numero da chave
curl -H "Content-Type: application/json" -X GET https://localhost:8080/inicio

Lista todos os deploys 
curl -H "Content-Type: application/json" -X GET https://localhost:8080/projects
