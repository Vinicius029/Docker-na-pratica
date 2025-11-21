# Como funciona na prática

```yaml
    volumes:
  - postgres_data:/var/lib/postgresql/data
```

**Traduzindo:**
- `postgres_data` = nome do volume (um "HD externo" gerenciado pelo Docker)
- `/var/lib/postgresql/data` = pasta DENTRO do container onde o PostgreSQL salva os dados

**É como plugar um pen drive no container!**
```
┌─────────────────────────┐
│   Container PostgreSQL  │
│                         │
│  /var/lib/postgresql/   │
│       /data  ←──────────┼──→ Volume "postgres_data" 
│                         │     (salvo no seu HD real)
└─────────────────────────┘
```
## Tipos de volumes

Named Volume
```yaml
  services:
  db:
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:  # Docker gerencia onde salvar
```
* Docker escolhe onde salvar no seu sistema
* Geralmente em: /var/lib/docker/volumes/

Bind Mount 
```yaml
  services:
  web:
    volumes:
      - ./meu-codigo:/app  # Pasta do seu PC : Pasta no container
```

**Uso:** Desenvolvimento! Você edita o código no seu PC e o container vê as mudanças instantaneamente!
```
Seu PC                    Container
┌──────────────┐         ┌──────────────┐
│ ./meu-codigo │  ←────→ │    /app      │
│   app.py     │         │   app.py     │
│   main.py    │         │   main.py    │
└──────────────┘         └──────────────┘
      ↑                         ↑
      └─────── Mesma pasta! ────┘
```
## Comandos

```bash
  # Listar todos os volumes
  docker volume ls

  # Ver detalhes de um volume específico
  docker volume inspect nome-do-volume

  # Ver onde está salvo no seu sistema
  docker volume inspect postgres_data --format '{{ .Mountpoint }}'

  # Remover volume 
  docker volume rm postgres_data

  # Remover volumes não usados
  docker volume prune

  # Fazer backup de um volume
  docker run --rm -v postgres_data:/data -v $(pwd):/backup \
    ubuntu tar czf /backup/backup.tar.gz /data

