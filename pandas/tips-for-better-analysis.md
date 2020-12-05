Binning is a better way to categorize your numeric data so that model can analyse data easily.  

bins = numpy.linspace(min(data["Price"]), max(data['Price']), 4)  
group=['Low', 'Medium','High']  
data['Price Binned'] = pandas.cut(data["Price Each"], bins, labels=group_names, include_lowest=True)  
