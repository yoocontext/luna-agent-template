# Application layer guide

## Layer structure

- entities — state and invariants; see `entities/AGENTS.md`.
- use_cases — business workflows and orchestration.
- interfaces — contracts between components.
- services — domain rules spanning several entities or ports.

## Where logic goes

| Component | Called by | Responsibility | Transaction |
|---|---|---|---|
| use case | delivery, background jobs | one scenario end to end | owns `commit()` |
| service | use cases, services | domain rule over several entities or ports | never commits |
| entity | use cases, services | rules over its own state | — |
| dm, queries | use cases, services | data access, no decisions | never commits |

Pick the first that fits:

1. A rule over one entity's state → entity method.
2. Data access → dm or queries.
3. An external system → interface in `interfaces/`, implemented in infra.
4. A rule or step sequence that spans several entities or ports and names a
   domain concept → service.
5. Anything else → private method of the use case.

| Logic | Goes to |
|---|---|
| `order.mark_paid(at)` | entity |
| price from order, plan, and promo | service `PricingCalculator` |
| charge a card | interface `IPaymentProvider` |
| send a receipt, only in checkout | private method of checkout use case |

Use cases do not call other use cases; move the shared part into a service.

## Interfaces

One component → one interface.

```text
infra/dm/payments/payment.py
→ interfaces/dm/payments/payment.py

infra/queries/billing/autopay.py
→ interfaces/queries/billing/autopay.py

infra/s3/*
→ interfaces/s3.py
```

See `infra/dm/AGENTS.md` and `infra/queries/AGENTS.md` for what belongs in
`dm` and what belongs in `queries`.
