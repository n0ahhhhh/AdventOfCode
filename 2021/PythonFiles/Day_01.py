#!/usr/bin/env python
# coding: utf-8

# In[13]:


#read in data and remove '\n' characters
depths = [int(line.rstrip('\n')) for line in open("day_01.txt")]


# In[14]:


#part 1
p1_ans = sum(x < y for x, y in zip(depths, depths[1:]))


# In[15]:


#part 2
p2_ans = sum(x < y for x,y in zip(depths, depths[3:]))


# In[16]:


print("The answer for Part One is:", p1_ans)
print("The answer for Part Two is:", p2_ans)

