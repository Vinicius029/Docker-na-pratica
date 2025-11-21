### Construir/reconstruir imagens
```bash
    docker compose build
```

### Subir todos os serviços
```bash
    docker compose up
```

### Em segundo plano (detached)
```bash
    docker compose up
```

### Ver logs
```bash
    docker compose logs
```

### Ver logs em tempo real
```bash
    docker compose logs -f
```

### Ver logs de um serviço específico
```bash
    docker compose logs web
```

### Ver status dos serviços
```bash
    docker compose ps
```

### Parar tudo
```bash
    docker compose down
```

### Parar e REMOVER os volumes (deleta dados do banco)
```bash
    docker compose down -v
```

### Executar comando dentro de um serviço
```bash
    docker compose exec web bash
    docker compose exec db psql -U postgres -d todoapp
```

## Rodar 3 instâncias simultaneamente
Ter 3 containers da aplicação rodando ao mesmo tempo, todos usando o mesmo banco de dados!

Remover container-name e deixar range das porta no `docker-compose.yml`
```yml
    web:
    build: .
    # Sem container_name (para permitir múltiplas instâncias)
    # Sem ports fixos
    ports:
      - "8080-8082:8080"  # ← Mapeia para portas 8080, 8081, 8082
    environment:
      DB_HOST: db
      DB_NAME: todoapp
      DB_USER: postgres
      DB_PASS: senha123
    depends_on:
      db:
        condition: service_healthy
    networks:
      - todo-network
```

```bash
# Parar tudo
docker compose down

# Subir com 3 instâncias
docker compose up -d --scale web=3

# Ver status
docker compose ps
```

Você verá algo assim:
```
NAME                           STATUS    PORTS
todo-postgres                  Up        
03-todo-app-compose-web-1      Up        0.0.0.0:8080->8080/tcp
03-todo-app-compose-web-2      Up        0.0.0.0:8081->8080/tcp
03-todo-app-compose-web-3      Up        0.0.0.0:8082->8080/tcp
```

---

## Testar as 3 instâncias

Abra 3 abas no navegador:
```
http://localhost:8080  ← Instância 1
http://localhost:8081  ← Instância 2
http://localhost:8082  ← Instância 3
```
