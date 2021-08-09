# mystery-box

## Javascript

1.

What does the following consoles output?

```javascript
const data = 1;

function add(data) {
  data += 1;
}

console.log(add(data));
console.log(data);
```

2.

What does the following consoles output?

```javascript
const data = [];

function populate(data) {
  data.push(10);
}

console.log(populate(data));
console.log(data);
```

3.

What does the following console output?

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

What does the following console output?

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

What does the following consoles output?

```javascript
const cars = [
  {
    make: "Kia",
    year: 2010
  },
  {
    make: "Chevy",
    year: 2020
  },
  {
    make: "Audi",
    year: 2000
  }
];

const newCars = [...cars].forEach(car => {
  car.make = care.make + " " + car.year;
});

console.log(cars);
console.log(newCars);

```

6.

What does the following consoles output?

```javascript
const a = {};
const b = {};
console.log(a === b);
console.log(a === a);
console.log(1 == "1");
console.log(1 + 2 + "3");
```

7.

What does the following consoles output?

```javascript
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log('Index: ' + i + ', element: ' + arr[i]);
  }, 3000);
}
```
