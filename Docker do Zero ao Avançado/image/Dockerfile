# IMAGEM DO NODE, COM LINUX ALPINE
FROM node:25-alpine3.22

# ADICIONO GRUPO DEV, E ADICIONO USUARIO VINICIUS COM O GRUPO DEV
RUN addgroup -S dev && adduser -S vinicius -G dev -s /bin/sh

# CRIO PASTA COM PASTA, ALTERA PROPRIEDADADES DA PASTA E PERMISSÃO
RUN mkdir -p /etc/todos && chown -R vinicius:dev /etc/todos && chmod 755 /etc/todos

# COPIA E ALTERAR USUARIO E GRUPO DOS ARQUIVOS
COPY --chown=vinicius:dev package.json yarn.lock ./

USER vinicius

COPY package.json .

WORKDIR /app

COPY --chown=vinicius:dev . . 

RUN yarn install --production

EXPOSE 3000

CMD [ "node", "src/index.js" ]