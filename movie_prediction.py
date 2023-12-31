# -*- coding: utf-8 -*-
"""movie prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CY2__2fB7vVSxE3YXPK3YGkGoC0kqZYW
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""movie data"""

movie=pd.read_csv('/content/movie.csv',sep="::",engine='python')
movie.columns=['movieIDs','MovieName','category']
movie.dropna(inplace=True)
movie.head()

movie.shape

movie.describe()

movie.isna().sum()

"""ratings data

"""

rating=pd.read_csv('/content/ratings.csv',sep="::",engine='python')
rating.columns=['UserId','MovieID','Ratings','TimeStamp']
rating.dropna(inplace=True)
rating.head(10)

rating.shape

rating.describe()

rating.isna().sum()

user=pd.read_csv('/content/users.csv',sep="::",engine='python')
user.columns=['UserId','Gender','Age','Ocuupation','Zip-code']
user.dropna(inplace=True)
user.head(10)

user.shape

user.describe()

user.isna().sum()

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()

user['Gender']=labelencoder.fit_transform(user['Gender'])
user.head()

"""
# concatinating the dataset
"""

data=pd.concat([movie,rating,user],axis=1)
data.dropna()
data.head(10)

data.shape

"""## removing the unnessary columns"""

process=data.drop(["Ocuupation","Zip-code","TimeStamp"],axis=1)
process.head()

process.shape

process.describe()

process.isna().sum()

"""# handling missing values"""

final=process.dropna()

final.shape

final.describe()

"""# visualising the data"""

sns.countplot(x=final['Gender'],hue=final['Ratings'])

final.Age.plot.hist(bins=25)
plt.ylabel("MovieIds")
plt.xlabel("Ratings")

final['Ratings'].value_counts().plot(kind='bar')
plt.show()

sns.countplot(x=final['Age'],hue=final['Ratings'])

"""# final dataset"""

final.head()

input=final.drop(['Ratings','MovieName','category','MovieID'],axis=1)
target=final['Ratings']

target.head()

input.head()

"""# Training the model using Logistic regressions"""

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
scaled_data= scaler.fit_transform(input)
scaled=pd.DataFrame(scaled_data,columns=input.columns)

scaled.head()

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(input,target,test_size=0.3)

print(Y_train)

print(Y_test)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,Y_train)

X_test=np.array(X_test)

"""# prediction"""

model.predict(X_test)

print(Y_test)