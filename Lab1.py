#!/usr/bin/env python
# coding: utf-8

# # Sylabus
# 
# - Podstawowe rozkłady i ich charakterystyki
# - Prawa wielkich liczb.
# - Centralne twierdzenia graniczne.
# - Próby losowe, modele statystyczne.Elementy statystyki opisowej.
# - Funkcje charakterystyczne i funkcje tworzące momenty.
# - Podstawowe statystyki i ich rozkłady.
# - Modele parametryczne i nieparametrczne.Estymatory i ich własności.
# - Estymacja punktowa. Funkcja ryzyka.
# - Estymacja przedziałowa.
# - Asymptotyczne własności estymatorów.
# - Weryfikacja hipotez. Metody konstrukcji testów.
# - Testy parametryczne. Przykłady testów.
# - Testy nieparametrycne. Przykłady testów.
# - Krzywa mocy testu.
# - Testy ilorazu wiarogodności. 
# 
# 
# \begin{aligned}
# \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
# \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
# \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
# \nabla \cdot \vec{\mathbf{B}} & = 0
# \end{aligned}
# 

# In[ ]:


get_ipython().run_cell_magic('latex', '', '\\begin{aligned}\n\\nabla \\times \\vec{\\mathbf{B}} -\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{E}}}{\\partial t} & = \\frac{4\\pi}{c}\\vec{\\mathbf{j}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{E}} & = 4 \\pi \\rho \\\\\n\\nabla \\times \\vec{\\mathbf{E}}\\, +\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{B}}}{\\partial t} & = \\vec{\\mathbf{0}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{B}} & = 0\n\\end{aligned}')


# In[ ]:


# lub
from IPython.display import Latex
Latex(r"""\begin{eqnarray}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0
\end{eqnarray}""")


# In[ ]:


# a może tak
from IPython.display import Math
Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx')


# ## Random Numbers and Monte Carlo Simulation
# 
# Many of the code examples in this book make use of pseudorandom number generation, often
# coupled with the so-called Monte Carlo simulation method for obtaining numerical estimates. 
# Thephrase `Monte Carlo` associated with random number generation comes from the European province
# in Monaco famous for its many casinos. 
# We now overview the core ideas and principles of random number generation and Monte Carlo simulation.
# The main player in this discussion is the `rand()` function. 
# When used without input arguments, rand() generates a “random” number in the interval [0; 1]. Several questions can be asked. How
# is it random? What does random within the interval [0; 1] really mean? How can it be used as an
# aid for statistical and scientific computation? For this we discuss pseudorandom numbers in a bit
# more generality.
# The “random” numbers we generate using Python, as well as most “random” numbers used in any
# other scientific computing platform, are actually pseudorandom. That is, they aren’t really random
# but rather appear random. For their generation, there is some deterministic (non-random and well
# defined) sequence, fxng, specified by 
# $$ x_{n+1} = f(x_n, x_{n-1},\dots)$$
# originating from some specified seed, $x_0$.
# The mathematical function, $f()$ is often (but not always)
# quite a complicated function, designed to yield desirable properties for the sequence fxng that make
# it appear random. Among other properties we wish for the following to hold:
# 
# - Elements $x_i$ and $x_j$ for $i \neq j$ should appear statistically independent. That is, knowing the value of $x_i$ should not yield information about the value of $x_j$ .
# - The distribution of fxng should appear uniform. That is, there shouldn’t be values (or ranges of values) where elements of fxng occur more frequently than others.
# - The range covered by fxng should be well defined.
# - The sequence should repeat itself as rarely as possible.

# In[1]:


from random import random


# In[2]:


random()


# In[3]:


a = random()


# In[4]:


a


# In[5]:


a


# In[6]:


a = "string"


# In[7]:


[random(), random()]


# In[8]:


zm = list(range(10))


# In[9]:


for x in ["abc",'sdasd','sdasdwd']:
    print(x)
    print(x+'sdasda')


# In[10]:


nl = []
for x in zm:
    nl.append(x**2)

nl


# In[11]:


x


# In[12]:


[el for el in zm if el%2==0 ]


# In[14]:


N=10
[random() for _ in range(N)]


# In[ ]:





# In[15]:


[[0.2,0.3],[],[]]


# In[ ]:





# In[16]:


data = [[random(),random()] for _ in range(10)]


# In[17]:


data[4]


# In[18]:


data[1][0]**2+data[1][1]**2


# In[19]:


get_ipython().system('pip3 install numpy')


# In[20]:


import numpy as np
from numpy.linalg import norm


# In[21]:


print(f"wektor {data[0]} , suma kwadratow = {data[0][0]**2+data[0][1]**2}, \n sqrt(sumy kwardratow) = {np.sqrt(data[0][0]**2+data[0][1]**2)}")


# In[22]:


def dlugosc(x):
    return np.sqrt(x[0]**2+x[1]**2) 


# In[23]:


dlugosc(data[1])


# In[24]:


[ dlugosc(x) for x in data ]


# In[25]:


data = [[random(),random()] for _ in range(100000)]


# In[26]:


normy = [norm(x) for x in data]


# In[27]:


normy


# In[28]:


[x for x in normy if x<=1]


# In[37]:


normy = np.array(normy)


# In[38]:


normy


# In[39]:


normy[ normy<=1 ]


# In[40]:


len(normy[normy<=1])


# In[41]:


len(normy)


# In[42]:


PI = 4*(len(normy[normy<=1])/len(normy))


# In[43]:


PI


# ###  Zad 1 ... Wykres PI od N (ilości punktów losowych) 
# 
# 
# ### Zad 2 ... wykres pokazujący, że rand() jest z rozkł jednostajnego
# 
# 

# In[ ]:




