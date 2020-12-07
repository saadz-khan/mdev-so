#### Some Stats cheat sheet/help.  
# Pearson Correlation
Test for two continuous variables.
### Corr Coefficient  
Close to +1 Large Positive relationship  
Close to -1 Large Neg relationship  
Close 0 No Relation  
 
### P value
P < 0.0001 Strong certainty in result  
P < 0.05 Moderate certainty  
P < 0.1 Weak certainty  
P > 0.1 No certainty  

### Python Help
Stats package in python
stats.pearsonr(df[""], df[""])  

# Chi-Square Association Test
__Tests for two categorical variables independence hypothesis testing  
cont_table = pd.crosstab(df[''], df[''])  
scipy.stats.chi2_contingency(cont_table, correction = True)__  
### Chi-Square Stats
### P-Value
###  Degree of Freedom 
(cat1-1)*(cat2-1)  
### Expected Values
