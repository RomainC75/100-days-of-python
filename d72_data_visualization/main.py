import pandas as pd
import matplotlib.pyplot as plt

#import
# df = pd.read_csv("QueryResults.csv")
#rename the columns 
# df.columns=['DATE', 'TAG', 'POSTS']

# or import + rename 
df = pd.read_csv("QueryResults.old.csv",names=['DATE', 'TAG', 'POSTS'],header=0)

print(df.head())

print(df.shape)
count = df.count()
print(count)

# get the total number of posts
pivoted_by_language_number_of_posts = df.groupby('TAG').sum()
print(pivoted_by_language_number_of_posts)

#get the total number of months
pivoted_by_language_number_of_months = df.groupby('TAG').count()
print(pivoted_by_language_number_of_months)

print(df['DATE'][0])
print(df.DATE[0])

#convert to datetime a cell
converted = pd.to_datetime(df['DATE'][1])
print("converted : ", converted)

# convert the ENTIRE row to datetime
converted_row = pd.to_datetime(df['DATE'])
print(converted_row)

#pivoted df
pivoted_df = df.pivot(index="DATE",columns="TAG",values="POSTS")
pivoted_df.fillna(0,inplace=True)
print("=======================")
print("======",pivoted_df, pivoted_df.shape, pivoted_df.columns, pivoted_df.count())

# print(pivoted_df.isna().values.any())

plt.style.use('_mpl-gallery')


# fig, ax = plt.subplots()


# pivoted_df = pivoted_df.rolling(window=6).mean()
colors = ['blue','orange','green','red','purple','brown','pink','gray','olive','cyan']


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date',fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0,35000)

for index,column_name in enumerate(pivoted_df.columns):
    print("====",pivoted_df[column_name].name)
    plt.plot(pivoted_df.index, 
        pivoted_df[column_name],
        color=colors[index%len(colors)],
        linewidth=3,
        label=column_name)

plt.legend(fontsize=16)
plt.show()
