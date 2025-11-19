# Docker! 🐳

## O que é Docker? (A base de tudo)
Imagine que você desenvolveu um aplicativo no seu computador. Ele funciona perfeitamente! Mas quando você tenta rodar em outro computador ou no servidor da empresa... não funciona. Por quê? Porque:

* A versão do Python é diferente
* Faltam bibliotecas instaladas
* O sistema operacional é outro
* As configurações não são as mesmas

Docker resolve exatamente isso!<br/>
Docker é como se fosse uma `caixinha mágica` que empacota seu aplicativo junto com TUDO que ele precisa para funcionar: o código, as bibliotecas, as dependências, as configurações... tudo junto! Essa "caixinha" funciona em qualquer lugar que tenha Docker instalado.

## Conceitos fundamentais 

**1. Imagem Docker**
* É como se fosse uma "receita de bolo" ou um "modelo"
* Contém o sistema operacional básico + suas aplicações + dependências
* É somente leitura (você não modifica diretamente)
* Exemplo: uma imagem do Ubuntu com Python 3.11 instalado

**2. Container**
* É o "bolo pronto" feito a partir da receita (imagem)
* É uma instância rodando da imagem
* Você pode ter vários containers da mesma imagem
* Cada container é isolado dos outros

**3. Dockerfile**
* É o arquivo de texto onde você escreve as instruções
* É literalmente a "receita" de como criar sua imagem
* Diz: qual sistema usar, o que instalar, quais arquivos copiar, etc.

**4. Docker Hub**
* É como uma "loja de aplicativos" de imagens Docker Tem milhares de imagens prontas (Ubuntu, Python, Node, MySQL, etc.)
*Pode baixar imagens de lá e também publicar as suas

## Analogia para fixar
Pense assim:
* Dockerfile = Receita escrita no papel
* Imagem = Forma de bolo (o molde)
* Container = O bolo assado e pronto para comer
* Docker Hub = Livro de receitas online

## Rodando o container
Primeiramente realizar a build da imagem, depois rodar o container
```bash
    docker build -t primeiro-app-docker .
    docker run -t primeiro-app-docker
```

## Comandos essenciais para começar
```bash
# Listar containers rodando agora

docker ps

# Listar TODOS os containers (inclusive parados)
docker ps -a

# Listar imagens baixadas no seu computador
docker images

# Baixar uma imagem sem rodar
docker pull ubuntu

# Parar um container rodando
docker stop NOME_OU_ID

# Iniciar um container parado
docker start NOME_OU_ID

# Remover um container
docker rm NOME_OU_ID

# Remover uma imagem
docker rmi NOME_DA_IMAGEM

# Ver logs de um container
docker logs NOME_OU_ID
```

## Explicando sobre o `Dockerfile`
```bash
    FROM python:3.11-slim
```
* Diz qual imagem base usar
* Aqui estamos usando Python 3.11 versão "slim" (mais leve)
```bash
    WORKDIR /app
```
* Define onde os próximos comandos vão trabalhar
* É como fazer `cd /app`
```bash
    COPY app.py .
```
* Copia arquivo do seu computador para dentro do container
* app.py = arquivo de origem
* `.` = destino (a pasta /app que definimos)
```bash
    CMD ["python", "app.py"]
```
* O comando que será executado quando o container iniciar
* É como você digitar `python app.py` no terminal
* `.` = destino (a pasta /app que definimos)
