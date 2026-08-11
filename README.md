# Luna Agent Template

Lightweight Python 3.12 application scaffold with four flat layers, dependency
injection, Docker Compose infrastructure, local `AGENTS.md` guides, and
pre-commit quality checks. It intentionally has no modules or code-generation
workflow.

## Start a project

1. Create a repository with **Use this template**.
2. Replace `project-name` (slugs, images, services) and `project_name`
   (Python/database identifiers) with the real project name.
3. Follow the initialization checklist in the root `AGENTS.md`; keep that file.
4. Install dependencies and hooks:

   ```bash
   uv sync --all-groups
   uv run pre-commit install
   ```

5. Create `.dev.env`:

   ```dotenv
   APP_PORT=8003

   PG__PORT=5432
   PG__DB=project_name
   PG__USER=project_name
   PG__PASSWORD=change-me
   PGADMIN_EMAIL=admin@example.com
   PGADMIN_PASSWORD=change-me
   PGADMIN_PORT=5050

   REDIS__PORT=6379
   REDIS__PASSWORD=change-me

   MINIO__API_PORT=9000
   MINIO__CONSOLE_PORT=9001
   MINIO__ROOT_USER=minioadmin
   MINIO__ROOT_PASSWORD=change-me
   ```

6. Add the project-specific `Dockerfile` and application entrypoint before
   running the app container; this repository provides architecture and
   infrastructure scaffolding, not finished product behavior.

## Commands

```bash
just pg redis minio                 # start infrastructure
just pg-down redis-down minio-down  # stop infrastructure
just app                            # build/start the implemented app

uv run pre-commit run --all-files   # Ruff, mypy, pyright
uv run pytest                       # tests
```

RabbitMQ is not included in Compose; provide a broker and configure
`RMQ__RABBIT_BROKER_URL` when FastStream is used.

## Architecture

| Layer | Responsibility | May depend on |
| --- | --- | --- |
| `bootstrap` | application assembly and IoC | all layers |
| `delivery` | controllers, schemas, validation, auth | `application` |
| `application` | use cases and contracts | its own pure code |
| `infra` | external implementations | application contracts |

Keep dependencies registered in `src/bootstrap/ioc/`. Do not instantiate them
outside IoC, and do not introduce modules or cross-layer imports beyond the
rules in `AGENTS.md`.
