
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Описание функций и примеры вызовов
## `calculate.py`
### `calc(fig, func, size)`
- Возвращает значение функции для фигуры с заданными параметрами. :shipit:

  Пример вызова:
```python
>> calc('circle', 'perimeter', {5})
perimeter of circle is 31.41592653589793
```

## `circle.py`
### `area(r)`
- Вычисляет значение площади окружности радиуса r. :shipit:
  
Пример вызова:
```python
>> area(3.14)
30.959144000000002
```

### `perimeter(r)`
- Вычисляет значение длины окружности радиуса r. :shipit:
  
Пример вызова:
```python
>> perimeter(3.14)
19.7192
```

## `square.py`
### `area(a)`
- Вычисляет значение площади квадрата со стороой a. :shipit:
  
Пример вызова:
```python
>> area(3)
9
```

### `perimeter(a)`
- Вычисляет значение периметра квадрата со стороой a. :shipit:
  
Пример вызова:
```python
>> perimeter(3)
12
```

## `triangle.py`
### `area(a, b, c)`
- Вычисляет значение полупериметра треугольника со сторонами a, b, c. :shipit:
  
Пример вызова:
```python
>> area(1, 2, 3)
2.0
```

### `perimeter(a, b, c)`
- Вычисляет значение периметра треугольника со сторонами a, b, c. :shipit:
  
Пример вызова:
```python
>> perimeter(1,2,3)
6
```

# История изменения проекта

- d76db2a L-04: Add calculate.py
- 51c40eb L-04: Doc updated for triangle
- d080c78 L-04: Triangle added
- d078c8d (origin/main, origin/HEAD) L-03: Docs added
- 8ba9aeb L-03: Circle and square added
