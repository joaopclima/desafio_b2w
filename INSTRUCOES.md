# Desafio Webcrawler

## Configurações Iniciais

É necessário instalado em sua máquina _Python 3_ , seu pacote de instalação (_pip_), e um ambiente virtual (venv). Também é necessário ter o _MongoDB_ instalado na sua máquina e instalar os pacotes que estão dentro do arquivo _"requirements.txt"_. 

_Para a ativação do ambiente virtual no ambiente Linux e MacOS..._
```console
 $ source nome_do_diretorio/venv/bin/activate
```
_Para a ativação do ambiente virtual no ambiente Windows..._
```console
 $ .\venv\Scripts/activate.bat
```
_Para a instalação dos pacotes..._
```console
$ pip install -r requirements.txt
```


## Como Rodar

Execute o comando (dentro da pasta _quotes_challenge_)
```console
$ scrapy crawl quotes
```

O crawler irá rodar, buscando tudo o que foi definido no arquivo _quotes.py_. Logo após, irá salvar todas as informações no banco de dados criado com o nome de _quotes_, dentro da collection _joao_lima_, conforme definido pelo pipeline criado.

Os arquivos exportados, que estão em JSON e em CSV, estão disponíveis na pasta principal
do projeto (_quotes_challenges_), se for necessário ter uma base de como os dados estão estruturados e dispostos.

## Relatórios

Todas as queries necessárias solicitadas estão dentro do arquivo _queries.js_. Só precisar executar os comandos que os resultados serão retornados.
