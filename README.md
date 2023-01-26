# Gradient-Descent
Gradient Descent is the iterative algorithm that is used by various machine learning algorithms to learn about the data especially the algorithms that applies regression in any form in their core mathematically speaking it uses some cool differential calculus to find the minima of a convex function, while if the function is non-convex, various techniques are applied to find the global minima as in this case it is very likely that the learning stops at any local minima or a saddle point, but those concepts are for later understanding as of now the idea here is to get a basic understanding of how we make machines learn about regression tasks using gradient descent.

![Convex-and-nonconvex-functions-A-function-g-is-a-convex-function-if-domain-of-g-is-a](https://user-images.githubusercontent.com/116963622/214846129-33ac6a05-ae31-4508-86d1-a1c6995aef5c.png)

Basically, the function we take for this is called the cost function, and we try to reduce the cost function by taking partial derivatives of the cost function with respect to each of the independent features in the function, these partial derivatives state the change in the cost function with respect to the change in the respective features after this we deduct these partial derivatives from the respective features but before that the partial derivative is multiplied with a hyperparameter called the learning rate which helps in controlling the rate of the deductions so that it is neither too high nor too low but close enough to converge at the global minima, if the deductions is too high it would miss the global minima while if the deductions is too low it won't converge at the global minima. 

Let's take up linear regression problem for simplicity and understand how it works  

This is the equation of line that we try to fit in a linear regression problem:

![image](https://user-images.githubusercontent.com/116963622/214846595-beff1e26-30a4-45b5-939f-ea4395cd23b8.png)

Here “m” and “b” are the independent variables slope and y-intercept which is used to calculate the predicted values with the correct values of “m” and “b”.

The cost-function in case of Linear regression is mean-squared error :

![1_BtVajQNj29LkVySEWR_4ww](https://user-images.githubusercontent.com/116963622/214847200-57ca516a-7e29-4981-a0bf-bcc6befcda29.png)

Now we substitute the value of “y^i” in the function and the function becomes like this:

![1_gwyZEgUjs6i_yuNa4IQpLw](https://user-images.githubusercontent.com/116963622/214849196-aa43785a-8ea6-46cc-aa09-3ee58acec4ac.png)

Now we take partial derivative w.r.t the independent features that is “m” and “b”, and we get:

![1_nmSmU82ZfqU5p84XwgU_cg](https://user-images.githubusercontent.com/116963622/214851794-dec42ea0-fc93-4f45-8f38-03767c608fab.png)

Now the independent features are updated as: 

m = m – learning rate * d/dm 

b = b – learning rate * d/db 

Until the cost function converges at the global minimum, the corresponding values of “m” and “b” are the correct value that will be used in the equation of the line y = mx + b for making appropriate predictions.
