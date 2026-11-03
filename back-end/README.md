# Back-end — Numerical code reading and debugging

This assessment takes approximately 15 minutes. Work through the three exercises with your interviewer and explain your reasoning aloud.

Give an initial explanation in your own words. You may then run the snippets and consult documentation. AI assistance is not permitted in this block; the separate live exercise allows AI tools.

The snippets use Python, NumPy, and pandas.

## A1 — NumPy arrays

What does each line print? Explain what `axis=0` means here.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a[a > 2])
print(a.reshape(2, 2).sum(axis=0))
```

## B1 — Channel contributions

What does this code return? Is it correct? What would you change and test?

```python
import pandas as pd

# Each channel's contribution is its spend times its coefficient.
# Channel names identify which values belong together.
spend = pd.Series(
    [100.0, 200.0],
    index=["search", "social"],
)
coefficients = pd.Series(
    [0.2, 0.5],
    index=["social", "search"],
)

contribution = spend.to_numpy() * coefficients.to_numpy()
print(contribution.sum())
```

## B2 — Optimization result

This code prints “Validated”. Is the recommendation valid? Walk me through what these checks establish and what you would add.

```python
import numpy as np

# Allocate exactly this budget across two advertising channels.
# Each allocation must be nonnegative.
budget = 100.0

# Outputs returned by an optimization solver:
# channel order is [search, social].
allocation = np.array([60.0, 50.0])
solver_success = True
reported_value = 120.0  # Objective value reported by the solver.


def calculate_value(allocation):
    """Independently calculate the objective for a given allocation."""
    search_spend, social_spend = allocation
    return 2.0 * search_spend + social_spend


# Validate the result before publishing the recommendation.
assert solver_success
assert np.isclose(reported_value, reported_value)

print("Validated")
```
