import requests as rs
import csv
import pandas as pd


csv_url="https://docs.google.com/spreadsheets/u/1/d/14KHVWNqqy4_cF4qU0eHsZpSDtn2Ap0AdXXjg2S5QzhI/export?format=csv&id=14KHVWNqqy4_cF4qU0eHsZpSDtn2Ap0AdXXjg2S5QzhI&gid=0"
res=rs.get(url=csv_url)
open('google.csv', 'wb').write(res.content)


df = pd.read_csv("google.csv")

matrix2 = df[df.columns[0]].as_matrix()
list2 = matrix2.tolist()

print(list2)