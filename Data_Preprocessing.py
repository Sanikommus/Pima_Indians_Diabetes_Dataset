import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
from scipy import stats

#Q1 a
df = pd.read_csv("C:/Users/manta/Downloads/pima-indians-diabetes.csv")

df1 = df.copy()


col = ["pregs" , "plas" , "pres" , "skin" , "test" , "BMI" , "pedi" , "Age"]

#removing the outliears by  replacing it with the mmedian values of the column
for i in col:
    q1,q2,q3 = df1[i].quantile([0.25 , 0.50 , 0.75])
    IQR = q3 - q1
    df1[i].mask((q1 - 1.5*IQR) > df1[i] , q2 , inplace = True)
    df1[i].mask((q3 + 1.5*IQR) < df1[i] , q2 , inplace = True)
   
df2 = df1.copy()
df3 = df1.copy()

#comparing the max and the min value after Max-Min normalization 
for i in col:
    print(i + " :")
    maxm = df1[i].max()
    minm = df1[i].min()
    df1[i] = (df1[i] - minm)*(7)/(maxm - minm) + 5
    print("Old Minimum is :" + str(minm) + " and Old Maximum is :" + str(maxm))
    new_maxm = df1[i].max()
    new_minm = df1[i].min()
    print("New Minimum is :" + str(new_minm) + " and New Maximum is :" + str(new_maxm))
    print("\n")
    
    
print("\n\n\n")

#Q1 b
#comparing the standarad deviation and the the mean after z standarad normalization
for i in col:
    print(i + " :")
    mean = df2[i].mean()
    stnd = df2[i].std()
    df2[i] = (df2[i] - mean)/stnd
    print("Old Mean is : " + str(mean) + " and Old Standard Deviation is : " + str(stnd))
    new_mean = df2[i].mean()
    new_stnd = df2[i].std()
    print("New Mean is :" + str(new_mean) + " and New Standard Deviation is : " + str(new_stnd))
    print("\n")
    

#Q2 
meanm = [0,0]
cov = [[13,-3] , [-3,5]]

#using this function i am generating a syntheic dataset
data = np.random.multivariate_normal(meanm , cov , 1000)

#seperating both the coloumns into two different list
data0 = [i[0] for i in data]
data1 = [i[1] for i in data]
plt.scatter(data0 , data1 , color = "green" )

#caluculating the eigen values
evalue , evect = np.linalg.eig(cov)

#every column here is a different eigen vector corres
evect1 = [evect[0][0] , evect[1][0]]
evect2 = [evect[0][1] , evect[1][1]]

print(evect1)
print(evect2)

#plotting the eigen vectors onto the scatter plots
plt.quiver( [0,0] , [0,0] , [evect[0][0] , evect[0][1]] , [evect[1][0] , evect[1][1]] , scale = 3 , color = "orange" )
plt.title("Plot of 2D synthetic data and eigen directions")
plt.axis([-20,20,-10,10])
plt.show()

#taking the dot product of the data and eigen values
a = np.dot(data , evect)

for i in range(2):
    b = []
    c = []
    for j in a:
        b.append(evect[0][i]*j[i])
        c.append(evect[1][i]*j[i])
    plt.scatter(data0 , data1 , color = "green" )#plotting the projection along with the scatter plots
    plt.scatter(b, c, color = 'r')
    plt.quiver( [0,0] , [0,0] , [evect[0][0] , evect[0][1]] , [evect[1][0] , evect[1][1]] , scale = 3 , color = "orange" )
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title('Projection of datapoints onto the eigen directions')
    plt.legend(['datapoints', 'eigenvector1',
               'eigenvector2', 'Projection of points'])
    plt.show()
    
#getting the data back from the eigen vectors...
d = decomposition.PCA(n_components=2)
e = d.fit_transform(data)
r = d.inverse_transform(e)

rdata0 = [i[0] for i in r]
rdata1 = [i[1] for i in r]

error = 0

#calculating the error in the original and generated data
for i in range(1000):
    error += ((data0[i] - rdata0[i])**2 + (data1[i] - rdata1[i])**2)**0.5

print("The reconstruction error calculated using eucledian distance is : ", round(error/1000, 3))

#Q3

#a part
#dropped column class and then reduced its dimensionality to 2 from 8
df3 = df3.drop(columns = ["class"])
d = decomposition.PCA(n_components=2)
zdf = stats.zscore(df3)
a = d.fit_transform(zdf)

#calculating the variance and the covariance to get the eign values and vectors
var = d.explained_variance_
print("Variance : " + str(var[0]) + " " + str(var[1]))

cov1 = d.get_covariance()
evalue1 , evect1 = np.linalg.eig(cov1)
print("Eigen Values : " )

for i in evalue1:
    print(i , end =" ")


adata0 = [i[0] for i in a]
adata1 = [i[1] for i in a]

#plotting the data 
plt.scatter(adata0 , adata1)
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Scatter plot of Reduced dimensional data")
plt.show()

print("\n\n")

#b part
#sorting the eigen values and reversing it to get it in descending oder
evalue2 = np.sort(evalue1)[::-1]
for i in evalue2:
    print(i , end =" ")

#now plotting the values on descending oder
l = [1,2,3,4,5,6,7,8]
plt.plot(l , evalue2)
plt.ylabel("Eigen Values")
plt.title("Plot of eigen values in the descening order")
plt.show()
 
#c part
#calculating the error after reducing the dimensionality to 1 , 2 and so on
#and then plotting the error
err = []
for i in range(1, 9):
    pca = decomposition.PCA(n_components=i)
    tra = pca.fit_transform(zdf)
    recons = pca.inverse_transform(tra)
    eucd = np.linalg.norm(zdf - recons)
    err.append(eucd)
plt.plot(l, err)
plt.xlabel("l")
plt.ylabel("Reconstruction error")
plt.title("Plot of reconstruction error VS Number of lower dimensions")
plt.show()

print("\n\n")

#d partcomparing the covariance of the original 8-dimensional matrix and the newly generated 8-dimensional matrix
e = decomposition.PCA(n_components=8)
f = e.fit_transform(zdf)
covar = d.get_covariance()
covar = covar.round(3)
cov1 = cov1.round(3)
print(cov1)
print("\n\n")
print(covar)