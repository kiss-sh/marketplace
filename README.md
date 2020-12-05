marketplace
===========

Requisitos minimos para executar o projeto:
-------------------------------------------
* python 3.6 ou superior
* uma instancia do postgres devidamente configurado
* um arquivo contendo atributos usados pelo projeto, disponivel em um repo privado

Dicas para colaboradores:
-------------------------
Setup para desenvolvimento no linux

* Clone por HTTPS
```console
$ git clone https://github.com/kiss-sh/marketplace.git
```
* Clone por SSH
```console
$ git clone git@github.com:kiss-sh/marketplace.git
```
* Navegando pelas pastas do projeto, setando uma venv e instalando os requerimentos
```console
$ cd marketplace/src/
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
para trabalhar em um novo recurso é preciso criar uma branch a partir da branch dev

* Para baixar a branch dev localmente
```console
$ git branch dev origin/dev
```

* Para trocar para a branch dev:
```console
$ git checkout dev
```

* Apos trocar para a branch dev, para criar uma nova branch a partir da dev
```console
$ git branch nome-recurso
```

* Sempre que for criar uma nova branch a partir da dev é ideial atualizar os dados locais
```console
$ git pull
```

* Empurrar nova branch para o repo remoto pela primeira vez
```console
$ git push --set-upstream origin nome-recurso
```

após concluir o recurso, crie uma merge request usando o github, para mesclar a branch com a branch dev

Criar uma instancia do postgres usando docker:
----------------------------------------------
> os comandos a seguir tambem podem ser usados no podman, trocando o comando docker por podman
* Baixar a imagem do postgres
```console
$ docker pull postgres
```

* Criar um container do postgres e executá-lo
```console
$ docker run --name postgres-django -p 5432:5432 -e "POSTGRES_PASSWORD=senha" -d postgres
```
> **_Observação:_**  o argumento do parametro POSTGRES_PASSWORD está em um arquivo em um repo privado

* Entrar no container e usar a cli do postgres pra criar um banco de dados
```console
$ docker exec -it postgres-django bash
# psql -U postgres
# CREATE DATABASE market_db;
```

encerrar a cli e sair do container
```console
# \q
# exit
```
