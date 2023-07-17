#!/usr/bin/env python
# coding: utf-8

# In[3]:


# this is armstrong number programme
num=int(input("enter the number::"))
sum=0
order=len(str(num))
num2=num
while(num>0):
    digit=num%10
    sum=sum+(digit**order)
    num=num//10
print("the sum of this number::",sum)    
if(num2==sum):
    print("This is armstrong number")
else:
    print("This is not armstrong number")


# In[11]:


#fibonannci series number 0,1,1,2,3,5,8
num=int(input("Enter the number::"))
a=0
b=1
c=0
for i in range(0,num+1):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    


# In[24]:


#perfect number or not perfect number
num=int(input("enter the number::"))
total=0
for i in range(1,num):
    if(num%i==0):
        total=total+i
        
        
if(total==num):
    print("This is perfect number")
else:
    print("This is not perfect number")


# In[35]:


# prime or not prime
num=int(input("Enter the number"))
count=0
for i in range(1,num+1):
    if(num%i==0):
    
        count=count+1
        print(i)
print(count,"number can divide number ",num)
if(count==2):
    print("This is prime number")
else:
    print("This is not prime number")


# In[64]:


# 1
# 12
# 123
# 1234
# 12345
#     1
#    21
#   321
#  4321
# 54321
n=6
for i in range(1,n):
    for j in range(1,n-1):
        print(" ")
           for j in range(1,i):
        print(i,end="")  
   
        
        
    print()        

