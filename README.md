marketplace
===========

Dicas para colaboradores:
-------------------------
Setup para desenvolvimento no linux
```console
$ git clone git@github.com:kiss-sh/marketplace.git
$ cd marketplace/src/
$ python -m venv .venv
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

papapapapapap

* Para criar uma nova branch a partir da dev
```console
$ git branch nome-recurso
```

* Empurrar nova branch para o repo remoto pela primeira vez
```console
$ git push --set-upstream origin nome-recurso
```

* Sempre que for criar uma nova branch a patir da dev é ideial atualizar os dados locais
```console
$ git pull
```

após concluir o recurso, crie uma merge request usando o github, para mesclar a branch com a branch dev