# Project architecture

- bootstrap — application assembly and dependency wiring.
- delivery — transport layer: controllers, schemas, validation, auth.
- application — business use cases and orchestration.
- infra — external integrations and implementations.

## Layer dependencies

- bootstrap — knows all layers.
- delivery — may know only application.
- application — knows only its own contracts and pure application code.
- infra — knows application contracts and implements external integrations.

### Import rule

- Import only layers listed above.

## src/bootstrap

- Assembly layer, entrypoint.
- Register all new dependencies in `bootstrap/ioc/`.
- Do not instantiate dependencies outside IoC.

## File and folder granularity

### File structure

Prefer small files.

Organize code by feature or domain, then by entity.

```text
payments/tax.py
payments/user/tax.py
```

Refactor freely as the domain evolves:

```text
users.py
→ users/tax.py
→ payments/users/tax.py
```

Do not preserve file structure for backward compatibility. Prefer correct
ownership and cohesion.

## Code rules

Do not create `helpers` or `utils` packages.

Avoid nested classes and nested functions.

Do not introduce constants for configuration values.
Use `settings` sourced from `.env` or `config.toml`.
