# importing dependencies
import numpy as np
from sklearn.linear_model import LinearRegression


# some random data-1
a=np.array([1,3,5,7,8,10]).reshape(-1,1)
b=np.array([24,28,36,42,49,55]).reshape(-1,1)


# some random data-2
a1=np.array([2,6,7,10,16,11]).reshape(-1,1)
b1=np.array([34,45,49,57,70,53]).reshape(-1,1)


# LinearRegression model from sklearn, applying on random data- 1
model=LinearRegression()
model.fit(a,b)
print('LinearRegression model from sklearn')
print(f'slope: {float(model.coef_)}')
print(f'intercept: {float(model.intercept_)}')


# LinearRegression from scratch with Gradient Descent, applying on random data- 1
def linear_regression(x,y,max_iter,lr):
    n=len(x)
    slope=intercept=0
    learning_rate=lr
    for i in range(max_iter):
        y_hat=slope*x+intercept
        mean_squared_error=(1/n)*sum((y-y_hat)**2)
        slope_derivative=(-2/n)*sum(x*(y-y_hat))
        intercept_derivative=(-2/n)*sum(y-y_hat)
        slope=slope-learning_rate*slope_derivative
        intercept=intercept-learning_rate*intercept_derivative
        print(f'cost:{mean_squared_error}, slope:{slope}, intercept:{intercept}, iteration:{i}')
linear_regression(a,b,max_iter=1000,lr=0.02)


# here we see that the sklearn's linear regression model and our linear regression model
# that we created from scratch using only numpy by applying concept of gradient descent produces almost
# same results, just play around with 'max_iter' and 'lr' parameter to get appropriate results for
# other datasets also such as one another given above and compare it with sklearns model for verification.
