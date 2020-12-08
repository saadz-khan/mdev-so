# Sci-kit Learn Help
## Pipelines
A best way to perform multiple models sequentially in single method grouped together.  
from sklearn.pipeline import Pipeline
* Normalizating   
from sklearn.preprocessing import StandardScaler
* Polynomial Transformation  
from sklearn.preprocessing import PolynomialFeature
* Linear Regression  
from sklearn.linear_model import LinearRegression  
i = [('scale', StandardScaler()), ('polynomial',Polynoomial Feature(degree=2), ('mode', LinearRegression())]  
pipe = Pipeline(i)  
