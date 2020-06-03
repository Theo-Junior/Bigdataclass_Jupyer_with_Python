#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import pandas as pd
import sys

## Initialize Data
student = pd.read_csv("./Data/student.csv")
student.head()


# In[15]:


## Initialize Function
def calculateBMI(a, b):
        return (a/b)


# student.describe()

# In[3]:


## Calculate Bmi && Make 'BMI' Column

student['bmi'] = student['weight'] / ((student['height']/100)*(student['height']/100))


# student['bmi'].head()

# In[33]:


# Divide male, female Column

filter_male = student['sex'] == 'male'
filter_male.head()

filter_female = student['sex'] == 'female'
filter_female.head()


# In[13]:


student_male = student[filter_male]
student_male_bmi = student_male['bmi']

student_female = student[filter_female]
student_female_bmi = student_female['bmi']


# In[11]:


student_male.head()


# In[12]:


student_female.head()


# In[21]:


print("######## Gender Avg. BMI Score #########")
num = int(input("Select what you want to know about which avg. Bmi score Man(1), Women(2), Exit(3) :"))


# student_male['weight'].mean()

# student_male['height'].mean()

# In[32]:


if num == 1:
    print(calculateBMI(student_male_bmi.sum(), len(student_male_bmi)))
elif num == 2:
    print(calculateBMI(student_female_bmi.sum(), len(student_female_bmi)))
else:
    print("End")
    ##sys.exit(1)

