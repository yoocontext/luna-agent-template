# IoC guide

## Structure

```text
src/bootstrap/ioc/
  container.py
  providers/{layer}/...
```

## Provider location rule

`src/bootstrap/ioc/providers/` mirrors `src/` by ownership and layer.
Provider files may group lifecycle wiring for a subsystem or entity instead of
matching every source file one-to-one.

Source file:

```text
src/infra/dm/user.py
```

Provider file:

```text
src/bootstrap/ioc/providers/infra/dm.py
```

## Provider responsibility

A provider manages the object lifecycle.

Example:

```text
../providers/infra/alchemy.py
```
