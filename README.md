# Pima-Indians-Diabetes-Dataset

Given the Pima Indians Diabetes Database as a csv file. This data-set is originally
from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to
predict based on diagnostic measurements whether a patient has diabetes. Several constraints
were placed on the selection of these instances from a larger database. In particular, all patients
here are females with at least 21 years old of Pima Indian heritage.  

The Data_Visualization code:
* Loads the csv file into the Spyder Enviornment.
* Calculates and print the various statistical features of each attribute like Mean, Median, Mode etc.
* Calculates and print the correlation cofficient between the target attribute and various columns
* Plots the scatter plot between 2 different attributes.


The Data_Preprocessing code:
* Imports PCA from sklearn.
* Loads the csv file into the Spyder Enviornment.
* Normalization and standarization of each and every attribute except the target class.
* Then generates a syntheic data inoder to perform Eigenvalue and EigenVector decomposition.
* Applys PCA on the given Dataset in oder to reduce the dimensions of the data.
* Caluculates and print the covarience matrix after dimensionality reduction.



# Input Dataset

https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

![image](https://user-images.githubusercontent.com/119813195/228885870-124eceb8-0e4d-4381-992f-e567e7ffcfb8.png)


# Output

Statistical Analysis:

![image](https://user-images.githubusercontent.com/119813195/228886486-d491a86d-e2ad-44b8-92cc-7e7956993a94.png)

![image](https://user-images.githubusercontent.com/119813195/228887122-2090b7e2-096a-4c4e-85af-d6b812713b7b.png)

![image](https://user-images.githubusercontent.com/119813195/228887163-7093b32a-0db9-4776-b969-d652ea6be8a4.png)

Normalization and Standarization of each column :

![image](https://user-images.githubusercontent.com/119813195/228903363-8973ceb1-29fe-49df-8a4b-3c8f91ef15e4.png)

![image](https://user-images.githubusercontent.com/119813195/228903765-f0c57206-5122-45aa-9fd2-5bb024b452d8.png)

EigenValue analysis Of the Synetheic Data:

![image](https://user-images.githubusercontent.com/119813195/228904381-b8c3c9f0-ba9d-429c-82e6-375a3c1b0e90.png)

PCA on the main Dataset :

![image](https://user-images.githubusercontent.com/119813195/228904878-2c3b2b03-8870-465d-95a3-f3ce00957e47.png)

![image](https://user-images.githubusercontent.com/119813195/228905068-1dc33a18-6e3f-473e-8ac2-085b34758bdc.png)

![image](https://user-images.githubusercontent.com/119813195/228905270-62cfc94f-c643-4983-b594-95955930a76c.png)

