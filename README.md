# Docker na Prática

Repositório pessoal de estudos sobre **Docker**, usado como um laboratório para testar, aprender e documentar na prática:

- Criação de imagens e containers
- Uso de `docker-compose`
- Ambientes de desenvolvimento com múltiplos serviços (PHP, Node.js, MySQL, phpMyAdmin, etc.)
- Cenários reais do dia a dia 
> Este repositório é focado em **aprendizado**.  
> Alguns exemplos podem estar simplificados e **não são recomendados** exatamente assim para produção.

---

## Objetivo do repositório

- Registrar minha **evolução** com Docker de forma prática
- Criar um **laboratório** para testar ideias:
  - Ambientes com múltiplos containers
  - Padronização de versões (PHP, Node, banco de dados)
  - Simulação de cenários de Dev/DevOps/Cloud
- Ter uma base pronta para:
  - Estudos futuros de CI/CD
  - Integração com Linux, Shell Script e Cloud

---

## O que você vai encontrar aqui

A ideia é ir organizando em **pastas por cenário**, por exemplo:

- `php-docker/`  
  Ambiente com PHP 8.2, MySQL e phpMyAdmin para rodar **Aplicações PHP**, ajudando a resolver problemas de instalação/compatibilidade em máquinas diferentes.

- `node-basico-docker/`  
  Exemplo simples de aplicação Node.js rodando em container, com `Dockerfile` e, depois, `docker-compose`.

- `python-mysql-docker/`  
  API em flaskApi + banco MySQL, se comunicando via Docker Compose.
  
> Conforme os estudos forem avançando, novas pastas e exemplos vão sendo adicionados.

---

## Pré-requisitos

Para rodar os exemplos deste repositório, você vai precisar de:

- [Docker](https://www.docker.com/) instalado
- [Docker Compose](https://docs.docker.com/compose/)  
  (no Docker Desktop mais recente ele já vem integrado)

Opcional (mas ajuda bastante):

- Git
- Algum editor de código (VS Code, por exemplo)

---

## Como usar este repositório

O padrão da maioria dos exemplos será:

1. Clonar o repositório:

   ```bash
   git clone https://github.com/Vinicius029/Docker-na-pratica.git
   cd Docker-na-pratica

