import pandas as pd
df = pd.read_csv('data gaji.csv')

a = df.head(10)
print(a)

b = df.tail(10)
print(b)

c = df["gaji"].mean()
print(c)

d = df["tahun_berkerja"].mean()
print (d)

e = df["gaji"].max()
print(e)

f = df["tahun_berkerja"].min()
print(f)