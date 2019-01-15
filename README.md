# mystery-box

## Javascript

1.

What does the following code output?

```javascript
const data = 1;

function add(data) {
  data += 1;
}

console.log(add(data));
console.log(data);
```

2.

What does the following code output?

```javascript
const data = [];

function populate(data) {
  data.push(10);
}

console.log(populate(data));
console.log(data);
```

3.

What does the following code output?

```javascript
const users = {
  names: ['John', 'Harry'],
  quality: 'awesome',
  makeAwesome: function() {
    return this.names.map(function(name) {
      return `${name} is really ${this.quality}`;
    });
  }
};

console.log(users.makeAwesome());
```


4.

What does the following code output?

```javascript
const getValue = (value) => {
  return {
    get: () => value
  };
};

const obj = getValue(1);

console.log(obj.get());
```

5.

What does the following code output?

```javascript
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log('Index: ' + i + ', element: ' + arr[i]);
  }, 3000);
}
```


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

for i in range (5):
    with open("data.txt", "r") as f:
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
