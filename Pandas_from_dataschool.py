#!/usr/bin/env python
# coding: utf-8

# In[2]:


# conventional way to import pandas
import pandas as pd


# In[2]:


# read a dataset of Chipotle orders directly from a URL and store the results in a DataFrame
orders = pd.read_table('http://bit.ly/chiporders')


# In[3]:


# examine the first 5 rows
orders.head()


# Documentation for [**`read_table`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_table.html)

# In[2]:


import pandas as pd
# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)


# In[5]:


# examine the first 5 rows
users.head()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 3. How do I select a pandas Series from a DataFrame? ([video](https://www.youtube.com/watch?v=zxqjeyKP2Tk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=3))

# In[6]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_table('http://bit.ly/uforeports', sep=',')


# In[7]:


# read_csv is equivalent to read_table, except it assumes a comma separator
ufo = pd.read_csv('http://bit.ly/uforeports')


# In[8]:


# examine the first 5 rows
ufo.head()


# In[9]:


# select the 'City' Series using bracket notation
ufo['City']

# or equivalently, use dot notation
ufo.City


# **Bracket notation** will always work, whereas **dot notation** has limitations:
# 
# - Dot notation doesn't work if there are **spaces** in the Series name
# - Dot notation doesn't work if the Series has the same name as a **DataFrame method or attribute** (like 'head' or 'shape')
# - Dot notation can't be used to define the name of a **new Series** (see below)

# In[10]:


# create a new 'Location' Series (must use bracket notation to define the Series name)
ufo['Location'] = ufo.City + ', ' + ufo.State
ufo.head()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 4. Why do some pandas commands end with parentheses (and others don't)? ([video](https://www.youtube.com/watch?v=hSrDViyKWVk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=4))

# In[11]:


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')


# **Methods** end with parentheses, while **attributes** don't:

# In[12]:


# example method: show the first 5 rows
movies.head()


# In[13]:


# example method: calculate summary statistics
movies.describe()


# In[14]:


# example attribute: number of rows and columns
movies.shape


# In[15]:


# example attribute: data type of each column
movies.dtypes


# In[16]:


# use an optional parameter to the describe method to summarize only 'object' columns
movies.describe(include=['object'])


# Documentation for [**`describe`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 5. How do I rename columns in a pandas DataFrame? ([video](https://www.youtube.com/watch?v=0uBirYFhizE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=5))

# In[17]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')


# In[18]:


# examine the column names
ufo.columns


# In[19]:


# rename two of the columns by using the 'rename' method
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
ufo.columns


# Documentation for [**`rename`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)

# In[20]:


# replace all of the column names by overwriting the 'columns' attribute
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
ufo.columns


# In[21]:


# replace the column names during the file reading process by using the 'names' parameter
ufo = pd.read_csv('http://bit.ly/uforeports', header=0, names=ufo_cols)
ufo.columns


# Documentation for [**`read_csv`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)

# In[22]:


# replace all spaces with underscores in the column names by using the 'str.replace' method
ufo.columns = ufo.columns.str.replace(' ', '_')
ufo.columns


# Documentation for [**`str.replace`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.replace.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 6. How do I remove columns from a pandas DataFrame? ([video](https://www.youtube.com/watch?v=gnUKkS964WQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=6))

# In[23]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()


# In[24]:


# remove a single column (axis=1 refers to columns)
ufo.drop('Colors Reported', axis=1, inplace=True)
ufo.head()


# Documentation for [**`drop`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html)

# In[25]:


# remove multiple columns at once
ufo.drop(['City', 'State'], axis=1, inplace=True)
ufo.head()


# In[26]:


# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)
ufo.head()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 7. How do I sort a pandas DataFrame or a Series? ([video](https://www.youtube.com/watch?v=zY4doF6xSxY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=7))

# In[27]:


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# **Note:** None of the sorting methods below affect the underlying data. (In other words, the sorting is temporary).

# In[28]:


# sort the 'title' Series in ascending order (returns a Series)
movies.title.sort_values().head()


# In[29]:


# sort in descending order instead
movies.title.sort_values(ascending=False).head()


# Documentation for [**`sort_values`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sort_values.html) for a **Series**. (Prior to version 0.17, use [**`order`**](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.order.html) instead.)

# In[30]:


# sort the entire DataFrame by the 'title' Series (returns a DataFrame)
movies.sort_values('title').head()


# In[31]:


# sort in descending order instead
movies.sort_values('title', ascending=False).head()


# Documentation for [**`sort_values`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html) for a **DataFrame**. (Prior to version 0.17, use [**`sort`**](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sort.html) instead.)

# In[32]:


# sort the DataFrame first by 'content_rating', then by 'duration'
movies.sort_values(['content_rating', 'duration']).head()


# [Summary of changes to the sorting API](http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#changes-to-sorting-api) in pandas 0.17
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 8. How do I filter rows of a pandas DataFrame by column value? ([video](https://www.youtube.com/watch?v=2AFGPdNn4FM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=8))

# In[33]:


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[34]:


# examine the number of rows and columns
movies.shape


# **Goal:** Filter the DataFrame rows to only show movies with a 'duration' of at least 200 minutes.

# In[35]:


# create a list in which each element refers to a DataFrame row: True if the row satisfies the condition, False otherwise
booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)


# In[36]:


# confirm that the list has the same length as the DataFrame
len(booleans)


# In[37]:


# examine the first five list elements
booleans[0:5]


# In[38]:


# convert the list to a Series
is_long = pd.Series(booleans)
is_long.head()


# In[39]:


# use bracket notation with the boolean Series to tell the DataFrame which rows to display
movies[is_long]


# In[40]:


# simplify the steps above: no need to write a for loop to create 'is_long' since pandas will broadcast the comparison
is_long = movies.duration >= 200
movies[is_long]

# or equivalently, write it in one line (no need to create the 'is_long' object)
movies[movies.duration >= 200]


# In[41]:


# select the 'genre' Series from the filtered DataFrame
movies[movies.duration >= 200].genre

# or equivalently, use the 'loc' method
movies.loc[movies.duration >= 200, 'genre']


# Documentation for [**`loc`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 9. How do I apply multiple filter criteria to a pandas DataFrame? ([video](https://www.youtube.com/watch?v=YPItfQ87qjM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=9))

# In[42]:


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[43]:


# filter the DataFrame to only show movies with a 'duration' of at least 200 minutes
movies[movies.duration >= 200]


# Understanding **logical operators:**
# 
# - **`and`**: True only if **both sides** of the operator are True
# - **`or`**: True if **either side** of the operator is True

# In[44]:


# demonstration of the 'and' operator
print(True and True)
print(True and False)
print(False and False)


# In[45]:


# demonstration of the 'or' operator
print(True or True)
print(True or False)
print(False or False)


# Rules for specifying **multiple filter criteria** in pandas:
# 
# - use **`&`** instead of **`and`**
# - use **`|`** instead of **`or`**
# - add **parentheses** around each condition to specify evaluation order

# **Goal:** Further filter the DataFrame of long movies (duration >= 200) to only show movies which also have a 'genre' of 'Drama'

# In[46]:


# CORRECT: use the '&' operator to specify that both conditions are required
movies[(movies.duration >=200) & (movies.genre == 'Drama')]


# In[47]:


# INCORRECT: using the '|' operator would have shown movies that are either long or dramas (or both)
movies[(movies.duration >=200) | (movies.genre == 'Drama')].head()


# **Goal:** Filter the original DataFrame to show movies with a 'genre' of 'Crime' or 'Drama' or 'Action'

# In[48]:


# use the '|' operator to specify that a row can match any of the three criteria
movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')].head(10)

# or equivalently, use the 'isin' method
movies[movies.genre.isin(['Crime', 'Drama', 'Action'])].head(10)


# Documentation for [**`isin`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.isin.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 10. Your pandas questions answered! ([video](https://www.youtube.com/watch?v=B-r9VuK80dk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=10))

# **Question:** When reading from a file, how do I read in only a subset of the columns?

# In[49]:


# read a dataset of UFO reports into a DataFrame, and check the columns
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.columns


# In[50]:


# specify which columns to include by name
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=['City', 'State'])

# or equivalently, specify columns by position
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=[0, 4])
ufo.columns


# **Question:** When reading from a file, how do I read in only a subset of the rows?

# In[51]:


# specify how many rows to read
ufo = pd.read_csv('http://bit.ly/uforeports', nrows=3)
ufo


# Documentation for [**`read_csv`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)

# **Question:** How do I iterate through a Series?

# In[52]:


# Series are directly iterable (like a list)
for c in ufo.City:
    print(c)


# **Question:** How do I iterate through a DataFrame?

# In[53]:


# various methods are available to iterate through a DataFrame
for index, row in ufo.iterrows():
    print(index, row.City, row.State)


# Documentation for [**`iterrows`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iterrows.html)

# **Question:** How do I drop all non-numeric columns from a DataFrame?

# In[54]:


# read a dataset of alcohol consumption into a DataFrame, and check the data types
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.dtypes


# In[55]:


# only include numeric columns in the DataFrame
import numpy as np
drinks.select_dtypes(include=[np.number]).dtypes


# Documentation for [**`select_dtypes`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.select_dtypes.html)

# **Question:** How do I know whether I should pass an argument as a string or a list?

# In[56]:


# describe all of the numeric columns
drinks.describe()


# In[57]:


# pass the string 'all' to describe all columns
drinks.describe(include='all')


# In[58]:


# pass a list of data types to only describe certain types
drinks.describe(include=['object', 'float64'])


# In[59]:


# pass a list even if you only want to describe a single data type
drinks.describe(include=['object'])


# Documentation for [**`describe`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 11. How do I use the "axis" parameter in pandas? ([video](https://www.youtube.com/watch?v=PtO3t6ynH-8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=11))

# In[60]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[61]:


# drop a column (temporarily)
drinks.drop('continent', axis=1).head()


# Documentation for [**`drop`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html)

# In[62]:


# drop a row (temporarily)
drinks.drop(2, axis=0).head()


# When **referring to rows or columns** with the axis parameter:
# 
# - **axis 0** refers to rows
# - **axis 1** refers to columns

# In[63]:


# calculate the mean of each numeric column
drinks.mean()

# or equivalently, specify the axis explicitly
drinks.mean(axis=0)


# Documentation for [**`mean`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.mean.html)

# In[64]:


# calculate the mean of each row
drinks.mean(axis=1).head()


# When performing a **mathematical operation** with the axis parameter:
# 
# - **axis 0** means the operation should "move down" the row axis
# - **axis 1** means the operation should "move across" the column axis

# In[65]:


# 'index' is an alias for axis 0
drinks.mean(axis='index')


# In[66]:


# 'columns' is an alias for axis 1
drinks.mean(axis='columns').head()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 12. How do I use string methods in pandas? ([video](https://www.youtube.com/watch?v=bofaC0IckHo&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=12))

# In[67]:


# read a dataset of Chipotle orders into a DataFrame
orders = pd.read_table('http://bit.ly/chiporders')
orders.head()


# In[68]:


# normal way to access string methods in Python
'hello'.upper()


# In[69]:


# string methods for pandas Series are accessed via 'str'
orders.item_name.str.upper().head()


# In[70]:


# string method 'contains' checks for a substring and returns a boolean Series
orders.item_name.str.contains('Chicken').head()


# In[71]:


# use the boolean Series to filter the DataFrame
orders[orders.item_name.str.contains('Chicken')].head()


# In[72]:


# string methods can be chained together
orders.choice_description.str.replace('[', '').str.replace(']', '').head()


# In[73]:


# many pandas string methods support regular expressions (regex)
orders.choice_description.str.replace('[\[\]]', '').head()


# [String handling section](http://pandas.pydata.org/pandas-docs/stable/api.html#string-handling) of the pandas API reference
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 13. How do I change the data type of a pandas Series? ([video](https://www.youtube.com/watch?v=V0AWyzVMf54&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=13))

# In[74]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[75]:


# examine the data type of each Series
drinks.dtypes


# In[76]:


# change the data type of an existing Series
drinks['beer_servings'] = drinks.beer_servings.astype(float)
drinks.dtypes


# Documentation for [**`astype`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.astype.html)

# In[77]:


# alternatively, change the data type of a Series while reading in a file
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
drinks.dtypes


# In[78]:


# read a dataset of Chipotle orders into a DataFrame
orders = pd.read_table('http://bit.ly/chiporders')
orders.head()


# In[79]:


# examine the data type of each Series
orders.dtypes


# In[80]:


# convert a string to a number in order to do math
orders.item_price.str.replace('$', '').astype(float).mean()


# In[81]:


# string method 'contains' checks for a substring and returns a boolean Series
orders.item_name.str.contains('Chicken').head()


# In[82]:


# convert a boolean Series to an integer (False = 0, True = 1)
orders.item_name.str.contains('Chicken').astype(int).head()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 14. When should I use a "groupby" in pandas? ([video](https://www.youtube.com/watch?v=qy0fDqoMJx8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=14))

# In[83]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[84]:


# calculate the mean beer servings across the entire dataset
drinks.beer_servings.mean()


# In[85]:


# calculate the mean beer servings just for countries in Africa
drinks[drinks.continent=='Africa'].beer_servings.mean()


# In[86]:


# calculate the mean beer servings for each continent
drinks.groupby('continent').beer_servings.mean()


# Documentation for [**`groupby`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html)

# In[87]:


# other aggregation functions (such as 'max') can also be used with groupby
drinks.groupby('continent').beer_servings.max()


# In[88]:


# multiple aggregation functions can be applied simultaneously
drinks.groupby('continent').beer_servings.agg(['count', 'mean', 'min', 'max'])


# Documentation for [**`agg`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.groupby.DataFrameGroupBy.agg.html)

# In[89]:


# specifying a column to which the aggregation function should be applied is not required
drinks.groupby('continent').mean()


# In[90]:


# allow plots to appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[91]:


# side-by-side bar plot of the DataFrame directly above
drinks.groupby('continent').mean().plot(kind='bar')


# Documentation for [**`plot`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 15. How do I explore a pandas Series? ([video](https://www.youtube.com/watch?v=QTVTq8SPzxM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=15))

# In[92]:


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[93]:


# examine the data type of each Series
movies.dtypes


# **Exploring a non-numeric Series:**

# In[94]:


# count the non-null values, unique values, and frequency of the most common value
movies.genre.describe()


# Documentation for [**`describe`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.describe.html)

# In[95]:


# count how many times each value in the Series occurs
movies.genre.value_counts()


# Documentation for [**`value_counts`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html)

# In[96]:


# display percentages instead of raw counts
movies.genre.value_counts(normalize=True)


# In[97]:


# 'value_counts' (like many pandas methods) outputs a Series
type(movies.genre.value_counts())


# In[98]:


# thus, you can add another Series method on the end
movies.genre.value_counts().head()


# In[99]:


# display the unique values in the Series
movies.genre.unique()


# In[100]:


# count the number of unique values in the Series
movies.genre.nunique()


# Documentation for [**`unique`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.unique.html) and [**`nunique`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.nunique.html)

# In[101]:


# compute a cross-tabulation of two Series
pd.crosstab(movies.genre, movies.content_rating)


# Documentation for [**`crosstab`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.crosstab.html)

# **Exploring a numeric Series:**

# In[102]:


# calculate various summary statistics
movies.duration.describe()


# In[103]:


# many statistics are implemented as Series methods
movies.duration.mean()


# Documentation for [**`mean`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.mean.html)

# In[104]:


# 'value_counts' is primarily useful for categorical data, not numerical data
movies.duration.value_counts().head()


# In[105]:


# allow plots to appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[106]:


# histogram of the 'duration' Series (shows the distribution of a numerical variable)
movies.duration.plot(kind='hist')


# In[107]:


# bar plot of the 'value_counts' for the 'genre' Series
movies.genre.value_counts().plot(kind='bar')


# Documentation for [**`plot`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.plot.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 16. How do I handle missing values in pandas? ([video](https://www.youtube.com/watch?v=fCMrO_VzeL8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=16))

# In[108]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.tail()


# **What does "NaN" mean?**
# 
# - "NaN" is not a string, rather it's a special value: **`numpy.nan`**.
# - It stands for "Not a Number" and indicates a **missing value**.
# - **`read_csv`** detects missing values (by default) when reading the file, and replaces them with this special value.
# 
# Documentation for [**`read_csv`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)

# In[109]:


# 'isnull' returns a DataFrame of booleans (True if missing, False if not missing)
ufo.isnull().tail()


# In[110]:


# 'nonnull' returns the opposite of 'isnull' (True if not missing, False if missing)
ufo.notnull().tail()


# Documentation for [**`isnull`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.isnull.html) and [**`notnull`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.notnull.html)

# In[111]:


# count the number of missing values in each Series
ufo.isnull().sum()


# This calculation works because:
# 
# 1. The **`sum`** method for a DataFrame operates on **`axis=0`** by default (and thus produces column sums).
# 2. In order to add boolean values, pandas converts **`True`** to **1** and **`False`** to **0**.

# In[112]:


# use the 'isnull' Series method to filter the DataFrame rows
ufo[ufo.City.isnull()].head()


# **How to handle missing values** depends on the dataset as well as the nature of your analysis. Here are some options:

# In[113]:


# examine the number of rows and columns
ufo.shape


# In[114]:


# if 'any' values are missing in a row, then drop that row
ufo.dropna(how='any').shape


# Documentation for [**`dropna`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html)

# In[115]:


# 'inplace' parameter for 'dropna' is False by default, thus rows were only dropped temporarily
ufo.shape


# In[116]:


# if 'all' values are missing in a row, then drop that row (none are dropped in this case)
ufo.dropna(how='all').shape


# In[117]:


# if 'any' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape


# In[118]:


# if 'all' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='all').shape


# In[119]:


# 'value_counts' does not include missing values by default
ufo['Shape Reported'].value_counts().head()


# In[120]:


# explicitly include missing values
ufo['Shape Reported'].value_counts(dropna=False).head()


# Documentation for [**`value_counts`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html)

# In[121]:


# fill in missing values with a specified value
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)


# Documentation for [**`fillna`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html)

# In[122]:


# confirm that the missing values were filled in
ufo['Shape Reported'].value_counts().head()


# [Working with missing data in pandas](http://pandas.pydata.org/pandas-docs/stable/missing_data.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 17. What do I need to know about the pandas index? (Part 1) ([video](https://www.youtube.com/watch?v=OYZNk7Z9s6I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17))

# In[123]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[124]:


# every DataFrame has an index (sometimes called the "row labels")
drinks.index


# In[125]:


# column names are also stored in a special "index" object
drinks.columns


# In[126]:


# neither the index nor the columns are included in the shape
drinks.shape


# In[127]:


# index and columns both default to integers if you don't define them
pd.read_table('http://bit.ly/movieusers', header=None, sep='|').head()


# **What is the index used for?**
# 
# 1. identification
# 2. selection
# 3. alignment (covered in the next video)

# In[128]:


# identification: index remains with each row when filtering the DataFrame
drinks[drinks.continent=='South America']


# In[129]:


# selection: select a portion of the DataFrame using the index
drinks.loc[23, 'beer_servings']


# Documentation for [**`loc`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html)

# In[130]:


# set an existing column as the index
drinks.set_index('country', inplace=True)
drinks.head()


# Documentation for [**`set_index`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html)

# In[131]:


# 'country' is now the index
drinks.index


# In[132]:


# 'country' is no longer a column
drinks.columns


# In[133]:


# 'country' data is no longer part of the DataFrame contents
drinks.shape


# In[134]:


# country name can now be used for selection
drinks.loc['Brazil', 'beer_servings']


# In[135]:


# index name is optional
drinks.index.name = None
drinks.head()


# In[136]:


# restore the index name, and move the index back to a column
drinks.index.name = 'country'
drinks.reset_index(inplace=True)
drinks.head()


# Documentation for [**`reset_index`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html)

# In[137]:


# many DataFrame methods output a DataFrame
drinks.describe()


# In[138]:


# you can interact with any DataFrame using its index and columns
drinks.describe().loc['25%', 'beer_servings']


# [Indexing and selecting data](http://pandas.pydata.org/pandas-docs/stable/indexing.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 18. What do I need to know about the pandas index? (Part 2) ([video](https://www.youtube.com/watch?v=15q-is8P_H4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=18))

# In[139]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[140]:


# every DataFrame has an index
drinks.index


# In[141]:


# every Series also has an index (which carries over from the DataFrame)
drinks.continent.head()


# In[142]:


# set 'country' as the index
drinks.set_index('country', inplace=True)


# Documentation for [**`set_index`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html)

# In[143]:


# Series index is on the left, values are on the right
drinks.continent.head()


# In[144]:


# another example of a Series (output from the 'value_counts' method)
drinks.continent.value_counts()


# Documentation for [**`value_counts`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html)

# In[145]:


# access the Series index
drinks.continent.value_counts().index


# In[146]:


# access the Series values
drinks.continent.value_counts().values


# In[147]:


# elements in a Series can be selected by index (using bracket notation)
drinks.continent.value_counts()['Africa']


# In[148]:


# any Series can be sorted by its values
drinks.continent.value_counts().sort_values()


# In[149]:


# any Series can also be sorted by its index
drinks.continent.value_counts().sort_index()


# Documentation for [**`sort_values`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sort_values.html) and [**`sort_index`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sort_index.html)

# **What is the index used for?**
# 
# 1. identification (covered in the previous video)
# 2. selection (covered in the previous video)
# 3. alignment

# In[150]:


# 'beer_servings' Series contains the average annual beer servings per person
drinks.beer_servings.head()


# In[151]:


# create a Series containing the population of two countries
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
people


# Documentation for [**`Series`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html)

# In[152]:


# calculate the total annual beer servings for each country
(drinks.beer_servings * people).head()


# - The two Series were **aligned** by their indexes.
# - If a value is missing in either Series, the result is marked as **NaN**.
# - Alignment enables us to easily work with **incomplete data**.

# In[153]:


# concatenate the 'drinks' DataFrame with the 'population' Series (aligns by the index)
pd.concat([drinks, people], axis=1).head()


# Documentation for [**`concat`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)
# 
# [Indexing and selecting data](http://pandas.pydata.org/pandas-docs/stable/indexing.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 19. How do I select multiple rows and columns from a pandas DataFrame? ([video](https://www.youtube.com/watch?v=xvpNA7bC8cs&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=19))

# In[154]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head(3)


# The [**`loc`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html) method is used to select rows and columns by **label**. You can pass it:
# 
# - A single label
# - A list of labels
# - A slice of labels
# - A boolean Series
# - A colon (which indicates "all labels")

# In[155]:


# row 0, all columns
ufo.loc[0, :]


# In[156]:


# rows 0 and 1 and 2, all columns
ufo.loc[[0, 1, 2], :]


# In[157]:


# rows 0 through 2 (inclusive), all columns
ufo.loc[0:2, :]


# In[158]:


# this implies "all columns", but explicitly stating "all columns" is better
ufo.loc[0:2]


# In[159]:


# rows 0 through 2 (inclusive), column 'City'
ufo.loc[0:2, 'City']


# In[160]:


# rows 0 through 2 (inclusive), columns 'City' and 'State'
ufo.loc[0:2, ['City', 'State']]


# In[161]:


# accomplish the same thing using double brackets - but using 'loc' is preferred since it's more explicit
ufo[['City', 'State']].head(3)


# In[162]:


# rows 0 through 2 (inclusive), columns 'City' through 'State' (inclusive)
ufo.loc[0:2, 'City':'State']


# In[163]:


# accomplish the same thing using 'head' and 'drop'
ufo.head(3).drop('Time', axis=1)


# In[164]:


# rows in which the 'City' is 'Oakland', column 'State'
ufo.loc[ufo.City=='Oakland', 'State']


# In[165]:


# accomplish the same thing using "chained indexing" - but using 'loc' is preferred since chained indexing can cause problems
ufo[ufo.City=='Oakland'].State


# The [**`iloc`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iloc.html) method is used to select rows and columns by **integer position**. You can pass it:
# 
# - A single integer position
# - A list of integer positions
# - A slice of integer positions
# - A colon (which indicates "all integer positions")

# In[166]:


# rows in positions 0 and 1, columns in positions 0 and 3
ufo.iloc[[0, 1], [0, 3]]


# In[167]:


# rows in positions 0 through 2 (exclusive), columns in positions 0 through 4 (exclusive)
ufo.iloc[0:2, 0:4]


# In[168]:


# rows in positions 0 through 2 (exclusive), all columns
ufo.iloc[0:2, :]


# In[169]:


# accomplish the same thing - but using 'iloc' is preferred since it's more explicit
ufo[0:2]


# The [**`ix`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ix.html) method is used to select rows and columns by **label or integer position**, and should only be used when you need to mix label-based and integer-based selection in the same call.

# In[170]:


# read a dataset of alcohol consumption into a DataFrame and set 'country' as the index
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
drinks.head()


# In[171]:


# row with label 'Albania', column in position 0
drinks.ix['Albania', 0]


# In[172]:


# row in position 1, column with label 'beer_servings'
drinks.ix[1, 'beer_servings']


# **Rules for using numbers with `ix`:**
# 
# - If the index is **strings**, numbers are treated as **integer positions**, and thus slices are **exclusive** on the right.
# - If the index is **integers**, numbers are treated as **labels**, and thus slices are **inclusive**.

# In[173]:


# rows 'Albania' through 'Andorra' (inclusive), columns in positions 0 through 2 (exclusive)
drinks.ix['Albania':'Andorra', 0:2]


# In[174]:


# rows 0 through 2 (inclusive), columns in positions 0 through 2 (exclusive)
ufo.ix[0:2, 0:2]


# [Summary of the pandas API for selection](https://github.com/pydata/pandas/issues/9595)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 20. When should I use the "inplace" parameter in pandas? ([video](https://www.youtube.com/watch?v=XaCSdr7pPmY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=20))

# In[175]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()


# In[176]:


ufo.shape


# In[177]:


# remove the 'City' column (doesn't affect the DataFrame since inplace=False)
ufo.drop('City', axis=1).head()


# In[178]:


# confirm that the 'City' column was not actually removed
ufo.head()


# In[179]:


# remove the 'City' column (does affect the DataFrame since inplace=True)
ufo.drop('City', axis=1, inplace=True)


# In[180]:


# confirm that the 'City' column was actually removed
ufo.head()


# In[181]:


# drop a row if any value is missing from that row (doesn't affect the DataFrame since inplace=False)
ufo.dropna(how='any').shape


# In[182]:


# confirm that no rows were actually removed
ufo.shape


# In[183]:


# use an assignment statement instead of the 'inplace' parameter
ufo = ufo.set_index('Time')
ufo.tail()


# In[184]:


# fill missing values using "backward fill" strategy (doesn't affect the DataFrame since inplace=False)
ufo.fillna(method='bfill').tail()


# In[185]:


# compare with "forward fill" strategy (doesn't affect the DataFrame since inplace=False)
ufo.fillna(method='ffill').tail()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 21. How do I make my pandas DataFrame smaller and faster? ([video](https://www.youtube.com/watch?v=wDYDYGyN_cw&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=21))

# In[186]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[187]:


# exact memory usage is unknown because object columns are references elsewhere
drinks.info()


# In[188]:


# force pandas to calculate the true memory usage
drinks.info(memory_usage='deep')


# In[189]:


# calculate the memory usage for each Series (in bytes)
drinks.memory_usage(deep=True)


# Documentation for [**`info`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html) and [**`memory_usage`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.memory_usage.html)

# In[190]:


# use the 'category' data type (new in pandas 0.15) to store the 'continent' strings as integers
drinks['continent'] = drinks.continent.astype('category')
drinks.dtypes


# In[191]:


# 'continent' Series appears to be unchanged
drinks.continent.head()


# In[192]:


# strings are now encoded (0 means 'Africa', 1 means 'Asia', 2 means 'Europe', etc.)
drinks.continent.cat.codes.head()


# In[193]:


# memory usage has been drastically reduced
drinks.memory_usage(deep=True)


# In[194]:


# repeat this process for the 'country' Series
drinks['country'] = drinks.country.astype('category')
drinks.memory_usage(deep=True)


# In[195]:


# memory usage increased because we created 193 categories
drinks.country.cat.categories


# The **category** data type should only be used with a string Series that has a **small number of possible values**.

# In[196]:


# create a small DataFrame from a dictionary
df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})
df


# In[197]:


# sort the DataFrame by the 'quality' Series (alphabetical order)
df.sort_values('quality')


# In[198]:


# define a logical ordering for the categories
df['quality'] = df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
df.quality


# In[199]:


# sort the DataFrame by the 'quality' Series (logical order)
df.sort_values('quality')


# In[200]:


# comparison operators work with ordered categories
df.loc[df.quality > 'good', :]


# [Overview of categorical data in pandas](http://pandas.pydata.org/pandas-docs/stable/categorical.html)
# 
# [API reference for categorical methods](http://pandas.pydata.org/pandas-docs/stable/api.html#categorical)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 22. How do I use pandas with scikit-learn to create Kaggle submissions? ([video](https://www.youtube.com/watch?v=ylRlGCtAtiE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22))

# In[201]:


# read the training dataset from Kaggle's Titanic competition into a DataFrame
train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# **Goal:** Predict passenger survival aboard the Titanic based on [passenger attributes](https://www.kaggle.com/c/titanic/data)
# 
# **Video:** [What is machine learning, and how does it work?](https://www.youtube.com/watch?v=elojMnjn4kk&list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A&index=1)

# In[202]:


# create a feature matrix 'X' by selecting two DataFrame columns
feature_cols = ['Pclass', 'Parch']
X = train.loc[:, feature_cols]
X.shape


# In[203]:


# create a response vector 'y' by selecting a Series
y = train.Survived
y.shape


# **Note:** There is no need to convert these pandas objects to NumPy arrays. scikit-learn will understand these objects as long as they are entirely numeric and the proper shapes.

# In[204]:


# fit a classification model to the training data
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)


# **Video series:** [Introduction to machine learning with scikit-learn](https://www.youtube.com/playlist?list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A)

# In[205]:


# read the testing dataset from Kaggle's Titanic competition into a DataFrame
test = pd.read_csv('http://bit.ly/kaggletest')
test.head()


# In[206]:


# create a feature matrix from the testing data that matches the training data
X_new = test.loc[:, feature_cols]
X_new.shape


# In[207]:


# use the fitted model to make predictions for the testing set observations
new_pred_class = logreg.predict(X_new)


# In[208]:


# create a DataFrame of passenger IDs and testing set predictions
pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).head()


# Documentation for the [**`DataFrame`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) constructor

# In[209]:


# ensure that PassengerID is the first column by setting it as the index
pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).set_index('PassengerId').head()


# In[210]:


# write the DataFrame to a CSV file that can be submitted to Kaggle
pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).set_index('PassengerId').to_csv('sub.csv')


# Documentation for [**`to_csv`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html)

# In[211]:


# save a DataFrame to disk ("pickle it")
train.to_pickle('train.pkl')


# In[212]:


# read a pickled object from disk ("unpickle it")
pd.read_pickle('train.pkl').head()


# Documentation for [**`to_pickle`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_pickle.html) and [**`read_pickle`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_pickle.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 23. More of your pandas questions answered! ([video](https://www.youtube.com/watch?v=oH3wYKvwpJ8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=23))

# **Question:** Could you explain how to read the pandas documentation?
# 
# [pandas API reference](http://pandas.pydata.org/pandas-docs/stable/api.html)

# **Question:** What is the difference between **`ufo.isnull()`** and **`pd.isnull(ufo)`**?

# In[213]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()


# In[214]:


# use 'isnull' as a top-level function
pd.isnull(ufo).head()


# In[215]:


# equivalent: use 'isnull' as a DataFrame method
ufo.isnull().head()


# Documentation for [**`isnull`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.isnull.html)

# **Question:** Why are DataFrame slices inclusive when using **`.loc`**, but exclusive when using **`.iloc`**?

# In[216]:


# label-based slicing is inclusive of the start and stop
ufo.loc[0:4, :]


# In[217]:


# position-based slicing is inclusive of the start and exclusive of the stop
ufo.iloc[0:4, :]


# Documentation for [**`loc`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html) and [**`iloc`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iloc.html)

# In[218]:


# 'iloc' is simply following NumPy's slicing convention...
ufo.values[0:4, :]


# In[219]:


# ...and NumPy is simply following Python's slicing convention
'python'[0:4]


# In[220]:


# 'loc' is inclusive of the stopping label because you don't necessarily know what label will come after it
ufo.loc[0:4, 'City':'State']


# **Question:** How do I randomly sample rows from a DataFrame?

# In[221]:


# sample 3 rows from the DataFrame without replacement (new in pandas 0.16.1)
ufo.sample(n=3)


# Documentation for [**`sample`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sample.html)

# In[222]:


# use the 'random_state' parameter for reproducibility
ufo.sample(n=3, random_state=42)


# In[223]:


# sample 75% of the DataFrame's rows without replacement
train = ufo.sample(frac=0.75, random_state=99)


# In[224]:


# store the remaining 25% of the rows in another DataFrame
test = ufo.loc[~ufo.index.isin(train.index), :]


# Documentation for [**`isin`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.isin.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 24. How do I create dummy variables in pandas? ([video](https://www.youtube.com/watch?v=0s_1IsROgDc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=24))

# In[225]:


# read the training dataset from Kaggle's Titanic competition
train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# In[226]:


# create the 'Sex_male' dummy variable using the 'map' method
train['Sex_male'] = train.Sex.map({'female':0, 'male':1})
train.head()


# Documentation for [**`map`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html)

# In[227]:


# alternative: use 'get_dummies' to create one column for every possible value
pd.get_dummies(train.Sex).head()


# Generally speaking:
# 
# - If you have **"K" possible values** for a categorical feature, you only need **"K-1" dummy variables** to capture all of the information about that feature.
# - One convention is to **drop the first dummy variable**, which defines that level as the "baseline".

# In[228]:


# drop the first dummy variable ('female') using the 'iloc' method
pd.get_dummies(train.Sex).iloc[:, 1:].head()


# In[229]:


# add a prefix to identify the source of the dummy variables
pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:].head()


# In[230]:


# use 'get_dummies' with a feature that has 3 possible values
pd.get_dummies(train.Embarked, prefix='Embarked').head(10)


# In[231]:


# drop the first dummy variable ('C')
pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:, 1:].head(10)


# How to translate these values back to the original 'Embarked' value:
# 
# - **0, 0** means **C**
# - **1, 0** means **Q**
# - **0, 1** means **S**

# In[232]:


# save the DataFrame of dummy variables and concatenate them to the original DataFrame
embarked_dummies = pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:, 1:]
train = pd.concat([train, embarked_dummies], axis=1)
train.head()


# Documentation for [**`concat`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)

# In[233]:


# reset the DataFrame
train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# In[234]:


# pass the DataFrame to 'get_dummies' and specify which columns to dummy (it drops the original columns)
pd.get_dummies(train, columns=['Sex', 'Embarked']).head()


# In[235]:


# use the 'drop_first' parameter (new in pandas 0.18) to drop the first dummy variable for each feature
pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True).head()


# Documentation for [**`get_dummies`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 25. How do I work with dates and times in pandas? ([video](https://www.youtube.com/watch?v=yCgJGsg0Xa4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=25))

# In[236]:


# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()


# In[237]:


# 'Time' is currently stored as a string
ufo.dtypes


# In[238]:


# hour could be accessed using string slicing, but this approach breaks too easily
ufo.Time.str.slice(-5, -3).astype(int).head()


# In[239]:


# convert 'Time' to datetime format
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.head()


# In[240]:


ufo.dtypes


# Documentation for [**`to_datetime`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html)

# In[241]:


# convenient Series attributes are now available
ufo.Time.dt.hour.head()


# In[242]:


ufo.Time.dt.weekday_name.head()


# In[243]:


ufo.Time.dt.dayofyear.head()


# API reference for [datetime properties and methods](http://pandas.pydata.org/pandas-docs/stable/api.html#datetimelike-properties)

# In[244]:


# convert a single string to datetime format (outputs a timestamp object)
ts = pd.to_datetime('1/1/1999')
ts


# In[245]:


# compare a datetime Series with a timestamp
ufo.loc[ufo.Time >= ts, :].head()


# In[246]:


# perform mathematical operations with timestamps (outputs a timedelta object)
ufo.Time.max() - ufo.Time.min()


# In[247]:


# timedelta objects also have attributes you can access
(ufo.Time.max() - ufo.Time.min()).days


# In[248]:


# allow plots to appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[249]:


# count the number of UFO reports per year
ufo['Year'] = ufo.Time.dt.year
ufo.Year.value_counts().sort_index().head()


# In[250]:


# plot the number of UFO reports per year (line plot is the default)
ufo.Year.value_counts().sort_index().plot()


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 26. How do I find and remove duplicate rows in pandas? ([video](https://www.youtube.com/watch?v=ht5buXUMqkQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=26))

# In[251]:


# read a dataset of movie reviewers into a DataFrame
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')
users.head()


# In[252]:


users.shape


# In[253]:


# detect duplicate zip codes: True if an item is identical to a previous item
users.zip_code.duplicated().tail()


# In[254]:


# count the duplicate items (True becomes 1, False becomes 0)
users.zip_code.duplicated().sum()


# In[255]:


# detect duplicate DataFrame rows: True if an entire row is identical to a previous row
users.duplicated().tail()


# In[256]:


# count the duplicate rows
users.duplicated().sum()


# Logic for [**`duplicated`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.duplicated.html):
# 
# - **`keep='first'`** (default): Mark duplicates as True except for the first occurrence.
# - **`keep='last'`**: Mark duplicates as True except for the last occurrence.
# - **`keep=False`**: Mark all duplicates as True.

# In[257]:


# examine the duplicate rows (ignoring the first occurrence)
users.loc[users.duplicated(keep='first'), :]


# In[258]:


# examine the duplicate rows (ignoring the last occurrence)
users.loc[users.duplicated(keep='last'), :]


# In[259]:


# examine the duplicate rows (including all duplicates)
users.loc[users.duplicated(keep=False), :]


# In[260]:


# drop the duplicate rows (inplace=False by default)
users.drop_duplicates(keep='first').shape


# In[261]:


users.drop_duplicates(keep='last').shape


# In[262]:


users.drop_duplicates(keep=False).shape


# Documentation for [**`drop_duplicates`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop_duplicates.html)

# In[263]:


# only consider a subset of columns when identifying duplicates
users.duplicated(subset=['age', 'zip_code']).sum()


# In[264]:


users.drop_duplicates(subset=['age', 'zip_code']).shape


# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 27. How do I avoid a SettingWithCopyWarning in pandas? ([video](https://www.youtube.com/watch?v=4R4WsDJ-KVc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=27))

# In[265]:


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[266]:


# count the missing values in the 'content_rating' Series
movies.content_rating.isnull().sum()


# In[267]:


# examine the DataFrame rows that contain those missing values
movies[movies.content_rating.isnull()]


# In[268]:


# examine the unique values in the 'content_rating' Series
movies.content_rating.value_counts()


# **Goal:** Mark the 'NOT RATED' values as missing values, represented by 'NaN'.

# In[269]:


# first, locate the relevant rows
movies[movies.content_rating=='NOT RATED'].head()


# In[270]:


# then, select the 'content_rating' Series from those rows
movies[movies.content_rating=='NOT RATED'].content_rating.head()


# In[271]:


# finally, replace the 'NOT RATED' values with 'NaN' (imported from NumPy)
import numpy as np
movies[movies.content_rating=='NOT RATED'].content_rating = np.nan


# **Problem:** That statement involves two operations, a **`__getitem__`** and a **`__setitem__`**. pandas can't guarantee whether the **`__getitem__`** operation returns a view or a copy of the data.
# 
# - If **`__getitem__`** returns a view of the data, **`__setitem__`** will affect the 'movies' DataFrame.
# - But if **`__getitem__`** returns a copy of the data, **`__setitem__`** will not affect the 'movies' DataFrame.

# In[272]:


# the 'content_rating' Series has not changed
movies.content_rating.isnull().sum()


# **Solution:** Use the **`loc`** method, which replaces the 'NOT RATED' values in a single **`__setitem__`** operation.

# In[273]:


# replace the 'NOT RATED' values with 'NaN' (does not cause a SettingWithCopyWarning)
movies.loc[movies.content_rating=='NOT RATED', 'content_rating'] = np.nan


# In[274]:


# this time, the 'content_rating' Series has changed
movies.content_rating.isnull().sum()


# **Summary:** Use the **`loc`** method any time you are selecting rows and columns in the same statement.
# 
# **More information:** [Modern Pandas (Part 1)](http://tomaugspurger.github.io/modern-1.html)

# In[275]:


# create a DataFrame only containing movies with a high 'star_rating'
top_movies = movies.loc[movies.star_rating >= 9, :]
top_movies


# **Goal:** Fix the 'duration' for 'The Shawshank Redemption'.

# In[276]:


# overwrite the relevant cell with the correct duration
top_movies.loc[0, 'duration'] = 150


# **Problem:** pandas isn't sure whether 'top_movies' is a view or a copy of 'movies'.

# In[277]:


# 'top_movies' DataFrame has been updated
top_movies


# In[278]:


# 'movies' DataFrame has not been updated
movies.head(1)


# **Solution:** Any time you are attempting to create a DataFrame copy, use the [**`copy`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.copy.html) method.

# In[279]:


# explicitly create a copy of 'movies'
top_movies = movies.loc[movies.star_rating >= 9, :].copy()


# In[280]:


# pandas now knows that you are updating a copy instead of a view (does not cause a SettingWithCopyWarning)
top_movies.loc[0, 'duration'] = 150


# In[281]:


# 'top_movies' DataFrame has been updated
top_movies


# Documentation on indexing and selection: [Returning a view versus a copy](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy)
# 
# Stack Overflow: [What is the point of views in pandas if it is undefined whether an indexing operation returns a view or a copy?](http://stackoverflow.com/questions/34884536/what-is-the-point-of-views-in-pandas-if-it-is-undefined-whether-an-indexing-oper)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 28. How do I change display options in pandas? ([video](https://www.youtube.com/watch?v=yiO43TQ4xvc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=28))

# In[282]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')


# In[283]:


# only 60 rows will be displayed when printing
drinks


# In[284]:


# check the current setting for the 'max_rows' option
pd.get_option('display.max_rows')


# Documentation for [**`get_option`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_option.html)

# In[285]:


# overwrite the current setting so that all rows will be displayed
pd.set_option('display.max_rows', None)
drinks


# In[286]:


# reset the 'max_rows' option to its default
pd.reset_option('display.max_rows')


# Documentation for [**`set_option`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.set_option.html) and [**`reset_option`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.reset_option.html)

# In[287]:


# the 'max_columns' option is similar to 'max_rows'
pd.get_option('display.max_columns')


# In[288]:


# read the training dataset from Kaggle's Titanic competition into a DataFrame
train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# In[289]:


# an ellipsis is displayed in the 'Name' cell of row 1 because of the 'max_colwidth' option
pd.get_option('display.max_colwidth')


# In[290]:


# overwrite the current setting so that more characters will be displayed
pd.set_option('display.max_colwidth', 1000)
train.head()


# In[291]:


# overwrite the 'precision' setting to display 2 digits after the decimal point of 'Fare'
pd.set_option('display.precision', 2)
train.head()


# In[292]:


# add two meaningless columns to the drinks DataFrame
drinks['x'] = drinks.wine_servings * 1000
drinks['y'] = drinks.total_litres_of_pure_alcohol * 1000
drinks.head()


# In[293]:


# use a Python format string to specify a comma as the thousands separator
pd.set_option('display.float_format', '{:,}'.format)
drinks.head()


# In[294]:


# 'y' was affected (but not 'x') because the 'float_format' option only affects floats (not ints)
drinks.dtypes


# In[295]:


# view the option descriptions (including the default and current values)
pd.describe_option()


# In[296]:


# search for specific options by name
pd.describe_option('rows')


# Documentation for [**`describe_option`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.describe_option.html)

# In[297]:


# reset all of the options to their default values
pd.reset_option('all')


# [Options and Settings](http://pandas.pydata.org/pandas-docs/stable/options.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 29. How do I create a pandas DataFrame from another object? ([video](https://www.youtube.com/watch?v=-Ov1N1_FbP8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=29))

# In[298]:


# create a DataFrame from a dictionary (keys become column names, values become data)
pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'red']})


# In[299]:


# optionally specify the order of columns and define the index
df = pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'red']}, columns=['id', 'color'], index=['a', 'b', 'c'])
df


# Documentation for [**`DataFrame`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)

# In[300]:


# create a DataFrame from a list of lists (each inner list becomes a row)
pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']], columns=['id', 'color'])


# In[301]:


# create a NumPy array (with shape 4 by 2) and fill it with random numbers between 0 and 1
import numpy as np
arr = np.random.rand(4, 2)
arr


# In[302]:


# create a DataFrame from the NumPy array
pd.DataFrame(arr, columns=['one', 'two'])


# In[303]:


# create a DataFrame of student IDs (100 through 109) and test scores (random integers between 60 and 100)
pd.DataFrame({'student':np.arange(100, 110, 1), 'test':np.random.randint(60, 101, 10)})


# Documentation for [**`np.arange`**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html) and [**`np.random`**](http://docs.scipy.org/doc/numpy/reference/routines.random.html)

# In[304]:


# 'set_index' can be chained with the DataFrame constructor to select an index
pd.DataFrame({'student':np.arange(100, 110, 1), 'test':np.random.randint(60, 101, 10)}).set_index('student')


# Documentation for [**`set_index`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html)

# In[305]:


# create a new Series using the Series constructor
s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')
s


# Documentation for [**`Series`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html)

# In[306]:


# concatenate the DataFrame and the Series (use axis=1 to concatenate columns)
pd.concat([df, s], axis=1)


# **Notes:**
# 
# - The Series name became the column name in the DataFrame.
# - The Series data was aligned to the DataFrame by its index.
# - The 'shape' for row 'a' was marked as a missing value (NaN) because that index was not present in the Series.
# 
# Documentation for [**`concat`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)
# 
# [<a href="#Python-pandas-Q&A-video-series-by-Data-School">Back to top</a>]

# ## 30. How do I apply a function to a pandas Series or DataFrame? ([video](https://www.youtube.com/watch?v=P_q0tkYqvSk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=30))

# In[307]:


# read the training dataset from Kaggle's Titanic competition into a DataFrame
train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# **Goal:** Map the existing values of a Series to a different set of values
# 
# **Method:** [**`map`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html) (Series method)

# In[308]:


# map 'female' to 0 and 'male' to 1
train['Sex_num'] = train.Sex.map({'female':0, 'male':1})
train.loc[0:4, ['Sex', 'Sex_num']]


# **Goal:** Apply a function to each element in a Series
# 
# **Method:** [**`apply`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.apply.html) (Series method)
# 
# **Note:** **`map`** can be substituted for **`apply`** in many cases, but **`apply`** is more flexible and thus is recommended

# In[309]:


# calculate the length of each string in the 'Name' Series
train['Name_length'] = train.Name.apply(len)
train.loc[0:4, ['Name', 'Name_length']]


# In[310]:


# round up each element in the 'Fare' Series to the next integer
import numpy as np
train['Fare_ceil'] = train.Fare.apply(np.ceil)
train.loc[0:4, ['Fare', 'Fare_ceil']]


# In[311]:


# we want to extract the last name of each person
train.Name.head()


# In[312]:


# use a string method to split the 'Name' Series at commas (returns a Series of lists)
train.Name.str.split(',').head()


# In[313]:


# define a function that returns an element from a list based on position
def get_element(my_list, position):
    return my_list[position]


# In[314]:


# apply the 'get_element' function and pass 'position' as a keyword argument
train.Name.str.split(',').apply(get_element, position=0).head()


# In[315]:


# alternatively, use a lambda function
train.Name.str.split(',').apply(lambda x: x[0]).head()


# **Goal:** Apply a function along either axis of a DataFrame
# 
# **Method:** [**`apply`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) (DataFrame method)

# In[316]:


# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[317]:


# select a subset of the DataFrame to work with
drinks.loc[:, 'beer_servings':'wine_servings'].head()


# In[318]:


# apply the 'max' function along axis 0 to calculate the maximum value in each column
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0)


# In[319]:


# apply the 'max' function along axis 1 to calculate the maximum value in each row
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=1).head()


# In[320]:


# use 'np.argmax' to calculate which column has the maximum value for each row
drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1).head()


# **Goal:** Apply a function to every element in a DataFrame
# 
# **Method:** [**`applymap`**](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.applymap.html) (DataFrame method)

# In[321]:


# convert every DataFrame element into a float
drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float).head()

# overwrite the existing DataFrame columns
drinks.loc[:, 'beer_servings':'wine_servings'] = drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)
drinks.head()
