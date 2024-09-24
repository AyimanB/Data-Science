#!/usr/bin/env python
# coding: utf-8

# # Interview QUestions And ANSWER

# In[14]:


# SOLUTION 1
def anagram(s1,s2):
    
    s1=s1.replace(' ',' ').lower()
    s2=s2.replace(' ',' ').lower()
    
    return sorted(s1)==sorted(s2)


# In[2]:


anagram('god','dog')


# In[6]:


anagram('clint eastwood','old west action')


# In[12]:


def anagram2(s1,s2):
    
    s1=s1.replace(' ',' ').lower()
    s2=s2.replace(' ',' ').lower()
    
    return sorted(s1)==sorted(s2)
    if len(s1) !=len(s2):
        return False 
    count={}
    
    for letter in s1:
        if letter in count:
            count[letter]+=1
    else:
        count[letter]=1
        
    for letter in s2:
        if letter in count:
            count[letter]-=1
    else:
        count[letter]=1
        
    for k in count:
        if count[k] != 0:
            return False
        
        return True


# In[13]:


anagram2('clint eastwood','old west action')


# In[25]:


# solution 2

def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # sets for tracking 
    seen =set()
    output = set()
    
    for num in arr:
    
       target = k- num

    if target not in seen:
        seen.add(num)
    else:
        output.add(((min(num,target)),max(num,target)))
    return len(output)


# In[26]:


pair_sum([1,3,2,2],4)


# In[ ]:




