# A+ Decision Engine Reference Core

Standard-library-only reference implementation of the generic decision aggregation contract.

## Scope
- Applies already-computed hard-constraint checks.
- Aggregates expert-provided soft-preference fit levels (0, 1, 2, or null).
- Keeps evidence coverage separate from fit score.
- Treats missing hard checks as unknown.
- Has no commission input.

It does not parse vendor text, infer specifications, decide category thresholds, or calculate fit from raw specifications. Those rules require Product Expert approval after the MVP category is selected.

## Run tests

```bash
python -m unittest -v
```

No third-party dependency is required. Tests validate the reference contract only, not a production system. Fit score uses only known preference-fit values; evidence coverage reports the weighted proportion with known evaluations. A hard failure excludes a candidate; an unknown hard check is held for verification.
