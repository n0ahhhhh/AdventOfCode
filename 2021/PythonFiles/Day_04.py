#!/usr/bin/env python
# coding: utf-8

# In[47]:


#read in data
data = [x for x in open('day_04.txt').read().strip().split('\n')]

#drawn numbers
nums = list(map(int,data[0].split(',')))

#boards
board_r = data[2:]
boards = []
idx = 0

while(idx <= len(board_r) - 5):
    b = []
    for i in range(5):
        b.append([int(s) for s in (board_r[idx].split())])
        idx += 1
    idx += 1 
    boards.append(b)


# In[61]:


drawn = set()
wins = []

for draw in [int(num) for num in nums]:
    drawn.add(draw)
    btr = []
    for i, board in enumerate(boards):
        win = False
        #check horizontal
        for line in board:
            if len([n for n in line if n in drawn]) == 5: #list of drawn #s
                #winner
                win = True
        #check vertical
        for line in zip(*board): #effectively transposes board
            if len([n for n in line if n in drawn]) == 5: #list of drawn #s
                #winner
                win = True
        if win:
            tot = 0
            #calculate score sum(not picked #s) * last drawn number
            for line in board:
                tot += sum([n for n in line if n not in drawn])
            if i not in wins:
                print(f"SCORE {tot * draw}")
                wins.append(i)

