# Lessons Learned
## Day 1 - Sonar Sweep: [- Problem -](https://adventofcode.com/2021/day/1)
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

## Day 2 - Dive!: [- Problem -](https://adventofcode.com/2021/day/2)
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

## Day 3 - Binary Diagnostic: [- Problem -](https://adventofcode.com/2021/day/3)
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

## Day 4 - Giant Squid: [- Problem -](https://adventofcode.com/2021/day/4)
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

## Day 5 - Hydrothermal Venture: [- Problem -](https://adventofcode.com/2021/day/5)
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

## Day 6 - Lanternfish: [- Problem -](https://adventofcode.com/2021/day/6)
`defaultdict` can be useful for counting (amongst other useful things)
```python
ages = defaultdict(int)
for f in fish:
    ages[f] += 1
```

## Day 7 - The Treachery of Whales: [- Problem -](https://adventofcode.com/2021/day/7)
The `statistics` module has a lot of handy functions, like median.
```python
median = int(statistics.median(data)) #part1
mean = int(statistics.mean(data))
```

## Day 8 - Seven Segment Search: [- Problem -](https://adventofcode.com/2021/day/8)
Programming is hard. Some takeaways:
* SLOW DOWN.
* THINK before you start coding. Write things down, make diagrams, get your thoughts in order FIRST.
* It's okay to not have a beautiful, elegant solution right away.
    
I was stumped and resorted to reddit for my answer. After reading everyone else's solutions, I realized that sometimes it's okay to brute-force things.

## Day 9 - Smoke Basin: [- Problem -](https://adventofcode.com/2021/day/9)
You can return tuples based on a condition:
```python
adjacent = [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]
    return [(a,b) for a,b in adjacent if 0 <= a < N and 0 <= b < M]
```

The `all` statement can check to see if multiple statements are true in a single line:
```python
if all(data[y][x] < data[a][b] for a,b in adjacents(y,x)):
            lowpoints.append((y,x))
```
            
## Day 10 - Syntax Scoring: [- Problem -](https://adventofcode.com/2021/day/10)
Try and think about what steps you can skip or combine.
I solved this puzzle on my own, but later saw other results that condensed my logic in a smarter way.
E.g, use a `dict` to store the point values for `)]}>` instead of how I did it.

## Day 11 - Dumbo Octopus: [- Problem -](https://adventofcode.com/2021/day/11)
`while` loops can help implement a sort of queue so you don't end in some recursion hell, e.g.:
```python
while something > 0:
    do things
        new_things_to_do_stuff_on = foo
    something = new_things_to_do_stuff_on
```

`set()` is a helpful tool to keep track of and easily combine or compare information
```python
all_flashes = set(just_flashed)
    ...
    all_flashes = all_flashes.union(new_flashes)
    just_flashed = new_flashes
```

## Day 12 - Passage Pathing: [- Problem -](https://adventofcode.com/2021/day/12)
Depth First Search (DFS) is helpful for finding paths and solving mazes. Understanding how it works is crucial.
Honestly, this was one of the most confusing ones so far because I was still confused even after studying other people's answers closely.

## Day 13 - Transparent Origami: [- Problem -](https://adventofcode.com/2021/day/13)
NumPy has some handy functions, i.e. `np.flipud` and `np.fliplr` which both made this one pretty straightforward.

## Day 14 - Extended Polymerization: [- Problem -](https://adventofcode.com/2021/day/14)
Read the problem *carefully*. You don't always need to calculate everything. Sometimes you just need to count!
If you need to look at a pair of adjacent characters in a string, you can use the `zip()` function:
```python
for first, second in zip(template[:-1], template[1:]): #everything except last, everything except first
        pair_counts[''.join((first, second))] += 1 #adds each pair from inital template to dict
```

## Day 15 - Chiton: [- Problem -](https://adventofcode.com/2021/day/15)
Crash course on Dijkstra's Shortest Path algorithm. I had to rely on other people's answers for this puzzle because I simply didn't know how to implement the algorithm. I understand the concepts, but the actual syntax was confusing me.

Also, it's very important when dealing with a grid to make sure you have the correct grid width and height when looking for any neighbors. That threw me off for a long time.

Finally, understanding generators and how they work is going to be important. I *think* I understand it better now, but it's still confusing.

## Day 16: Packet Decoder [- Problem -](https://adventofcode.com/2021/day/16)
Once I figured out *how* to structure the data, this one became a lot of fun. I still didn't come up with the majority of the solution on my own, but that's precisely why I'm doing this - to learn. `dict()` are very useful for organizing stuff like packet header info! One thing I need to study up on is recursion. That still confuses me.

## Day 17: Trick Shot [- Problem -](https://adventofcode.com/2021/day/17)
A really cool problem, but another that I couldn't figure out 100% on my own. I had a lot of the skeleton in place, but there were a couple of smaller things that I didn't know how to do, like setting up the `while x <= x2+1 and y1-1 <= y:` loop. Other than that, this one felt fairly straightfoward.

## Day 18: - Snailfish [- Problem -](https://adventofcode.com/2021/day/18)
I had to concede to this puzzle. I just didn't know how to parse the information into something useful. I didn't know where to begin, or how to go about this puzzle at *all*. The result I put here came from Reddit. Even going through it line by line, I have a hard time understanding what it does. The past few days have been very hard for me because I'm neither familiar enough with commonly known algorithms or data structures, nor knowledgeable enough to apply them. BUT... *I am learning.* - and that was the whole point of this. :)

## Day 19: [- Problem -](https://adventofcode.com/2021/day/19)

## Day 20: [- Problem -](https://adventofcode.com/2021/day/20)

## Day 21: [- Problem -](https://adventofcode.com/2021/day/21)

## Day 22: [- Problem -](https://adventofcode.com/2021/day/22)

## Day 23: [- Problem -](https://adventofcode.com/2021/day/23)

## Day 24: [- Problem -](https://adventofcode.com/2021/day/24)

## Day 25: [- Problem -](https://adventofcode.com/2021/day/25)
