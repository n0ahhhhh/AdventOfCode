# Advent of Code 2022 Walkthrough

## Table of Contents
* [Day 01 - Calorie Counting](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-01---calorie-counting)
* [Day 02 - Rock, Paper, Scissors](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-02---rock-paper-scissors)
* [Day 03 - Rucksack Reorganization](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-03---rucksack-reorganization)
* [Day 04 - Camp Cleanup](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-04---camp-cleanup)
* [Day 05 - Supply Stacks](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-05---supply-stacks)
* [Day 06 - Tuning Trouble](https://github.com/noah-kg/AdventOfCode/blob/main/2022/README.md#day-06---tuning-trouble)

## Day 01 - Calorie Counting
[Problem](https://adventofcode.com/2022/day/1) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_01_Calorie_Counting.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

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
[Problem](https://adventofcode.com/2022/day/3) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_03_Rucksack_Reorganization.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

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
## Day 04 - Camp Cleanup
[Problem](https://adventofcode.com/2022/day/4) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_04_Camp_Cleanup.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

### Part 1
Today we are given a list of pairs of section IDs for which each elf is responsible for cleaning. We need to figure out which pairs have a full overlap of section IDs. For example:

```
Given     Visually
 2-8      .2345678.
 3-7      ..34567..

 6        .....6...
 4-6      ...456...

 2-6      .23456...
 4-8      ...45678.
```

For part one we are only concerned about finding the number of assignment pairs where one range *fully* overlaps the other. In the above, it would be the first and second pairs.

To start, we just need to parse the input and [split()](https://docs.python.org/3/library/stdtypes.html#str.split) it into appropriate pieces of data, while not forgetting to [map](https://docs.python.org/3/library/functions.html#map) the inputs to integers:

```python
for line in fin:
    a, b   = line.strip().split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
```

Then we need to calculate the points where the two ranges overlap. We can compute the extremes of the overlap by simply calculating the maximum between the two range start values and the minimum between the two range end values. We can make good use out of the [min()](https://docs.python.org/3/library/functions.html#min) and [max()](https://docs.python.org/3/library/functions.html#max) functions here. 

```python
o1 = max(a1, b1)
o2 = min(a2, b2)

if o1 == a1 and o2 == a2 or o1 == b1 and o2 == b2:
    full_overlap += 1
    
advent.print_answer(1, full_overlap)
```

### Part 2
For part 2, we're tasked with finding out the number of range pairs that overlap paritally *or* fully. The number of pairs from part 1 will still count for part 2. We simply need to calculate partial overlaps. To do this, we can calculate the two extremes of the overlap calculated from part 1:

```
    a1|------------|a2     |            a1|--------|a2
b1|---------|b2            |   b1|--|b2
    o1|-----|o2            |        |o2 o1|
      overlap (o2 >= o1)   |       no overlap (o2 < o1)
```

All of this simply means adding one check to our part 1 code, and since we know that a full overlap is a special case of a partial overlap, we can move the part 1 check inside the part 2 one like so:

```python
if o2 >= o1:
    overlap +=1
    if o1 == a1 and o2 == a2 or o1 == b1 and o2 == b2:
        full_overlap += 1
        
advent.print_answer(2, overlap)
```

## Day 05 - Supply Stacks
[Problem](https://adventofcode.com/2022/day/5) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_05_Supply_Stacks.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

### Part 1
Today is the first puzzle (so far) where parsing the input is more difficult than the actual problem. In today's puzzle, we are simulating a giant crate-moving crane. We are given our initial state of crates:

```
            [M] [S] [S]            
        [M] [N] [L] [T] [Q]        
[G]     [P] [C] [F] [G] [T]        
[B]     [J] [D] [P] [V] [F] [F]    
[D]     [D] [G] [C] [Z] [H] [B] [G]
[C] [G] [Q] [L] [N] [D] [M] [D] [Q]
[P] [V] [S] [S] [B] [B] [Z] [M] [C]
[R] [H] [N] [P] [J] [Q] [B] [C] [F]
 1   2   3   4   5   6   7   8   9
 ```
 
 After a line break we are also given a long list of instructions in the form ```move [n] from [i] to [j]```, like the following:
 
 ```
move 1 from 7 to 4
move 3 from 4 to 7
move 4 from 3 to 4
```

After executing all instructions, we need to combine the letters from each of the topmost crates in each stack. For example, if the above configuration was the outcome after all instructions, our answer would be ```GGMMSSQFG```. The easiest way of doing this is to effectively transpose each row of input, which would essentially give us the columns. The [zip()](https://docs.python.org/3/library/functions.html#zip) function, as well as an [unpacking operator](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists) can make this much easier.

```python
inp = []

for line in fin:
    if line == '\n': #we stop at the line break
        break
    inp.append(line)
```

Then we use zip() to transpose the input. After transposing, we only need to take 1 from every 4 characters (the capital letter). Using the [modulo](https://docs.python.org/3.3/reference/expressions.html#binary-arithmetic-operations) operator makes this simple too. I won't go into too much detail about parsing this, because frankly it was really annoying.

```python
stacks = [None]
moves = []

cols = list(zip(*inp)) #transposes each column

for i, col in enumerate(cols):
    if i % 4 == 1:
        stacks.append(''.join(col[:-1]).lstrip())
        
original = stacks[:] #create copy for part 2
```

We then need to parse the actual instructions, which is thankfully more straightforward than the previous bit since we only care about the numbers, not the words.

```python
for line in fin:
    line = line.split()
    moves.append((int(line[1]), int(line[3]), int(line[5])))
```

Basically, what we need to do is isolate the "chunk" of crates that we need to move, update the state of the stack it came from, and then update the stack where the chunk is going. Because part 2 is similar, I've already turned the code into a function.

```python
def move_crates(stacks, moves, rev=True):
    for n, i, j in moves:
        if rev: chunk = stacks[i][:n][::-1] #part1
        else: chunk = stacks[i][:n]         #part2
        stacks[i] = stacks[i][n:]           #updates source stack after removing top crate
        stacks[j] = chunk + stacks[j]       #updates destination stack after adding crate
    
    return ''.join(s[0] for s in stacks[1:]) 
    
ans1 = move_crates(stacks, moves)
advent.print_answer(1, ans1)
```

### Part 2
For part 2 we learn that our crate-moving crane is actually capable of moving multiple boxes at the same time, as opposed to moving only one at a time. We now how to redo the instructions again using this new information. All that changes really, is how we define the "chunk" that gets moved. Previously, we needed to reverse it since each crate was moved individually. We no longer have to reverse it since all the crates get moved together. The important thing is to restore our stacks to their original state, which is why we made a copy earlier.

```python
stacks = original #restores from copy we made earlier
ans2 = move_crates(stacks, moves, False)

advent.print_answer(2, ans2)
```

## Day 06 - Tuning Trouble
[Problem](https://adventofcode.com/2022/day/6) - [Solution](https://github.com/noah-kg/AdventOfCode/blob/main/2022/solutions/Day_06_Tuning_Trouble.ipynb) - [Back to top](https://github.com/noah-kg/AdventOfCode/tree/main/2022#advent-of-code-2022-walkthrough)

### Part 1
We're given one very long string (which I have named ```buffer```) filled with seemingly random characters. Our goal is to find the ```start-of-packet``` message, which contains ```4``` unique characters. This is incredibly simple with the use of the ```set``` data structure, and a simple ```for loop```. All that we need to do is start and the first character ```i```, and create a set that goes to ```i + 4```. If the length of that set is equal to 4, we have found our message.

```python
for i in range(len(buffer) - 4):
    if len(set(buffer[i:i+4])) == 4:
        return i + 4 
```

### Part 2
Part 2 is identical to part 1, except now instead of checking for a packet that is 4 unique characters long, we need to find a packet that is 14 characters long. Following the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle, instead of repeating our code from part 1, we can turn it into a function instead. We can pass in the length of the message we're looking for as an argument.

```python
def find_marker(m_len):
    for i in range(len(buffer) - (m_len)):
        if len(set(buffer[i:i+m_len])) == m_len:
            return i + m_len        
        
ans1 = find_marker(4)  #start-of-packet
ans2 = find_marker(14) #start-of-message

advent.print_answer(1, ans1)
advent.print_answer(2, ans2)
```
