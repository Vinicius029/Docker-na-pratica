# Lista de comandos mais importantes (CLI)

## Container
| Ação                                    | Comando                           |
| --------------------------------------- | --------------------------------- |
| Rodar um container                      | `docker run imagem`               |
| Rodar com nome                          | `docker run --name meuapp imagem` |
| Rodar em background                     | `docker run -d imagem`            |
| Expor porta                             | `docker run -p 8080:80 imagem`    |
| Executar um comando dentro do container | `docker exec -it nome bash`       |
| Parar container                         | `docker stop nome`                |
| Iniciar container parado                | `docker start nome`               |
| Reiniciar                               | `docker restart nome`             |
| Remover container                       | `docker rm nome`                  |
| Força remoção container                 | `docker rm -f nome`               |
| Ver containers rodando                  | `docker ps`                       |
| Ver containers (todos)                  | `docker ps -a`                    |
| Ver logs                                | `docker logs nome`                |
| Ver logs em tempo real                  | `docker logs -f nome`             |
| Copiar arquivo para container           | `docker cp arquivo nome:/caminho` |
| Copiar do container                     | `docker cp nome:/caminho ./local` |

## Imagens
| Ação                      | Comando                  |
| ------------------------- | ------------------------ |
| Criar imagem              | `docker build -t nome .` |
| Criar imagem com tag      | `docker build -t app:v1.0.1 .`|
| Adicionar tag na imagem   | `docker image tag app:v1.0.1 vinicius029/appteste:v1`|
| Listar imagens            | `docker images`          |
| Remover imagem            | `docker rmi nome`        |
| Força remoção imagem      | `docker rmi -f nome`     |
| Fazer pull                | `docker pull ubuntu`     |
| Fazer push                | `docker push nome`       |
| Limpar imagens não usadas | `docker image prune`     |
| Compactar imagem          | `docker image save -o appv1.tar app:v1.0.1`|
| Desconpactar imagem       | `docker image load -i appv1.tar`|


## Volumes
| Ação               | Comando                          |
| ------------------ | -------------------------------- |
| Criar volume       | `docker volume create meuvolume` |
| Listar volumes     | `docker volume ls`               |
| Inspecionar volume | `docker volume inspect nome`     |
| Remover volume     | `docker volume rm nome`          |

## Networks
| Ação                      | Comando                                 |
| ------------------------- | --------------------------------------- |
| Criar rede                | `docker network create minha-rede`      |
| Listar redes              | `docker network ls`                     |
| Inspecionar rede          | `docker network inspect nome`           |
| Remover rede              | `docker network rm nome`                |
| Conectar container à rede | `docker network connect rede container` |

## Sistema
| Ação                                        | Comando                            |
| ------------------------------------------- | ---------------------------------- |
| Ver espaço usado                            | `docker system df`                 |
| Limpar tudo que não está sendo usado        | `docker system prune`              |
| Limpar tudo mesmo (imagens, redes, volumes) | `docker system prune -a --volumes` |

## Comandos do docker compose
| Ação                               | Comando                         |
| ---------------------------------- | ------------------------------- |
| Subir tudo                         | `docker compose up`             |
| Subir em background                | `docker compose up -d`          |
| Parar containers                   | `docker compose down`           |
| Listar serviços                    | `docker compose ps`             |
| Reconstruir imagens                | `docker compose build`          |
| Subir somente 1 serviço            | `docker compose up nome`        |
| Ver logs                           | `docker compose logs`           |
| Logs em tempo real                 | `docker compose logs -f`        |
| Executar comando dentro do serviço | `docker compose exec nome bash` |

## Comando Avançados
| Ação                         | Comando                                |
| ---------------------------- | -------------------------------------- |
| Inspecionar container        | `docker inspect nome`                  |
| Entrar no shell do container | `docker exec -it nome sh`              |
| Stats (uso de CPU, RAM)      | `docker stats`                         |
| Ver camadas da imagem        | `docker history nome`                  |
| Testar rede entre containers | `docker exec nome ping outrocontainer` |
