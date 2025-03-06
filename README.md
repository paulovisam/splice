# Splice Project

Bem-vindo ao projeto Splice!

## Instalação

Para instalar o projeto, siga os passos abaixo:

```bash
poetry install
poetry shell

cp .env.example .env #Altere o env com as credenciais do psql
docker compose up -d #Subir banco em 5432
createdb splice #Criar banco de dados
task alembic_upgrade #Aplicar migrações
task run #Executar projeto
```

## Comandos

- **task format**: Formata o código-fonte do projeto de acordo com as convenções de estilo definidas.
- **task run**: Executa a aplicação principal do projeto.
- **task test**: Executa a suíte de testes para verificar a integridade e funcionalidade do código.
- **task alembic_upgrade**: Aplica as migrações de banco de dados pendentes usando o Alembic.
- **task alembic_downgrade**: Reverte as migrações de banco de dados aplicadas usando o Alembic.
- **task alembic_down_up**: Reverte e reaplica as migrações de banco de dados, útil para garantir que as migrações sejam idempotentes.

---

### Fluxo de Desenvolvimento com Git Flow

Este projeto utiliza o modelo de ramificação Git Flow, que organiza o desenvolvimento em diferentes tipos de branches para facilitar o controle de versão e a entrega contínua. Abaixo estão as principais branches e como utilizá-las durante o desenvolvimento.

Instale com `sudo apt-get install git-flow`
Inicialize `git flow init` e **utilize os valores padrão!**

#### Estrutura de Branches

- **prod**: contém o códigos em produção, sempre em estado estável.

- **homologa**: contém o código com novas features para ser validadas antes de subir para produção

- **develop**: contém o código de desenvolvimento, onde as novas features são integradas antes de serem liberadas para produção.

#### Tipos de Branches

- **Feature**: branches usadas para o desenvolvimento de novas funcionalidades. Devem ser baseadas na branch develop.

- **Release**: branches usadas para preparar uma nova versão de produção. São baseadas em develop e, ao finalizar, devem ser mescladas em prod, homologa e develop.

- **Hotfix**: branches usadas para corrigir rapidamente um problema crítico em produção. São baseadas em prod e, ao finalizar, são mescladas em prod, homologa e develop.

#### Criando uma nova branch:

Ao iniciar:
`git flow tipo-da-branch start nome-da-feature`

Ao finalizar:
`git flow tipo-da-branch finish nome-da-feature`

---

TODO

- Fix warn ao gerar token
- Token gerado é válido somente para operações com aquele usuário
- Enviar email de confimação de conta
- Esqueci minha senha
- Configurar README-AI https://github.com/eli64s/readme-ai
- Docs com Scalar
