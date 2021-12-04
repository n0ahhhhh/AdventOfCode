#!/usr/bin/env python
# coding: utf-8

# In[1]:


#read in data and remove '\n' characters
data = [line.rstrip('\n') for line in open("day_03.txt")]


# In[2]:


#part 1
#transposes the list of strings, and sums to find how many 1's there are
data_t = [''.join(s) for s in zip(*data)]

gam = []
for r in data_t:
    num_1 = sum(map(int, r))
    if num_1 > len(data)/2:
        gam.append('1')
    else:
        gam.append('0')
#     print(num_1)

#combines list to single string        
gamma_s = ''.join(gam)
epsilon_s = ''.join(['1' if i == '0' else '0' for i in gamma_s])

#converts string to int
gamma = int(gamma_s,2)
epsilon = int(epsilon_s,2)
power = gamma * epsilon

print("The gamma rate is:", gamma)
print("The epsilon rate is:", epsilon)
print("The power consumption is:", power)


# In[3]:


#part 2
columns = [1] * len(data[0])
binary1 = binary2 = pd.read_fwf(data, widths = columns, header = None)
binary1


# In[4]:


#finding the oxygen generator rating
col = 0

while len(binary1) > 1:
    # 1 is most common
    if binary1.sum()[col] >= len(binary1)/2:
        mask = binary1[col] == 1
        binary1 = binary1[mask]
        col += 1
    # 0 is most common
    else:
        mask = binary1[col] == 0
        binary1 = binary1[mask]
        col += 1
        
binary1['ogr'] = binary1[[i for i in range(12)]].astype(str).agg(''.join, axis = 1)
binary1


# In[5]:


#finding the co2 supply rating
col = 0

while len(binary2) > 1:
    # 0 is most common
    if binary2.sum()[col] >= len(binary2)/2:
        mask = binary2[col] == 0
        binary2 = binary2[mask]
        col += 1
    # 1 is most common
    else:
        mask = binary2[col] == 1
        binary2 = binary2[mask]
        col += 1
        
binary2['csr'] = binary2[[i for i in range(12)]].astype(str).agg(''.join, axis = 1)
binary2


# In[6]:


ogr = int(binary1.iloc[0]['ogr'], 2)
csr = int(binary2.iloc[0]['csr'], 2)

print("The Oxygen Generator Rating is:", ogr)
print("The CO2 Scrubber Rating is:", csr)
print("The Life Support Rating is:", ogr * csr)

