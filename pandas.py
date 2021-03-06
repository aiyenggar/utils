# Summarizes the number of non-null objects and dtypes
df.info()
# Get summary stats of df
df.describe()

# Drop rows with missing values and drop duplicate
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

import seaborn as sns
# Visualize pairplot of df
sns.pairplot(df, hue='rating');

# Group by year
df_by_year = df.groupby('release_year')
# Check type of GroupBy object
type(df_by_year)
pandas.core.groupby.DataFrameGroupBy
# Summary stats over years
df_by_year.describe().head()
# Cast grouping as a list and check out one year
list(df_by_year)[10]
# Get median values by year and print first 5 rows
df_med_by_year = df_by_year.median()
df_med_by_year.head()

# Print index of df
print(df.index)

# Print index
print(df_med_by_year.index)

# Slice out user rating and plot
df_rat_by_year = df_med_by_year['user_rating_score']
plt.scatter(df_rat_by_year.index, df_rat_by_year)
plt.xlabel('year of release')
plt.ylabel('median rating');

devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result,
                  devices[['manufacturer', 'Model']],
                  left_on='device',
                  right_on='Model',
                  how='left')

result.groupby("manufacturer").agg({
        "outgoing_mins_per_month": "mean",
        "outgoing_sms_per_month": "mean",
        "monthly_mb": "mean",
        "use_id": "count"
    })

df.set_index(pd.DatetimeIndex(df['date']), inplace=True)
df.set_index(['date', 'language'], inplace=True)

df.index
df.loc['2017-01-02']
df.columns

# Set multiindex
df.set_index(['date', 'language'], inplace=True)
df.loc[('2017-01-02', 'r')]

# Swap levels of multi-index
df.swaplevel()
# Unstack your multi-index
df.unstack()
# Unsstack the outer index
df.unstack(level=0)

#Check how many rows in DataFrame contain certain substring s in column col
print(len(df[df['col'].str.contains("s")].index.values[:]))

#Get indices of rows that contain substring s in column col
print(len(df[df['col'].str.contains("s")].index.values[:]))

# List unique values in a DataFrame column
# h/t @makmanalp for the updated syntax!
df['Column Name'].unique()

# Convert Series datatype to numeric (will error if column has non-numeric values)
# h/t @makmanalp
pd.to_numeric(df['Column Name'])

# Convert Series datatype to numeric, changing non-numeric values to NaN
# h/t @makmanalp for the updated syntax!
pd.to_numeric(df['Column Name'], errors='coerce')

# Grab DataFrame rows where column has certain values
valuelist = ['value1', 'value2', 'value3']
df = df[df.column.isin(valuelist)]

# Grab DataFrame rows where column doesn't have certain values
valuelist = ['value1', 'value2', 'value3']
df = df[~df.column.isin(value_list)]

# Delete column from DataFrame
del df['column']

# Select from DataFrame using criteria from multiple columns
# (use `|` instead of `&` to do an OR)
newdf = df[(df['column_one']>2004) & (df['column_two']==9)]

# Rename several DataFrame columns
df = df.rename(columns = {
    'col1 old name':'col1 new name',
    'col2 old name':'col2 new name',
    'col3 old name':'col3 new name',
})

# Lower-case all DataFrame column names
df.columns = map(str.lower, df.columns)

# Even more fancy DataFrame column re-naming
# lower-case all DataFrame column names (for example)
df.rename(columns=lambda x: x.split('.')[-1], inplace=True)

# Loop through rows in a DataFrame
# (if you must)
for index, row in df.iterrows():
    print index, row['some column']

# Much faster way to loop through DataFrame rows
# if you can work with tuples
# (h/t hughamacmullaniv)
for row in df.itertuples():
    print(row)

# Next few examples show how to work with text data in Pandas.
# Full list of .str functions: http://pandas.pydata.org/pandas-docs/stable/text.html

# Slice values in a DataFrame column (aka Series)
df.column.str[0:2]

# Lower-case everything in a DataFrame column
df.column_name = df.column_name.str.lower()

# Get length of data in a DataFrame column
df.column_name.str.len()

# Sort dataframe by multiple columns
df = df.sort_values(['col1','col2','col3'],ascending=[1,1,0])

# Get top n for each group of columns in a sorted dataframe
# (make sure dataframe is sorted first)
top5 = df.groupby(['groupingcol1', 'groupingcol2']).head(5)

# Grab DataFrame rows where specific column is null/notnull
newdf = df[df['column'].isnull()]

# Select from DataFrame using multiple keys of a hierarchical index
df.xs(('index level 1 value','index level 2 value'), level=('level 1','level 2'))

# Change all NaNs to None (useful before
# loading to a db)
df = df.where((pd.notnull(df)), None)

# More pre-db insert cleanup...make a pass through the dataframe, stripping whitespace
# from strings and changing any empty values to None
# (not especially recommended but including here b/c I had to do this in real life one time)
df = df.applymap(lambda x: str(x).strip() if len(str(x).strip()) else None)

# Get quick count of rows in a DataFrame
len(df.index)

# Pivot data (with flexibility about what what
# becomes a column and what stays a row).
# Syntax works on Pandas >= .14
pd.pivot_table(
  df,values='cell_value',
  index=['col1', 'col2', 'col3'], #these stay as columns; will fail silently if any of these cols have null values
  columns=['col4']) #data values in this column become their own column

# Change data type of DataFrame column
df.column_name = df.column_name.astype(np.int64)

# Get rid of non-numeric values throughout a DataFrame:
for col in refunds.columns.values:
  refunds[col] = refunds[col].replace('[^0-9]+.-', '', regex=True)

# Set DataFrame column values based on other column values (h/t: @mlevkov)
df.loc[(df['column1'] == some_value) & (df['column2'] == some_other_value), ['column_to_change']] = new_value

# Clean up missing values in multiple DataFrame columns
df = df.fillna({
    'col1': 'missing',
    'col2': '99.999',
    'col3': '999',
    'col4': 'missing',
    'col5': 'missing',
    'col6': '99'
})

# Concatenate two DataFrame columns into a new, single column
# (useful when dealing with composite keys, for example)
# (h/t @makmanalp for improving this one!)
df['newcol'] = df['col1'].astype(str) + df['col2'].astype(str)

# Doing calculations with DataFrame columns that have missing values
# In example below, swap in 0 for df['col1'] cells that contain null
df['new_col'] = np.where(pd.isnull(df['col1']),0,df['col1']) + df['col2']

# Split delimited values in a DataFrame column into two new columns
df['new_col1'], df['new_col2'] = zip(*df['original_col'].apply(lambda x: x.split(': ', 1)))

# Collapse hierarchical column indexes
df.columns = df.columns.get_level_values(0)

# Convert Django queryset to DataFrame
qs = DjangoModelName.objects.all()
q = qs.values()
df = pd.DataFrame.from_records(q)

# Create a DataFrame from a Python dictionary
df = pd.DataFrame(list(a_dictionary.items()), columns = ['column1', 'column2'])

# Get a report of all duplicate records in a dataframe, based on specific columns
dupes = df[df.duplicated(['col1', 'col2', 'col3'], keep=False)]

# Set up formatting so larger numbers aren't displayed in scientific notation (h/t @thecapacity)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
# To display with commas and no decimals
pd.options.display.float_format = '{:,.0f}'.format


# having grouped by department in by_dept, how to get the five most popular departments
by_dept.title.nunique().sort_values(ascending=False)[:5]

#TODO learn to master the apply function

np.arange (not arrange, I initially mistook)  returns an list of evenly spaced elements. Can be used in ranking.
Apparently adding 1 to a list adds 1 to each of the elements. Incredible.

# clearly the groupby function is powerful. I think I need to learn better how to use the apply, and aggregate functions. Keep thinking and looking at good Python code, and life will get better

# data.loc[] takes a second parameter that allows you to specify which columns you with to select. Like data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

You can impute values (especially when they are missing) this way: data['Gender'].fillna(mode(data['Gender']).mode[0], inplace=True). fillna basically replaces something when it is null. How do you change only those values that match a particular value, the more generalized version of fillna?
For this there seems to be a replace function. data['item']=data['item'].replace('sms', 'text')

This one is fantastic. First it tells you how to change a specfic cell. Second it tells you how you can change it to a value that is calculated based on the rest of the data - a sort of imputation to median, mode etc.
impute_grps = data.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
for i,row in data.loc[data['LoanAmount'].isnull(),:].iterrows():
  ind = tuple([row['Gender'],row['Married'],row['Self_Employed']])
  data.loc[i,'LoanAmount'] = impute_grps.loc[ind].values[0]

axis = 0 means you go column by column and axis = 1 means you go row by row. of course axis = 0 means row and axis = 1 means column.

Binning is an interesting idea where you take a continuous value and put it into discrete bins. basically pd.cut(column, bin=a list of boundary values, labels= a list of associated category names). labels will be one less than boundary values.

df.query('a < b and b < c')
df.query('a < b < c')

http://pandas.pydata.org/pandas-docs/stable/indexing.html has a lot of examples using many different variations. Nice to practice, but a little long.

"""
    Turning out to miss the location_id
    citn = citn.set_index('p_location_id').join(pat_location.set_index('p_id'))
    citn = citn.set_index('c_location_id').join(cit_location.set_index('c_id'))
"""
    # Get locationid for the rawlocation_id for the inventors above. Find out how to select pandas rows that match of many values

"""
The following works for a one to one mapping. You can avoid a join. But in case you want to pull multiple fields then a join may become mandatory.

manip['p_location_id'] = manip.p_rawlocation_id.replace(citn_rawlocation.set_index('id')['location_id'])
manip['c_location_id'] = manip.c_rawlocation_id.replace(citn_rawlocation.set_index('id')['location_id'])
"""

"""
Some amazing discoveries by aiyenggar
"""

conditions10 = [ df_inventor['ua1'] >= 0, df_inventor['ua2'] >= 0, df_inventor['ua3'] >= 0 ]
choices10 = [ df_inventor['ua1'], df_inventor['ua2'], df_inventor['ua3'] ]
df_inventor['ua'] = np.select(conditions10, choices10, default=-1)
df_inventor['ualist'] = df_inventor['ua'].apply(lambda x: [x])
df_inventor = df_inventor[['patent_id', 'ualist']]
df_inventor = df_inventor.groupby('patent_id').agg({'ualist':'sum'})

To read a large file in parts and put it into a pandas dataframe
iter_csv = pd.read_csv('file.csv', iterator=True, chunksize=10000000)
df = pd.concat([chunk[chunk['field'] > cutoff] for chunk in iter_csv)

To find the unique values of an index (even if a multiindex)
df.index for the overall index (including single and multiindex)
df.index.levels[index_subscript] for a specific index in a multiindex

to access based on index use .loc, for a wild card leave blank but place appropriate number of commas (1 less than number of index fields in the multiindex)
df.loc[(3045, '3930274', ), ['q4','year']]


df1['matched'].value_counts() to get histogram counts
df1.hist() for histogram chart, but only works on numeric fields
df1._merge.unique() unique values in the column
df1.describe()
df1.info()
dict([(v, df3[v].apply(lambda r: len(str(r)) if r!=None else 0).max())for v in df3.columns.values]) gets the max length of each column

-----------------------------------
--------  Learning Groupby --------
-----------------------------------

data.sample(n=5)
data.sort_values(by='arr_delay', ascending=False)[:10]
def is_delayed(x):
    return x > 0
data['delayed'] = data['arr_delay'].apply(is_delayed)
data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)
data['delayed'].value_counts()
not_delayed = data['delayed'].value_counts()[0] # first value of the result above
delayed = data['delayed'].value_counts()[1] # second value of the result above
total_flights = not_delayed + delayed # total count of flights
print float(delayed) / total_flights # converting to float to get a float result

not_delayed, delayed = data['cancelled'].value_counts()
print delayed / (delayed + not_delayed), '<- without conversion'
print float(delayed) / (delayed + not_delayed), '<- _with_ conversion!'
group_by_carrier = data.groupby(['unique_carrier','delayed'])
group_by_carrier.size() # Count by the grouping
count_delays_by_carrier = group_by_carrier.size().unstack()
count_delays_by_carrier.plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')

You can customize plots a number of ways. Here's a quick guide to common parameters:

kind=: 'line', 'bar', 'barh', 'hist', 'box', 'area', 'scatter'
figsize=: (width, height) in inches
colormap=: a long list of color palettes, including: 'autumn', 'winter', 'summer'
title=: a string
stacked=: stack the values vertically (instead of allowing them to overlap)

Pivot Table
flights_by_carrier = data.pivot_table(index='flight_date', columns='unique_carrier', values='flight_num', aggfunc='count')
flights_by_carrier.head()
data.pivot_table(columns='flight_date') # gives aggregate stats on all fields
delays_list = ['carrier_delay','weather_delay','late_aircraft_delay','nas_delay','security_delay']
flight_delays_by_day = data.pivot_table(index='flight_date', values=delays_list, aggfunc='sum')
flight_delays_by_day.plot(kind='area', figsize=[16,6], stacked=True, colormap='autumn') # area plot
pd.Series([1, 2, 5, 9, 12, 20]).plot(kind='hist', bins=[0,10,20]) # `bins` defines the start and end points of bins Histogram
bin_values = np.arange(start=-50, stop=200, step=10)

bin_values = np.arange(start=-50, stop=200, step=10)
us_mq_airlines_index = data['unique_carrier'].isin(['US','MQ']) # create index of flights from those airlines
us_mq_airlines = data[us_mq_airlines_index] # select rows
group_carriers = us_mq_airlines.groupby('unique_carrier')['arr_delay'] # group values by carrier, select minutes delayed
group_carriers.plot(kind='hist', bins=bin_values, figsize=[12,6], alpha=.4, legend=True) # alpha for transparency
    
hi_volume_airports_pivots = hi_volume_airports.pivot_table(index='flight_date', columns='origin', values='arr_delay')
hi_volume_airports_pivots.plot(kind='box', figsize=[16,8])

bins = pd.cut(df["temp_c"], bins=3, labels=("cool", "warm", "hot"))

df.resample("Q")["co"].agg(["max", "min"]) # resample is an alternative to groupby where you pass a frequency string "Q" in the above case, usually time	

f.groupby("outlet", sort=False)["title"].apply(lambda ser: ser.str.contains("Fed").sum()).nlargest(10)


# Create storage object with filename `processed_data`
data_store = pd.HDFStore('processed_data.h5')

# Put DataFrame into the object setting the key as 'preprocessed_df'
data_store['preprocessed_df'] = df
data_store.close()

# Access data store
data_store = pd.HDFStore('processed_data.h5')

# Retrieve data using key
preprocessed_df = data_store['preprocessed_df']
data_store.close()

------------------------------
------------ Config ----------
------------------------------

# Use 3 decimal places in output display
pd.set_option("display.precision", 3)

# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)

# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 25)

# Check for occurances of string
df2.organization.str.contains('Toyota').sum()