import pandas as pd
df = pd.read_csv('sample_data/salaries_by_college_major.csv')
print(df.head())

# number of rows and columns
df.shape

# show column names
df.columns

# show the cells where there is a NaN value
df.isna()

# return the 5 first of last rows
df.tail()
df.head()

# drop the lines where there is a NaN and return the new data frame
clean_df = df.dropna()

# return the selected column
clean_df['Mid-Career Median Salary']

# return the max value 
clean_df['Mid-Career Median Salary'].max()

# retun the index of the max value of the selected column
clean_df['Mid-Career Median Salary'].idxmax()
clean_df['Starting Median Salary'].idxmin()

# return the row 8
clean_df.loc[8]

# create a new column with arithmetic
spread_column = (clean_df['Mid-Career 90th Percentile Salary']-clean_df['Mid-Career 10th Percentile Salary'])

# insert a new column
clean_df.insert(1,'spread',spread_column)

# sort the values depending on a column
clean_df.sort_values('spread')

# ex 
res1 = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False).head()

res2 = clean_df.sort_values('spread', ascending=False).head()


# pivoting
# count the number of rows by group : 
df.groupby('Group_name').count()

#formation the output after this line
pd.options.display.float_format = '{:,.2f}'.format

# sum the other cells after grouping :
df.groupby('Group_name').mean()