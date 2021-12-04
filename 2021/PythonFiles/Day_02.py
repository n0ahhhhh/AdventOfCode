#!/usr/bin/env python
# coding: utf-8

# In[7]:


#read in data and remove '\n' characters
data = [line.rstrip('\n') for line in open("day_02.txt")]

#splits instructions and appends to form list of lists
course_pair = []
for r in data:
    split = r.split()
    course_pair.append(split)

#creates dataframe from list of lists
directions = pd.DataFrame(course_pair, columns =['Direction', 'Num'])
directions['Num'] = directions['Num'].astype(int)
directions.head()


# In[23]:


#initial variables containing our positions
h_pos = 0
v_pos = 0

#for each row, check direction and +/- 
for index, r in directions.iterrows():    
    if r['Direction'] == 'forward':
        h_pos += r['Num']
    elif r['Direction'] == 'down':
        v_pos += r['Num']
    else:
        v_pos -= r['Num']
        
print("h_pos:", h_pos)
print("v_pos:", v_pos)

#multiply both positions together
p1_ans = h_pos * v_pos
print('The final answer is:', p1_ans)


# In[27]:


#initial variables containing our positions
h_pos_new = 0
v_pos_new = 0
aim = 0

#for each row, check direction and +/- 
for index, r in directions.iterrows():    
    if r['Direction'] == 'forward':
        h_pos_new += r['Num']
        v_pos_new += (r['Num'] * aim)
    elif r['Direction'] == 'down':
        aim += r['Num']
    else:
        aim -= r['Num']
        
print("h_pos:", h_pos_new)
print("v_pos:", v_pos_new)

#multiply both positions together
p2_ans = h_pos_new * v_pos_new
print('The final answer is:', p2_ans)

