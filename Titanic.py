import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing,cross_validation
#importing datd
train=pd.read_csv('C:/Users/XOR/Desktop/ML-master/problems/titanic/train.csv')
test=pd.read_csv('C:/Users/XOR/Desktop/ML-master/problems/titanic/test.csv')
print(train.isnull().sum())
print(len(train))
#ax=test["Age"].hist(bins=20)
#ax.set(xlabel='Age',ylabel='count')
#sns.countplot(x='Age',data=train)
#plt.show()
print('Mean Age:',train['Age'].mean(skipna=True))
print('Median Age:',train['Age'].median(skipna=True))
#removing the unnecessary attributes from training and testing dataset
#rain.drop('PassengerId',axis=1,inplace=True)
train.drop('Cabin',axis=1,inplace=True)
train.drop('Name',axis=1,inplace=True)
train.drop('Ticket',axis=1,inplace=True)
#test.drop('PassengerId',axis=1,inplace=True)
test.drop('Cabin',axis=1,inplace=True)
test.drop('Name',axis=1,inplace=True)
test.drop('Ticket',axis=1,inplace=True)
#this line will fill all the empty values
train['Age'].fillna(28,inplace=True)
#to check wheather the empty values are filled or not
#sns.countplot(x='Age',data=train)
#plt.show()
print(train.isnull().sum())
train['Embarked'].fillna('S',inplace=True)
test['Embarked'].fillna('S',inplace=True)
test['Age'].fillna(28,inplace=True)
#print(train.Pclass)
train2=pd.get_dummies(train,columns=["Pclass"])
train3=pd.get_dummies(train2,columns=["Sex"])
train4=pd.get_dummies(train3,columns=["Embarked"])
test2=pd.get_dummies(test,columns=["Pclass"])
test3=pd.get_dummies(test2,columns=["Sex"])
test4=pd.get_dummies(test3,columns=["Embarked"])
cols=["Age","SibSp","Parch","Pclass_1","Pclass_2","Embarked_C","Embarked_S","Sex_female"]
x=train4[cols]
y=train4["Survived"]
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
print(lr.score(x_test,y_test))
x2=test4[cols]
y2=lr.predict(x2)
y2=y2.reshape(418,1)
d=pd.DataFrame(data=y2[:,0],columns=["Survived"])
