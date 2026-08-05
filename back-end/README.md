# mystery-box

## Python

A 1.

```python
def somefunction(*args, **kwargs):
    print(args)
    print(kwargs)


somefunction('A', 2, name='Harry')
```

A 2.

```python
def multiply_number(num):
    def product(number):
        return num * number
    return product

num_t = multiply_number(2)

print(num_t(11))
print(num_t(4))
```

A 3.

```python
f = None

for i in range(5):
    with open("data.txt", "w") as f:
        if i > 2:
            break

print(f.closed)
```

A 4.

```python
values = [2, 33, 43, 111, 225]

print(values[-1])
print(values[1:3])
```

A 5.

```python
def somefunction():
    for val in [1, 33, 44]:
        yield val

f = somefunction()
print(next(f))
print([i for i in f])
```

A 6.

```python
def decorator(func):
    return lambda: "World " + func()

@decorator
def greet():
    return "Hello"

print(greet())
```

A 7.

```python
fruits = ["apple", "banana", "cherry"]
prices = [1.2, 0.5, 2.3]
print({fruit: price for fruit, price in zip(fruits, prices)})
```

A 8.

```python
import time
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"

async def main():
    results = await asyncio.gather(greet("Alice"), greet("Bob"))
    print(results)

start = time.time()
asyncio.run(main())
print(round(time.time() - start))
```

A 9.

```python
import numpy as np
a = np.array([1, 2, 3, 4])
print(a[a > 2])
print(a.reshape(2, 2).sum(axis=0))
```

B 1.

```python
def aggregate_by_week(data):
    week_number_to_value = {}
    week_number = 0
    for i, item in enumerate(data):
        if i % 7 == 0:
            week_number += 1
        week_number_to_value[week_number] += item
    print(week_number_to_value)

aggregate_by_week([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

B 2.

```python
import numpy as np

def softmax(x: np.ndarray) -> np.ndarray:
    e = np.exp(x)
    return e / e.sum()
```

