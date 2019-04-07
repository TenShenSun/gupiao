# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import datetime
import os
import pandas_datareader as web
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 11, 20)
#从互联网获取数据
#df = web.DataReader("XOM", "yahoo", start, end)

path=os.path.abspath(os.path.join(os.getcwd(), "../"))+"JDFA.csv"
df = pd.read_csv(path,encoding='utf-8')
#print(df)
#print(df.head())
#取这些列的数据

df = df[['开盘价',  '最高价',  '最低价',  '收盘价', '成交量']]
#print(df)

df['HL_PCT'] = (df['最高价'] - df['最低价']) / df['收盘价'] * 100.0
df['PCT_change'] = (df['收盘价'] - df['开盘价']) / df['开盘价'] * 100.0
df = df[['收盘价', 'HL_PCT', 'PCT_change', '成交量']]
#print(df.head())
print(len(df))


forecast_col = '收盘价'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
#预测forecast_out天后的
print("forecast_out:"+str(forecast_out))

print(len(df[forecast_col]))
df['label'] = df[forecast_col].shift(-forecast_out)
print(df['label'])
# print(df.shape)
# print(df.tail())
X = np.array(df.drop(['label'], 1))


X = preprocessing.scale(X)

X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
# print(X)
# print(X_lately)
y = np.array(df['label'])
#print(y)
# print(X.shape)
# print(y.shape)
X_train, X_test, y_train ,y_test = model_selection.train_test_split(X,y,test_size=0.2)
# LinearRegression 线性回归
clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)
# print("################LinearRegression#################")
# print("精确度：")
# print(accuracy)

forecast_set = clf.predict(X_lately)

print(forecast_set,accuracy,forecast_out)

style.use('ggplot')

df['Forecast']=np.nan

# last_date = df.iloc[-1].name
# last_unix = last_date.timestamp()
# print(last_date,last_unix)
# one_day = 86400
# next_unix = last_unix + one_day

# for i in forecast_set:
#     next_date = datetime.datetime.fromtimestamp(next_unix)
#     next_unix += 86400
#     df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
#
#
# print(df.tail())

df['收盘价'].plot()
df['Forecast'].plot()
plt.show()



"""
svm
for k in ['linear','poly','rbf','sigmoid']:
    clf2 = svm.SVR(k)
    clf2.fit(X_train,y_train)
    accuracy2 = clf2.score(X_test,y_test)    
    print(accuracy2)
"""
"""
clf3 = svm.SVC(kernel='linear',C=1)
scores = cross_val_score(clf3,X,y,cv=5,scoring='f1_macro')
print(scores)
"""