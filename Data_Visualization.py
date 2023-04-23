import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/manta/Downloads/pima-indians-diabetes.csv")

col = ["pregs","plas","pres","skin","test","BMI","pedi","Age","class"]

maxm = []
minm = []
mean = []
median = []
mode = []
sd = []
corrAge = []
corrBMI = []
st = []

#1st part
for i in col:
    mean.append(df[i].mean())
    median.append(df[i].median())
    mode.append(df[i].mode())
    sd.append(df[i].std())
    maxm.append(df[i].max())
    minm.append(df[i].min())
    

#2nd part
for j in ["Age","BMI"]:
    for i in col:
        if(i!= j and i!= "class"):
            plt.scatter(df[j], df[i])
            plt.xlabel(j,size = 16)
            plt.ylabel(i , size = 16)
            plt.title(j+":"+str(i),size = 20)
            plt.show()

#3rd part
for i in col:
    if(i!= "Age" and i!= "class"):
        corrAge.append(df["Age"].corr(df[i]))      
for i in col:
    if(i!= "BMI" and i!= "class"):
        corrBMI.append(df["BMI"].corr(df[i]))

#4th part  
df1 = df["pregs"]
df2 = df["skin"]

df1.plot.hist()
plt.show()
df2.plot.hist()
plt.show()

# 5th part
df3 = df[["pregs","class"]]
qw = df3.groupby("class")

for key, item in qw:
    st.append(qw.get_group(key))
    
cl0 = st[0]
cl1 = st[1]

cl0["pregs"].plot.hist()
plt.title("Class = 0")
plt.show()
cl1["pregs"].plot.hist()
plt.title("Class = 1")
plt.show()

#6th part
for i in col:
    if(i!= "class"):
        df.boxplot(i)
        plt.show()

#Now prinitng all the data in one go...

print("MEAN")
for i in range(8):
    print(str(col[i])+" : "+str(mean[i]))
print("\n\n\n")

print("MEDIAN")
for i in range(8):
    print(str(col[i])+" : "+str(median[i]))
print("\n\n\n")

print("MODE")
for i in range(8):
    print(str(col[i])+" : "+str(list(mode[i])[0]))
print("\n\n\n")

print("STANDARAD DEVIATION")
for i in range(8):
    print(str(col[i])+" : "+str(sd[i]))
print("\n\n\n")

print("MAXIMUM")
for i in range(8):
    print(str(col[i])+" : "+str(maxm[i]))
print("\n\n\n")

print("MINIMUM")
for i in range(8):
    print(str(col[i])+" : "+str(minm[i]))
print("\n\n\n")

print("CORRELATION WRT AGE")
for i in range(7):
    if(col[i]!="Age"):
        print(str(col[i])+" : "+str(corrAge[i]))
print("\n\n\n")

print("CORRELATION WRT BMI")
for i in range(7):
    if(col[i]!="BMI"):
        print(str(col[i])+" : "+str(corrBMI[i]))
print("\n\n\n")
