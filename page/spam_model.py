
# coding: utf-8

# In[2]:import numpy as np # linear algebra
import pandas as pd 
import os
df = pd.read_csv(r"static\spam_ham_dataset.csv")
df.head()


# In[3]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df["text"],df["label"], test_size = 0.1, random_state = 10)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
vect.fit(X_train)
X_train_df = vect.transform(X_train)
X_test_df = vect.transform(X_test)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
model = RandomForestClassifier()
model.fit(X_train_df,y_train)

target = model.predict(X_test_df)
accuracy_score(y_test,target)


# In[4]:


from joblib import dump, load
dump(model, 'model.joblib')
dump(vect, 'vector.joblib')


# In[5]:


model = load('model.joblib')
vect = load('vector.joblib')


# In[6]:


def is_spam(inp = ["FREE FREE FREE FREE"]):
    if model.predict(vect.transform(inp))[0] == "spam":
        return "It is a Spam "
    else:
        return "It is a Ham"


# In[8]:


print(is_spam(inp = ["free"]))


# In[9]:


print(is_spam(inp = ["""Congratulations You have won 10000$. FREE FREE FREE .Come and collect.
"""]))

