# All the data is present in the below location:
# https://github.com/justmarkham/pandas-videos/tree/master/data
# Either download else use the below url to access the data 
# http://bit.ly/<datasetfilename>

#read csv from a URL
df=pd.read_csv('http://bit.ly/uforeports')

# check the type of frame ( series or dataframe )
type(df)

# information about dataframe
drinks.info()

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
df= pd.DataFrame([['shobhit','SAP'],['bob','SA'],['han','BA']],columns=['name','des'],index=['a','b','c'])
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
'''concatination can be done horizontally and vertically. This is done using the index columns.'''
s=pd.Series(['1','2','4'],index =['a','b','c'],name='series')
df=pd.DataFrame({'name':['shobhit','tom','han'],'des':['SAP','SAP','BA']},index=['a','b','c'])
pd.concat([s,df],axis=1,ignore_index=True) # axis 1 means concatenated vertically and 0 means concatenated horizontally

pd.concat([s,df],ignore_index=True) # concatinated horizontally i.e rows will be added.

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

# Sort data in pandas dataframe ( both works )
movies.star_rating.sort_values(ascending=False)
movies.sort_values('genre',ascending=False)
movies.sort_values(['genre','star_ratings'])

# Duplicate values of a column in pandas & duplicate rows in pandas
movies.star_rating.duplicated().sum()
movies.duplicated().sum()
# All the rows which has duplicate values on column star_rating
movies.loc[movies.star_rating.duplicated(),:]
# Find duplicates based on the combination of columns
movies.duplicated(subset =['star_rating','genre']).sum()


# Drop duplicates
star_ratings.drop_duplicates(keep='first') # keep first row and drops all
star_ratings.drop_duplicates(keep='last') # keep last row and drops all 
star_ratings.drop_duplicates(keep=False)  # drops all the rows 



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

# how to find the count of data with null values
movies.content_ratings.isnull().sum()

# To set column as an index in dataframe
drinks.set_index('country',inplace=True)

# To give name to an index
drinks.index.name='CON'

# To reset the index
drinks.reset_index(inplace=True)

# Rename a column in dataframe
drinks.rename(index=str,columns={"CON":"Country"},inplace=True)

# to get all the aggrigate function
drinks.describe()

# to get all the arrigate function for a column
drinks.describe().loc[:,'beer_servings']

# to convert a time column into pandas datetime format
ufo['Time']= pd.to_datetime(ufo.Time)
ufo.Time.dt.hour
ufo.Time.dt.weekday
ufo.Time.dt.weekday_name

# to get count,unique,top,freq of a column
df.genre.describe()

# to get count of each types of genre
df.genre.value_counts()

o/p:
----
Drama        278
Comedy       156
Action       136
Crime        124
Biography     77
Adventure     75
Animation     62
Horror        29
Mystery       16

# to get the distinct value of a column
df.genre.unique()

# to get the count of unique values of a column
df.genre.nunique()

# drop the nan values
df.dropna(how='any') # if any of the rows has any value as NaN then drop the complete row
df.dropna(how='all') # if all the values in a rows is NaN then drop the that row.

# filter data based on column values in pandas
movies[movies.star_rating>9]

# drop columns ( here axis =1 means dropping columns )
ufo.drop(['City','State'],inplace=True,axis =1)
# drop rows
ufo.drop([0,2],inplace=True,axis=0) # here [0,2] is index or labels of dataframe

# how to fill NaN values:
ufo['Colors Reported'].fillna('NULL VALUE',inplace=True)

# rename columns:
ufo.rename(columns={'Colors Reported':'Colors_reported','Shape Reported':'Shape_reported'},inplace=True)
# we can also use replace functionality to remove spaces from column names
ufo.columns=ufo.columns.str.replace('','_')

# Speed up pandas
# 1) memory usage 
drinks.info(memory_usage='deep')

# 2) to make pandas faster: 
'''convert a column as category datatype , this will just store the numbers 
in the column which will point the lookup table. This way the unique value of a columns  will be stored in 
a lookup table with it's serial numbers and those series numbers will be used in dataframes
NOTE:
-----
We should only convert the data type of columns to categories which has less number of unique values else
the effect would be reverse i.e dataframe size will increase '''
drinks.continent=drinks.continent.astype('category') 
drinks.info(memory_usage='deep')

# Add a new row in the bottom of data frame:
df.loc[df.index.max()+1]=['xx',12,10]

# merging data frames:


# Join data frames:




