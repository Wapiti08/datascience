import pandas as pd


#读取一个csv文件并可视化的过程
#Read a csv file and visualize the process
housing_dataframe=pd.read_csv("document.path",sep=",",encoding='utf-8')
#Show overall data and framework
print(housing_dataframe.describe())
#Display the first few lines
print(housing_dataframe.head())
#icon display
print(housing_dataframe.hist('column name'))