#!/usr/bin/env python
# coding: utf-8

# In[1]:


#fibnocii series


# In[2]:


first_num=0
sec_num=1
print(first_num)
print(sec_num)
for i in range(0,9):
    thi_num=first_num+sec_num
    print(thi_num)
    first_num,sec_num=sec_num,thi_num


# In[3]:


#armstrong number


# In[4]:


n=153
s=n
b=len(str(n))
sm=0
while n!=0:
    r=n%10
    sm=sm+(r**b)
    n=n//10
if s==sm:
    print('it is armstrong number')
else:
    print('it is not armstrong number')


# In[5]:


#multipiclation table


# In[6]:


n=int(input('enter the number'))
for i in range(1,11):
    print(n,'*',i,'=',n*i)


# In[7]:


#factorial


# In[11]:


def fac(n):
    return 1 if (n==1 or n==0) else n*fac(n-1)
fac(5)


# In[12]:


#prime number


# In[14]:


n=int(input('enter the number'))
if n>=1:
    for i in range(2,n):
        if n%i==0:
            
            print('number is not prime')
            break
    else:
        print('number is prime number')
        
else:
    print('number is not prime')


# In[15]:


#ascaii


# In[16]:


c='g'
print('ascaii value of g is',ord(c))


# In[17]:


#sum of square of n natural number


# In[20]:


def son(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i)
    return sm
    
son(4)


# In[21]:


#simple interest


# In[23]:


def si(p,r,t):
    print(p)
    print(r)
    print(t)
    si=p*r*t/100
    return si

si(8,6,8)


# In[24]:


#array


# In[25]:


#sum of array


# In[26]:


a=[1,2,3,4,5,6,7,8,9,10]
def soa(a):
    s=0
    for i in a:
        s=s+i
    return s

soa(a)


# In[27]:


from functools import reduce


# In[28]:


reduce(lambda x,y:x+y,a)


# In[29]:


#rotate element


# In[31]:


a=[1,2,3,4,5]
def rot(a,d,n):
    a[:]=a[d:n]+a[0:d]
    return a

rot(a,2,len(a))


# In[32]:


#monotonic


# In[34]:


def mon(a):
    x,y=[],[]
    x.extend(a)
    y.extend(a)
    x.sort()
    y.sort(reverse=True)
    if (x==a or y==a):
        print('it is monotonic')
    else:
        print('it is not')
        
mon([3,4,5])


# In[35]:


#list


# In[36]:


#swap last element with fisrt in list


# In[37]:


def swap(l):
    l[0],l[-1]=l[-1],l[0]
    return l
l=[2,3,4]
swap(l)


# In[38]:


#reverse list


# In[39]:


def rev(l):
    l[:]=l[::-1]
    return l
l=[1,2,3,4,5]
rev(l)


# In[41]:


#n largest in list
l=[1,2,3,4,5]
def lar(l):
    l.sort()
    return(l[-1])

lar(l)


# In[42]:


reduce(lambda x,y:x if (x>y) else y,l)


# In[43]:


#even number


# In[44]:


def eve(l):
    for i in l:
        if i%2==0:
            print(i)

eve(l)


# In[59]:


#positive no.


# In[60]:


def ch(l):
    for i in l:
        if i>0:
            print(i)
    
ch([-0,-4,-5,3,5,-7,5,-9,3])    


# In[61]:


#remove mepty list from list


# In[66]:


l=[[],9,[],[],6,5,3,[]]
list(filter(lambda x:(x!=[]),l))


# In[67]:


#count occurance of element


# In[68]:


l=[1,2,2,2,3,2,5,6,2,6,8,2,7]
def cou(l,n):
    return l.count(n)

cou(l,2)


# In[69]:


#print duplicates from list


# In[81]:


new=[]
for i in l:
    n=l.count(i)
    if n>1:
        if new.count(i)==0:
            new.append(i)
            print(new)
    


# In[ ]:




