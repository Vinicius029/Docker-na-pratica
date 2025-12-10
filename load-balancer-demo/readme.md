# Load Balancer com Docker e Nginx

Projeto educacional demonstrando conceitos de Load Balancing, Docker Compose, e arquitetura distribuída.

---

## Sobre o Projeto

Este projeto demonstra como implementar um **Load Balancer** usando **Nginx** e **Docker Compose** para distribuir requisições entre múltiplas instâncias de uma aplicação Flask.

### O que é Load Balancer?

Load Balancer (Balanceador de Carga) é um componente que distribui requisições entre múltiplos servidores, proporcionando:

- **Performance**: Distribui a carga entre vários servidores
- **Alta Disponibilidade**: Se um servidor cair, os outros continuam funcionando
- **Escalabilidade**: Fácil adicionar mais servidores quando necessário
- **Manutenção sem Downtime**: Atualiza servidores um por vez

---

## Conceitos Aprendidos

### Docker
- Containers e isolamento
- Docker Compose para orquestração
- Networking entre containers
- Healthchecks
- Port mapping

### Load Balancing
- Algoritmo Round Robin
- Proxy reverso
- Distribuição de carga
- Detecção de falhas automática

### Nginx
- Configuração de upstream
- Proxy pass
- Headers HTTP
- Status monitoring

---

## Arquitetura

```
┌─────────────────────────────────────────────────────┐
│                  Cliente/Navegador                  │
│              http://localhost:8080                  │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│            Nginx (Load Balancer)                    │
│                  Porta: 8080                        │
│                                                     │
│  Algoritmo: Round Robin                            │
│  upstream backend {                                │
│    server app1:5000;                              │
│    server app2:5000;                              │
│    server app3:5000;                              │
│  }                                                  │
└───────┬─────────────────┬─────────────────┬─────────┘
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ app-server-1 │  │ app-server-2 │  │ app-server-3 │
│  Flask API   │  │  Flask API   │  │  Flask API   │
│ Porta: 5000  │  │ Porta: 5000  │  │ Porta: 5000  │
└──────────────┘  └──────────────┘  └──────────────┘
```

**Fluxo de Requisição:**
1. Cliente acessa `localhost:8080`
2. Nginx recebe a requisição
3. Nginx escolhe um servidor backend (Round Robin)
4. Servidor processa e retorna resposta
5. Nginx repassa resposta ao cliente

---

## Pré-requisitos

- Docker 20.10+
- Docker Compose 2.0+
- curl (para testes)
- jq (opcional, para formatar JSON)

### Instalação do Docker

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose-plugin

# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER

# Fazer logout e login novamente
```
---

## Instalação e Execução

### 1. Clone ou crie a estrutura do projeto

```bash
mkdir -p load-balancer-demo/{app,nginx}
cd load-balancer-demo
```

### 2. Subir o projeto

```bash
# Construir as imagens
docker compose build

# Subir todos os serviços
docker compose up -d

# Ver status
docker compose ps

# Ver logs
docker compose logs -f
```

### 3. Acessar a aplicação

```
http://localhost:8080/
```

---

## Como Funciona

### Round Robin (Algoritmo Padrão)

O Nginx distribui as requisições em ordem circular:

```
Requisição 1 → app-server-1
Requisição 2 → app-server-2
Requisição 3 → app-server-3
Requisição 4 → app-server-1 (volta ao início)
Requisição 5 → app-server-2
...
```

### Docker Networking

Todos os containers estão na mesma rede (`app-network`):

- O Nginx consegue acessar `app1:5000` usando o nome do serviço
- O Docker resolve automaticamente para o IP interno
- Isolamento: apenas containers na mesma rede se comunicam

### Healthchecks

Cada aplicação tem um healthcheck que:
- Testa a cada 10 segundos
- Aguarda 5 segundos por resposta
- Tenta 3 vezes antes de marcar como unhealthy
- Garante que o Nginx só envia requisições para servidores saudáveis

---

## Testando o Load Balancer

### Teste 1: Ver qual servidor atende

```bash
# Fazer 12 requisições
for i in {1..12}; do
  echo "Requisição $i:"
  curl -s http://localhost:8080/ | jq '.servidor'
done
```

**Resultado esperado:**
```
"app-server-1"
"app-server-2"
"app-server-3"
"app-server-1"
"app-server-2"
"app-server-3"
...
```

### Teste 2: Ver contadores individuais

```bash
# Cada servidor mantém seu próprio contador
for i in {1..9}; do
  curl -s http://localhost:8080/ | jq '{servidor, requisicoes: .requisicoes_atendidas}'
done
```

### Teste 3: Simular falha de servidor

```bash
# Parar o app2
docker compose stop app2

# Fazer requisições
for i in {1..9}; do
  curl -s http://localhost:8080/ | jq -r '.servidor'
done

# Resultado: Só mostra app-server-1 e app-server-3
# O Nginx detectou automaticamente que app2 está fora!

# Reativar
docker compose start app2
```

### Teste 4: Ver estatísticas

```bash
# Estatísticas de cada servidor
curl http://localhost:8080/stats | jq

# Status do Nginx
curl http://localhost:8080/nginx-status
```

### Teste 5: Teste de carga (Apache Bench)

```bash
# Instalar apache bench
sudo apt install apache2-utils

# 1000 requisições, 10 concorrentes
ab -n 1000 -c 10 http://localhost:8080/

# Ver como foi distribuído
docker compose logs app1 | grep -c "GET / HTTP"
docker compose logs app2 | grep -c "GET / HTTP"
docker compose logs app3 | grep -c "GET / HTTP"
```

---

## 📝 Comandos Úteis

### Gerenciamento de Containers

```bash
# Ver status
docker compose ps

# Ver logs em tempo real
docker compose logs -f

# Ver logs de um serviço específico
docker compose logs app1

# Parar um serviço
docker compose stop app2

# Iniciar serviço parado
docker compose start app2

# Reiniciar um serviço
docker compose restart nginx

# Parar tudo
docker compose down

# Parar tudo e remover volumes
docker compose down -v
```

### Escalar Serviços

```bash
# Rodar 5 instâncias do app
docker compose up -d --scale app1=5

# Ver todas as instâncias
docker compose ps
```

### Debug

```bash
# Entrar em um container
docker compose exec app1 bash

# Ver configuração do Nginx
docker compose exec nginx cat /etc/nginx/nginx.conf

# Testar configuração do Nginx
docker compose exec nginx nginx -t

# Recarregar configuração do Nginx (sem parar)
docker compose exec nginx nginx -s reload

# Ver processos em um container
docker compose top app1

# Ver uso de recursos
docker stats
```

### Networking

```bash
# Listar redes
docker network ls

# Ver detalhes da rede
docker network inspect load-balancer-demo_app-network

# Testar conectividade entre containers
docker compose exec app1 ping app2
docker compose exec nginx wget -O- http://app1:5000/health
```

---

## Algoritmos de Load Balancing

### 1. Round Robin (Padrão)

```nginx
upstream backend {
    server app1:5000;
    server app2:5000;
    server app3:5000;
}
```

Distribui requisições em ordem circular.

### 2. Least Connections

```nginx
upstream backend {
    least_conn;
    server app1:5000;
    server app2:5000;
    server app3:5000;
}
```

Envia para o servidor com menos conexões ativas.

### 3. IP Hash (Sessões Persistentes)

```nginx
upstream backend {
    ip_hash;
    server app1:5000;
    server app2:5000;
    server app3:5000;
}
```

Mesmo cliente sempre vai para o mesmo servidor.

### 4. Weighted (Pesos)

```nginx
upstream backend {
    server app1:5000 weight=3;  # Recebe 3x mais
    server app2:5000 weight=2;  # Recebe 2x mais
    server app3:5000 weight=1;  # Recebe 1x
}
```

Distribui baseado em pesos (útil quando servidores têm capacidades diferentes).

### 5. Com Backup

```nginx
upstream backend {
    server app1:5000;
    server app2:5000;
    server app3:5000 backup;  # Só usa se outros falharem
}
```

### 6. Com Health Checks

```nginx
upstream backend {
    server app1:5000 max_fails=3 fail_timeout=30s;
    server app2:5000 max_fails=3 fail_timeout=30s;
    server app3:5000 max_fails=3 fail_timeout=30s;
}
```

- `max_fails=3`: Após 3 falhas, marca como down
- `fail_timeout=30s`: Aguarda 30s antes de tentar novamente

---

## Troubleshooting

### Containers aparecem como "unhealthy"

**Causa:** Falta o `curl` na imagem Python.

**Solução 1:** Adicionar curl no Dockerfile (já incluído acima)

**Solução 2:** Remover o healthcheck do `docker-compose.yml`

### Nginx não inicia (Exited)

**Causa comum:** Erro de sintaxe no `nginx.conf`

```bash
# Ver erro
docker compose logs nginx

# Testar configuração
docker compose run --rm nginx nginx -t
```

**Erro comum:** `upstream` fora do bloco `http`

### Porta 8080 já está em uso

```bash
# Ver o que está usando a porta
sudo lsof -i :8080

# Matar o processo
sudo kill PID

# Ou usar outra porta no docker-compose.yml
ports:
  - "9000:80"
```

### Containers não se comunicam

```bash
# Verificar se estão na mesma rede
docker network inspect load-balancer-demo_app-network

# Testar conectividade
docker compose exec nginx ping app1
```

### "no such service" ao executar comandos

**Erro:** `docker compose stop app-server-1` → erro!

**Correto:** Use o nome do **SERVIÇO**, não do container:

```bash
docker compose stop app1  
docker stop app-server-1  
```