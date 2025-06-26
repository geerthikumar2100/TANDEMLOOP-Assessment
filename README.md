# TANDEMLOOP-Assessment
### Language Used: 
Python 3

---

### 1: Simple Calculator

#### Description:

This function performs basic operations like add, subtract, multiply, and divide using a class.

#### Example:

```python
calc = Calculator(10, 5, "add")
print(calc.calculate())

15
```

```
calc = Calculator(9, 3, "divide")
print(calc.calculate())

3.0
```

---

### 2: Generate First a Odd Numbers

#### Description:

This function prints the first `n` odd numbers starting from 1.

##### Example:

```python
print(print_odd_series(4))

[1, 3, 5, 7]
```

```python
print(print_odd_series(2))

[1, 3]
```

---

### 3: Print Odd Numbers Up to a

#### Description:

This function prints all odd numbers from 1 up to and including `a` if `a` is odd.

#### Example:

```
print(odd_series_up_to_input(4))

[1, 3]
```

```
print(odd_series_up_to_input(5))

[1, 3, 5]
```

---

### 4: Count Multiples in a List

#### Description:

This function takes a list of numbers and counts how many of them are divisible by each number from 1 to 9.

#### Example:

```python
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(numbers))

{
  1: 11,
  2: 8,
  3: 4,
  4: 4,
  5: 3,
  6: 2,
  7: 0,
  8: 1,
  9: 1
}
```
