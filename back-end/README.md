# mystery-box

## Python

1.

```python
def somefunction(*args, **kwargs):
    print(args)
    print(kwargs)


somefunction('A', 2, name='Harry')
```

2.

```python
def multiply_number(num):
    def product(number):
        return num * number
    return product

num_t = multiply_number(2)

print(num_t(11))
print(num_t(4))
```

3.

```python
f = None

for i in range(5):
    with open("data.txt", "w") as f:
        if i > 2:
            break
 
print(f.closed)
```

4.

```python
values = [2, 33, 43, 111, 225]

print(values[-1])
print(values[1:3])
```

5.

```python
def somefunction():
    for val in [1, 33, 44]:
        yield val

f = somefunction()
print(next(f))
print([i for i in f])
```

6.

```python
def decorator(func):
    return lambda: "World " + func()

@decorator
def greet():
    return "Hello"

print(greet())
```

7.

```python
fruits = ["apple", "banana", "cherry"]
prices = [1.2, 0.5, 2.3]
print({fruit: price for fruit, price in zip(fruits, prices)})
```

8.

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"

async def main():
    results = await asyncio.gather(greet("Alice"), greet("Bob"))
    print(results)

asyncio.run(main())
```
