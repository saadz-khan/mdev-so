# Sci-kit Learn Help
## Pipelines
A best way to perform multiple models sequentially in single method grouped together.  
from sklearn.pipeline import Pipeline
### Normalizating   
from sklearn.preprocessing import StandardScaler
### Polynomial Transformation  
from sklearn.preprocessing import PolynomialFeature  
Fit your inputs and outputs into the correct degree of Polynomial function.  
Your input changes to required input polynomial function of specific degree.
Make object with specific degree.  
Transform the inputs into that degree polynomial.
### Linear Regression  
from sklearn.linear_model import LinearRegression  
i = [('scale', StandardScaler()), ('polynomial',Polynoomial Feature(degree=2), ('mode', LinearRegression())]  
pipe = Pipeline(i) 
### Ridge Regression
Ridge Regression is used for when to errors increase. To reduce standard errors.  
Create Ridge object with specific value for alpha. 
Small alpha overfitting, high value underfitting.

----
* Choose all the degrees of polynomials wisely. Sometimes small degree are better than higher degree. The higher degree may fit the data well but it does not take the shape of the given function.
* Test all types of models. Split your data to test, train and use cross-validation as well.
