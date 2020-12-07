#### Plotting Rules and different graphing references.     
# Box Plot
__Used to understand the range of data which is not a continous values, can be used to understand and spot out different outliers.__   
* Part of SeaBorn
* Not for relationships between graphs.

# Scatter Plots
__Used to find the continous values and their range such as Price.__
* Shows relationship between two variables.  
* Each observation as a point.  
* Target Variable on y-axis.  
* Part of matplotlib. 

# Heatmap
Target variable over multiple variables.  
* Pivoted tables can be applied directly to the Heatmaps.  

# Regression plot on scatter plot
Correlation between two features.
* Shows relation between 2 variables. Related or not
* Straight line zero slope then no relation, excluded from predictions.
* sns.regplot(x,y, data= )

# Residual Plot
Model evaluation using visualization mean to be zero,
* Both variance line to be constant, horizontal.
* sns.residplot(df(x-axis), df(y-axis))

# Distribution Plot
Model evaluation with more independent variables.
* Compare actual values and predicted values
* ax = sns.distplot(df[Actual], hist=False)
* sns.distplot(Pred_out, hist=False)



