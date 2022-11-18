data  <- read.csv("D:/linear_regression/salary.csv")
print(data)

x <- data$Years.Of.Experience
y <- data$Salary


relation <- lm(y~x)
print(relation)
a <- data.frame(x = 3)

result <- predict(relation,a)

print(result)

f = c()

for(i in  x)
{
  f <- append(f,predict(relation,data.frame(x = i)))
}

print(length(x))
print(length(f))

plot(x,y,col = "red",main = "Regression line" , xlab = "Years of experienc", ylab = "salary")
par(new = TRUE)
plot(x,f, col = "green", type = 'l')

summary(relation)$r.squared 




