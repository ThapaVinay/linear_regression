import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
How to append dataframe into a csv file ->

data = {"Years Of Experience" : [2,4,6,8,1], "Salary" : [60000,100000,150000,200000,100000]}

df = pd.DataFrame(data)
df.to_csv("salary.csv",mode = 'a', index = False, header= False)
'''





data  = pd.read_csv("Employee_Salaries.csv")
print(data)
x = data["Years Of Experience"].values
y = data["Salary"].values
print("Independent Variable : Years of Experience ")
print("Dependent Variable: Salary ")

flag = False
while(True):
    choice = int(input("1. To Train the model \n2. To predict the values \n3. To diplay the graph \n4. Exit ..\n"))

    if(choice == 1):
        flag = True
        x_test = list(x)
        y_test = list(y)
        l = len(data)   # gives the number of rows 
        rand = np.random.choice(range(0,l),size=int(l*2/3),replace = False) # will select 3 elements from the range(0,6) without repeating
        x_train = []
        y_train = []
        
        for i in rand:
            df = data.loc[i]      # it gives us a dataframe 
            x_train.append(df["Years Of Experience"])
            x_test.remove(df["Years Of Experience"])
            y_train.append(df["Salary"])
            y_test.remove(df["Salary"])
        
        # m = $(x - mean_x)(y - mean_y) / $(x-mean_x)^2
        # mean of x and y
        mean_x = np.mean(x)
        mean_y = np.mean(y)

    
        # find the intercept and the slope of the line 
        n1 = 0
        n2 = 0
        for i in range(len(x_train)):
            n1 += ((x[i] - mean_x) * (y[i] - mean_y))
            n2 += (x[i] - mean_x)**2
        m = n1/n2
        
        # y = mx+c
        # mean_y = m(mean_x) + c
        # c = mean_y - m * mean_x
        c = mean_y - (m * mean_x)
        print("Slope : " ,m )
        print( "Intercept : " , c)


        # R sqaured method to find best fit 
        # R^2 = $(y_actutal - y_predicted)^2 / $(y_actual - mean_y)^2
        # r^2 = 1 - RSS/TSS (Residual sum of squares / Total sum of squares)
        num = 0
        den = 0
        for i in range(len(x)):
            y_pred = c + m * x[i]
            num += (y[i] - y_pred) **2
            den += (y[i] - mean_y) **2
        r = 1 - num/den
        print("R squared value ", r)

    elif(choice == 2):
        if(not flag):
            print("Model is not trained yet !")
            continue
        inp = float(input("Enter the experience in years :"))
        print("The expected salary is :", (c + m * inp))

    elif(choice == 3):
        # plotting 
        b = c + m*x
        plt.plot(x,b, color = "red",label = "Regression line")
        plt.scatter(x,y, color = "green", label = "Scatter Plot")
        plt.xlabel("Years Of Experience")
        plt.ylabel("Salary")
        plt.legend()
        plt.show()
        print()
        print()
    
    elif(choice == 4):
        exit(1)
    
    else:
        print("Wrong input .. Try Again ..")








'''

#   USING INBUILD SKLEARN LIBRARY 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
reg = LinearRegression()

# because sklearn does not take 1D array as input, it needs a 2D array
x = x.reshape(-1,1)

reg = reg.fit(x,y)

y_pred = reg.predict(x)  # predicted values for the model 
print(y_pred) 

r2_score =  reg.score(x,y)   # R squared value for the model 
print(r2_score)


print(reg.coef_)  # slope or m
print(reg.intercept_)    # intercept or c


'''
