![advent of code](https://user-images.githubusercontent.com/23434317/144762233-2dda88fc-f026-4b04-8dff-b4c45f11bc06.jpg)

https://adventofcode.com/2021

# Advent of Code 2021: Python

I'm Noah and here is my first GitHub repository. This is a multi-part project for me, as I am simulatneously learning GitHub and Python. I have a background in Computer Engineering, so I am familiar with a lot of concepts, just not the syntax behind them. I've decided to try my hand at this year's [Advent of Code](https://adventofcode.com/) as a beginner Python developer. Since I'm still learning, there will obviously be a ton of room for improvement! I'm learning a ton every day, and I hope I can improve and solidify my skills by attempting these fun challenges. I think as a nice bit of information, I will add any important lessons or tricks I've learned to the section below - not only to help myself, but to also help any other self-studying Python developers out there. Full disclosure, I may be picking and copying from other solutions for educational purposes, and to help expose me to multiple workflows. 😊

Thanks for reading!

## Lessons Learned
### Day 1:
The .zip() method takes multiple iterables and returns an iterator of tuples. Very handy!
```python
list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]
result = zip(list_1,list_2)
print(list(result))

#Output:
[('a', 1), ('b', 2), ('c', 3)]
```
List comprehension can dramatically reduce the amount of code needed for for-loops:
```python
# counts number of times x is less than y
ans = sum(x < y for x, y in zip(depths, depths[1:]))
```

### Day 2:
The .rstrip() method removes any trailing characters from a string. Useful when reading in data:
```python
#read in data and remove '\n' characters
data = [line.rstrip('\n') for line in open("day_02.txt")]
```

The pandas.DataFrame.iterrows() method can iterate over DataFrame rows as an (index, Series) pair:
```python
#for each row, do something 
for index, r in directions.iterrows():
```

### Day 3:
You can initialize mutltiple variables at the same time:
```python
var1 = var 2 = var3 = 0
```
Using the .zip() method to effectively transpose rows & columns:
```python
#transposes the list of strings (while combining them into one string)
data_t = [''.join(s) for s in zip(*data)]
```

Using .iloc() to access specific values in a DataFrame:
```python
#gets the value in the 'ogr' column in the first row of binary1
ogr = int(binary1.iloc[0]['ogr'], 2)
```

### Day 4
When reading in data, it's best to chain several methods to save code:
```python
#reads in data, strips whitespace and splits by newlines
data = [x for x in open('day_04.txt').read().strip().split('\n')]
```
Using the .map() function to apply a given function to an iterable:
```python
#drawn numbers: split the strings by comma, and cast each string as an int. Creates a list of ints.
nums = list(map(int,data[0].split(',')))
```

To check if all values in a row are set:
```python
for line in board:
    if len([n for n in line if n in drawn]) == 5: #list of drawn #s
        win = True
```

### Day 5
Using the `with` label is a safer way of opening files:
```python
#read in data
with open("day_05.txt") as f:
    data = f.readlines()
```

You can assign multiple variables after a .split() method:
```python
for r in data:
    start, end = r.split(" -> ")
    sx, sy = [int(i) for i in start.split(',')]
    ex, ey = [int(i) for i in end.split(',')]
    lines.append([sx, sy, ex, ey])

#a similar thing can be achieved with .map():
sx, sy = map(int, start.split(','))
```

Using np.count_nonzero() to count nonzero values in an np.array with given condition
```python
#counts nonzero values in overlap that are > 1
np.count_nonzero(overlap > 1)
```

### Day 6
`defaultdict` can be useful for counting (amongst other useful things)
```python
ages = defaultdict(int)
for f in fish:
    ages[f] += 1
```

### Day 7

### Day 8

### Day 9

### Day 10

### Day 11

### Day 12

### Day 13

### Day 14

### Day 15

### Day 16

### Day 17

### Day 18

### Day 19

### Day 20

### Day 21

### Day 22

### Day 23

### Day 24

### Day 25
