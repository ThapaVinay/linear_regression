
data  <- read.csv("D:/linear_regression/Employee_Salaries.csv")
print(data)

x <- data$Years.Of.Experience
y <- data$Salary

print("Independent Variable : Years of Experience ")
print("Dependent Variable: Salary ")

flag <- 0
while(1)
{
  choice <- readline(prompt = "1. To Train the model \n2. To predict the values \n3. To diplay the graph \n4. Exit ..\n")
  if(choice == 1)
  {
    flag = 1
    x_test <- c(x)
    y_test <- c(y)
    l = length(data$Years.Of.Experience)   # gives the number of rows 
    rand = sample(l,as.numeric((l*2/3)),replace = FALSE) # will select l elements from the range(0,6) without repeating
    x_train <- c()
    y_train <- c()
    x_test <- x_test[-rand]
    y_test <- y_test[-rand]
    for (i in rand)
    {
      df <- data[i,]      # it gives us a data frame 
      x_train <- append(x_train,df$Years.Of.Experience)
      y_train <- append(y_train,df$Salary)
    }
    
    # m = $(x - mean_x)(y - mean_y) / $(x-mean_x)^2
    
    mean_x <- mean(x_train)
    mean_y <- mean(y_train)
    
    n1 <- 0
    n2 <- 0
    
    for(i in 1 : length(x_train))
    {
      n1 <- n1 + ((x_train[i] - mean_x) * (y_train[i] - mean_y))
      n2 <- n2 + (x_train[i] - mean_x)**2
    }
    m <- n1/n2
    
    # y = mx+c
    # mean_y = m(mean_x) + c
    # c = mean_y - m * mean_x
    c = mean_y - (m * mean_x)
    cat("Slope : ",m ,"\n")
    cat("Intercept : " , c ,"\n")
    
    
    # R squared method to find best fit 
    # R^2 = $(y_actual - y_predicted)^2 / $(y_actual - mean_y)^2
    # r^2 = 1 - RSS/TSS (Residual sum of squares / Total sum of squares)
    num <- 0
    den <- 0
    for (i in 1 : length(x_test))
    {
      y_pred <- c + m * x_test[i]
      num <- num + (y_test[i] - y_pred) **2
      den <- den + (y_test[i] - mean_y) **2
    }
      
    r <- (1 - num/den)
    cat("R squared value : ", r, "\n\n\n")

  }
  
  else if(choice == 2)
  {
    if(flag == 0)
    {
      print("Model is not trained yet !")
      continue
    }
    inp <- readline(prompt = "Enter the experience in years :")
    inp <- as.double(inp)
    print(paste("The expected salary is :", (c + m * inp)))
  }
    
  else if(choice == 3)
  {
    # plotting 
    b = c + m*x
    plot(x,y, col = "green",main = "Regression line", xlab="Years of Experience", ylab="Salary", pch = 20)
    points(x,b, col = "red", type = 'l', lwd=2)
    
  }
  else if(choice == 4)
  {
    return(1)
  }
  else
  {
    print("Wrong input .. Try Again ..")
  }
    
}







