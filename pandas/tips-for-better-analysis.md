# Binning
Binning is a better way to categorize your numeric data so that model can analyse data easily.  

__bins = numpy.linspace(min(data["Price"]), max(data['Price']), 4)  
group=['Low', 'Medium','High']  
data['Price Binned'] = pandas.cut(data["Price Each"], bins, labels=group_names, include_lowest=True)__ 

# Normalization  
Missing Values can be treated in 3 ways,  
* Feature Scaling F-Fmax  
* Min-Max Normalization  
* Z-score data-avg/Standard Deviation __Best for outliers__.  

# Missing Vals  
* Imputation.  
* Leave them as it is.

# Dummies
* pandas.get_dummies(data['']) method changes the categorical variables to one-hot-encoding.  

# GroupBy  
* Categorical Variables
* Group data into categories
* Single or multiple variables  

# Pivot
* Categorical Variables in columns easy to visualize then GroupBy Method
* Index and Column to pivot in different columns.


