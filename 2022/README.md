# Advent of Code 2022 Walkthrough

## Table of Contents
* [Day 01 - Calorie Counting](https://github.com/noah-kg/AdventOfCode/new/main/2022#day-01---calorie-counting)

## Day 01 - Calorie Counting
[Problem](https://adventofcode.com/2022/day/1) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day%2001%20-%20Calorie%20Counting.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

### Part 1
We are given a list of integers representing the amount of calories for each snack that each elf is carrying. Each elf's list of snacks is separated by a new line. We need to parse this list, separate it into "chunks" (one chunk would be a single elf's snacks), and return the value of the elf with the most calories.

First, we need to parse the input into chunks (each chunk represents a singluar elf) - which can be done with the [split()](https://docs.python.org/3/library/stdtypes.html#str.split) method. Then we use [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) and the [map()](https://docs.python.org/3/library/functions.html#map) function to convert each item in a chunk to an integer:

```python
chunks = fin.read().split('\n\n')
chunks = [tuple(map(int, chunk.split())) for chunk in chunks]
```

Then it's just a matter of returning the biggest number by using the [max()](https://docs.python.org/3/library/functions.html#max) function:

```python
most = max(map(sum, chunks))
```

### Part 2
For part two we are told that instead of getting the elf with the most calories, we need the top 3 elves with the most calories. We can easily achieve this using the [sort()](https://docs.python.org/3/library/stdtypes.html#list.sort) method. We use ```key=sum``` so that the list of chunks is sorted based on the sum of their values. We also need to sort in descending order, so we set ```reverse=True```.

```python
chunks.sort(key=sum, reverse=True)
top3 = sum(map(sum, chunks[:3]))
```
