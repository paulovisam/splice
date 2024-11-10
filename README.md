# Splice Project

Bem-vindo ao projeto Splice!

## Instalação

Para instalar o projeto, siga os passos abaixo:

```bash
poetry install
poetry shell

cp .env.example .env
task alembic_upgrade
task run
```

## Comandos

- **task format**: Formata o código-fonte do projeto de acordo com as convenções de estilo definidas.
- **task run**: Executa a aplicação principal do projeto.
- **task test**: Executa a suíte de testes para verificar a integridade e funcionalidade do código.
- **task alembic_upgrade**: Aplica as migrações de banco de dados pendentes usando o Alembic.
- **task alembic_downgrade**: Reverte as migrações de banco de dados aplicadas usando o Alembic.
- **task alembic_down_up**: Reverte e reaplica as migrações de banco de dados, útil para garantir que as migrações sejam idempotentes.

task format
task run
task test
task alembic_upgrade
task alembic_downgrade
task alembic_down_up
