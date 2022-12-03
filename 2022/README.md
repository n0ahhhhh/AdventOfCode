# Advent of Code 2022 Walkthrough

## Table of Contents
* [Day 01 - Calorie Counting](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-01---calorie-counting)
* [Day 02 - Rock, Paper, Scissors](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-02---rock-paper-scissors)

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

## Day 02 - Rock, Paper, Scissors
[Problem](https://adventofcode.com/2022/day/2) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_02_Rock_Paper_Scissors.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

### Part 1
We are given a list of strings depicting rounds of the famous game Rock, Paper, Scissors. Each string is a combination of two letters: ```ABC``` for player one, and ```XYZ``` for player two (us). We don't quite know how to decode the list, but we do know the following: ```A = Rock```, ```B = Paper```, and ```C = Scissors```. Our initial assumption is to assume that ```XYZ``` is what we must play in order to win the round. There are 9 total combinations: ```AX```, ```AY```, ```AZ```, ```BX```, ..., ```CZ```, etc. Each combination has a unique score attached to it. The score is calculated based on two things: the shape we picked (the ```XYZ```) and the outcome of the round (win/lose/draw). A loss counts as ```0 points```, a draw counts as ```3 points```, and a win counts as ```6 points```. We can create a simple dictionary that has 9 keys representing the possible outcomes, with 9 values representing the scores.

```python
scores1 = {
    'AX': 4, #1 + 3 # A (rock)     vs X (rock)     -> draw
    'AY': 8, #2 + 6 # A (rock)     vs Y (paper)    -> win
    'AZ': 3, #3 + 0 # A (rock)     vs Z (scissors) -> loss
    'BX': 1, #1 + 0 # B (paper)    vs X (rock)     -> loss
    'BY': 5, #2 + 3 # B (paper)    vs Y (paper)    -> draw
    'BZ': 9, #3 + 6 # B (paper)    vs Z (scissors) -> win
    'CX': 7, #1 + 6 # C (scissors) vs X (rock)     -> win
    'CY': 2, #2 + 0 # C (scissors) vs Y (paper)    -> loss
    'CZ': 6 #3 + 3  # C (scissors) vs Z (scissors) -> draw
}
```

We can then loop through the list and add up each rounds respective scores to find the answer to part 1.

```python
ans1 = 0
for line in lines:
    a, b = line.strip().split()
    ans1 += scores1[a+b]
```

### Part 2
We are now informed that our initial assumption was incorrect, and that instead of ```XYZ``` needing to be the winning move, it now represents the desired outcome. ```X = lose```, ```Y = draw```, and ```Z = win```. We simply create a second dictionary with the updated scores, and we can calculate the answer to part 2 in the same loop used for part 1!

```python
scores2 = {
    'AX': 3, #3 + 0  A (rock)     vs X (scissors) -> loss
    'AY': 4, #1 + 3  A (rock)     vs Y (rock)     -> draw
    'AZ': 8, #2 + 6  A (rock)     vs Z (paper)    -> win
    'BX': 1, #1 + 0  B (paper)    vs X (rock)     -> loss
    'BY': 5, #2 + 3  B (paper)    vs Y (paper)    -> draw
    'BZ': 9, #3 + 6  B (paper)    vs Z (scissors) -> win
    'CX': 2, #2 + 0  C (scissors) vs X (paper)    -> loss
    'CY': 6, #3 + 3  C (scissors) vs X (scissors) -> draw
    'CZ': 7  #1 + 6  C (scissors) vs X (rock)     -> win
}

lines = list(map(str.strip, fin))
ans1 = ans2 = 0

for line in lines:
    a, b = line.strip().split()
    ans1 += scores1[a+b]
    ans2 += scores2[a+b]
    
advent.print_answer(1, ans1)
advent.print_answer(2, ans2)
```

## Day 03 - Rucksack Reorganization
[Problem](https://adventofcode.com/2022/day/3) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_03_Rucksack_Reogranization.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

### Part 1
We get a list of strings, where each string represents one elf's rucksack. The rucksack is divided into two even compartments, where elements of one compartment are (supposed to be) unique to that compartment. Unfortunately, the main packing elf made a mistake, and some items were put into both compartments by mistake. We have to identify the misplaced item (the one that shows up in both compartments) as well as assign a priority value to it. We then add all the values to get the answer for part 1.

For this, we can make great use of the [set()](https://docs.python.org/3/library/functions.html#func-set) function. This function takes in an object, and returns a set of unique elements within that object. But first, we need to divide each string in half to identify the compartments. Then, we simply initialize a set for each compartment.

```python
comp1 = line[:len(line)//2] #first half
comp2 = line[len(line)//2:] #second half

set1 = set(comp1)
set2 = set(comp2) 
```

The next line is an [intersection](https://docs.python.org/3/tutorial/datastructures.html#sets) operation on the two sets. This finds the element that exists in both sets.

```python
misplaced = set1 & set2
```

So that's part of the equation. The other part is converting each item to a priority. We're told that lowercase letters have priority ```1-26``` and uppercase letters have priority ```27-52```. Thankfully, this is made easier by using [string.ascii_letters](https://docs.python.org/3/library/string.html), which gives us one giant string of letters in alphabetical order. Then, we simply find the index of our misplaced item and add it to our ans1 variable.

```python
LETTERS = string.ascii_letters #concatenation of lowercase and uppercase ascii letters
idx = LETTERS.index(list(misplaced)[0])
ans1 += idx + 1
```
### Part 2
The second half of today's puzzle is a slight variation on the first part. Instead of looking at each rucksack as having two compartments, we now look at groups of three rucksacks, and we look at each rucksack as a whole. We no longer have to worry about compartments. Instead, we have to find which item is common between all three elves in a group. This follows the same process as part 1, with some slight modifications to our loop. We group them by threes, then we use some slick [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to get the set of each elf's items.

```python
while (idx + 2) < len(rucksacks):
    group = rucksacks[idx:idx+3]
    elves = [set(elf) for elf in group]
```

After that, the process is identical to part 1. We have to remember to increment our ```idx``` variable by 3, because we have to group them by threes.

```python
    misplaced = elves[0] & elves[1] & elves[2]
    p = LETTERS.index(list(misplaced)[0])
    ans2 += p + 1
    idx += 3
    
advent.print_answer(1, ans1)
advent.print_answer(2, ans2)
```
