# Networks

Como um container fala com outro? Eles precisam estar na mesma rede!
```yaml
    networks:
  - todo-network
```

---

## Como funciona
```
┌──────────────────────────────────────────┐
│         Rede: todo-network               │
│                                          │
│  ┌─────────────┐      ┌─────────────┐  │
│  │ Container   │      │ Container   │  │
│  │    web      │ ←──→ │     db      │  │
│  │             │      │             │  │
│  └─────────────┘      └─────────────┘  │
│                                          │
└──────────────────────────────────────────┘
```
* O container web pode acessar o db usando o nome do serviço
* É como um DNS interno: db = endereço do banco

## Tipos de drivers de rede
Bridge (padrão):
```yaml
    networks:
        todo-network:
            driver: bridge  # ← Mais comum
```
* Cria uma rede isolada
* Containers se comunicam entre si
* Podem acessar a internet
* Use sempre esse!

Host:
```yaml
    networks:
        todo-network:
            driver: host
```
* Container usa a rede do seu PC diretamente
* Sem isolamento
* Raramente usado
