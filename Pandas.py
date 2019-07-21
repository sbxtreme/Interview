#read csv from a URL
df=pd.read_csv('http://bit.ly/uforeports')

# check the type of frame ( series or dataframe )
type(df)

# gives last 5 recrds from dataframe
df.tail()

# checks for type of frame (series or dataframe)
type(df['City'])

# access series from dataframe
(df.City)

# add 2 series and assign to a new column of dataframe
df['location']=df.City+':'+df.State 

# creating dataframes using pandas dictionaries 
df=pd.DataFrame({'name':['shobhit','amit','joh'],'Designation':['SAP','SAP','BA']},columns=['Designation','name'],index=['a','b','c'])
# here columns are for sorting values based on columns and index is the index value of dataframe which needs to be set.

# creating dataframe using list of lists 
df= pd.DataFrame([['shobhit','SAP'],['bob','SA'],['priyanka','BA']],columns=['name','des'],index=['a','b','c'])
# here we have explicitly gave names to columns as the list of list value just treated as a row and no colunn header.

# creating dataframes using numpy arrays:
import numpy as np
import pandas as pd
arr=np.random.rand(5,3)
pd.DataFrame(arr,columns=['Randomval1','Randomval2','Randomval3'],index=['a','b','c','d','e'])

# creating dataframe using np.arange function:
pd.DataFrame({'student_id':np.arange(100,110,1),'marks':np.random.randint(50,60,10)})

# set a column as an index :
pd.DataFrame({'student_id':np.arange(100,110,1),'marks':np.random.randint(50,60,10)}).set_index('student_id')

# concatenate series and dataframe concat function:
s=pd.Series(['1','2','4'],index =['a','b','c'],name='series')
df=pd.DataFrame({'name':['shobhit','priyanka','heena'],'des':['SAP','SAP','BA']},index=['a','b','c'])
pd.concat([s,df],axis=1) # axis 1 means concatenated vertically and 0 means concatenated horizontally

# str method in dataframe:
order = pd.read_csv('http://bit.ly/chiporders',sep='\t')
order.item_name.str.upper()
order[order.item_name.str.contains('Chicken')] # get the data which contains Chicken in item_name column
# changing the value of choice_description by replacing [] in the data and store the latest data in choice_description column
order.choice_description=order.choice_description.str.replace('[','').str.replace(']','') 

# Loc and iloc
ufo=pd.read_csv('http://bit.ly/uforeports')
# loc method takes 2 arguments (rows,columns) ; to see all rows use : and to see rows from 0 to 2 use 0:2, same with columns
ufo.loc[0:2,:]
# this is different from loc in the sense that it will give 0th  and 1st index rows and will not give 2nd index rows 
# whereas loc gives 0,1,2 index rows
ufo.iloc[0:2,:]
# the below will give all the rows with city and state columns
ufo.loc[:,['City','State']]
# getting data based on certain condition (want rows where state ='NY' and selected columns should be City and Shape_reported)
ufo.loc[ufo.State=='NY',['City','Shape Reported']]

# Drop a column from dataframe 
ufo.drop(['Time'],axis=1)

#Aggrigate functions in pandas
drinks.beer_servings.mean() # calculate mean of beer_servings

#Groupby in pandas
drinks.groupby('continent').beer_servings.count()
drinks.groupby('continent').beer_servings.agg(['max','min','mean','std','count'])
# we can plot graph in ipython notebook using the below 
%matplotlib inline
drinks.groupby('continent').beer_servings.agg(['max','min','mean','std','count']).plot(kind='bar')

#Settingwithcopy warning

'''when ever we try to assign a value to a column of dataframe without using loc operation then it throws warning
Settingwithcopywarning, which means pandas not sure whether the changes which we are doing is on actual dataframe 
or copy of dataframe and since it's a warning but still the values will not be changed,
so to avoid this we use loc operation to change a value of a column'''

movies[movies.content_ratings=='NOT RATED'].content_ratings==np.nan # this is wrong
movies.loc[movies.content_ratings=='NOT RATED','content_ratings']=np.nan

'''Also if we create a copy of dataframe and then try to change the value , then also the same warning is received.
But this time the value is changed.To avoid this we should use .copy() function to copy dataframe'''

new_df = movies[movies.movie_ratings>=9].copy() # this is right
