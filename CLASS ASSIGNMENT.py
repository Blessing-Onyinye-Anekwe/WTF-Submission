#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT

# In[ ]:


# Print all elements of a list using for loop


# In[1]:


fruit_list = ['orange', 'pineapple','cherry','mango']
for i in (fruit_list):
    print(i)


# In[ ]:


# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
# Ask user for their salary and year of service and print the net bonus amount


# In[27]:


salary = int(input('enter salary'))
years = int(input('enter years of service given to the company'))
if(years > 5)
    print("net bonus is",0.05*salary)
    else:
        print('no bonus')


# In[ ]:


#Take input of age of 3 people by user and determine oldest and youngest among them.


# In[6]:


age1 = int(input("Enter age Person 1: "))
age2 = int(input("Enter age Person 2: "))
age3 = int(input("Enter age Person 3: "))
print()
if (age1 > age2) & (age1 > age3):
    print('Person 1 is the oldest')
    if age2 < age3:
        print('Person 2 is the youngest')
    else:
        print('Person 3 is the youngest')
elif (age2 > age1) & (age2 > age3):
    print('Person 2 is the oldest')
    if age1 < age3:
        print('Person 1 is the youngest')
    else:
        print('Person 3 is the youngest')
else:
     print('Person 3 is the oldest')
     if age1 < age2:
         print('Person 1 is the youngest')
     else:
         print('Person 2 is the youngest')


# In[11]:


#Write a Python script to merge two Python dictionaries
my_dict1 = {'ade':1,'don':2,'jane':3,'ken':4}
my_dict2 = {'nkechi':'london','mary':'canada','mike':'astralia'}
my_dict3 = my_dict1.copy()
my_dict3.update(my_dict2)
print (my_dict3)


# In[15]:


#Write a python program to get the largest number from a list
numbers_in_list = [200,500,1000,6000,570,400]
print('Largest element is:', max(numbers_in_list))


# In[20]:


#Write a python program to remove a key from a dictionary
my_items = {'a':1, 'b':2,'c':3,'d':4}
print(my_items)
if 'a' in my_items:
    del my_items ['a']
print(my_items)


# In[ ]:




