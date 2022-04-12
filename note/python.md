# Python-note

### re module

- re.match vs re.search
  - `re.match` searchs only from the **beginning of** the string
- re.findall
  - `re.findall` returns all non-overlapping matches of pattern in string, as a **list of strings or tuples**.

### FP in python

```python
from functools import reduce

# go
def go(*functions):
    return reduce(lambda x, f: f(x), functions)
```

### Iterator

```python
# get iterator object
iterator = iter(iterable)

# loop using next method
next(iterator)
next(iterator)
# ...
next(iterator) # Error iterator value is emtpy

```

### Time

- 시각 [s1,e1] 는 [s2, e2]의 구간에 포함된다.
  1. s1 <= e2
  2. e1 >= s2

```python
# 'hh:mm:ss' => second
def second_of(date):
    h,m,s = map(int,date.split(':'))
    return h * 3600 + m * 60 + s

# second => 'hh:mm:ss"
def format_of(second):
    ans = []
    quotient_list = [3600, 60, 1]

    for quotient in quotient_list:
        ans.append(str(second // quotient))
        second %= quotient

    return ':'.join(ans)

```

### Prime number

```python
def is_prime(n):
  for i in range(2, int(n ** 0.5) + 1):
      if x % i == 0:
          return False
  return True

```

### Ref.

- [geeksforgeeks](https://www.geeksforgeeks.org/python-re-search-vs-re-match/)
- [python-docs](https://docs.python.org/)
