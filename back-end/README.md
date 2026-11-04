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

You have just run a numerical optimization to allocate a fixed marketing budget across two channels: search and social.

The objective is to maximize the modeled return: each dollar allocated to search produces two units of return, and each dollar allocated to social produces one. Allocations must be nonnegative and sum to the fixed budget.

The solver returned the values below. Review the validation code before these results are published.

```python
import numpy as np

# Constraint: allocate exactly $100 across search and social.
# Each allocation must be nonnegative.
budget = 100.0

# Results returned by the numerical solver.
# Allocation order: [search, social], in dollars.
allocation = np.array([60.0, 50.0])
solver_success = True
solve_objective_value = 120.0


def calculate_objective_value(allocation):
    """Evaluate the modeled return for a given allocation."""
    search_spend, social_spend = allocation
    return 2.0 * search_spend + social_spend


# Validate the solver results before publishing them.
assert solver_success
assert np.isclose(solve_objective_value, solve_objective_value)

print("Validated")
```

The code prints “Validated”. What does it actually establish? Are these solver results valid, and what checks would you add?
