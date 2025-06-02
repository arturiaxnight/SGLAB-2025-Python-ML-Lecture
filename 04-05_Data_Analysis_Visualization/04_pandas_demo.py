# pip install pandas
#%%
import pandas as pd

#%%
# --- 1. Creating, Reading and Writing ---
# You can't work with data if you can't read it. Get started here.

# Creating DataFrames
data_dict = {'col1': [1, 2], 'col2': [3, 4]}
df_from_dict = pd.DataFrame(data_dict)
print("DataFrame from Dictionary:\n", df_from_dict)

data_list = [[1, 'apple'], [2, 'banana']]
df_from_list = pd.DataFrame(data_list, columns=['id', 'fruit'])
print("\nDataFrame from List:\n", df_from_list)

# Creating Series
series_example = pd.Series([10, 20, 30], name='counts')
print("\nSeries Example:\n", series_example)

# Reading Data (Placeholder - requires actual data file)
# try:
#     df_from_csv = pd.read_csv('your_data.csv')
#     print("\nDataFrame from CSV:\n", df_from_csv.head())
# except FileNotFoundError:
#     print("\nInfo: 'your_data.csv' not found. Skipping CSV read example.")

# try:
#     df_from_excel = pd.read_excel('your_data.xlsx')
#     print("\nDataFrame from Excel:\n", df_from_excel.head())
# except FileNotFoundError:
#     print("\nInfo: 'your_data.xlsx' not found. Skipping Excel read example.")


# Writing Data
# df_from_dict.to_csv('output_data.csv', index=False) # index=False prevents writing row indices
# df_from_dict.to_excel('output_data.xlsx', index=False)
print("\nInfo: Writing examples commented out to prevent file creation during demo run.")


print("\n" + "="*30 + "\n")

#%%
# --- 2. Indexing, Selecting & Assigning ---
# Pro data scientists do this dozens of times a day. You can, too!

# Sample DataFrame
data = {'col_a': [10, 20, 30, 40, 50],
        'col_b': ['A', 'B', 'C', 'D', 'E'],
        'col_c': [True, False, True, False, True]}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4', 'row5'])
print("Sample DataFrame for Indexing/Selecting:\n", df)

# Selecting Columns
col_a_data = df['col_a']
print("\nSelecting Column 'col_a':\n", col_a_data)
print("\nType of selected column:", type(col_a_data)) # It's a Series

subset_cols = df[['col_a', 'col_c']]
print("\nSelecting Multiple Columns ['col_a', 'col_c']:\n", subset_cols)
print("\nType of selected columns:", type(subset_cols)) # It's a DataFrame

# Selecting Rows using .loc (label-based)
row2_data = df.loc['row2']
print("\nSelecting Row 'row2' using .loc:\n", row2_data)

rows_1_3 = df.loc[['row1', 'row3']]
print("\nSelecting Rows 'row1' and 'row3' using .loc:\n", rows_1_3)

# Selecting Rows using .iloc (integer position-based)
row_at_pos_0 = df.iloc[0]
print("\nSelecting Row at index 0 using .iloc:\n", row_at_pos_0)

rows_at_pos_1_to_3 = df.iloc[1:4] # Selects rows at index 1, 2, 3 (exclusive of 4)
print("\nSelecting Rows at index 1 to 3 using .iloc:\n", rows_at_pos_1_to_3)

# Selecting specific rows and columns
val_at_row2_col_b_loc = df.loc['row2', 'col_b']
print("\nValue at 'row2', 'col_b' using .loc:", val_at_row2_col_b_loc)

val_at_pos_0_1_iloc = df.iloc[0, 1] # Row index 0, Column index 1
print("\nValue at index [0, 1] using .iloc:", val_at_pos_0_1_iloc)

subset_loc = df.loc[['row1', 'row4'], ['col_a', 'col_b']]
print("\nSubset using .loc:\n", subset_loc)

subset_iloc = df.iloc[[0, 3], [0, 1]] # Rows 0, 3 and Columns 0, 1
print("\nSubset using .iloc:\n", subset_iloc)

# Conditional Selection
condition = df['col_a'] > 25
print("\nConditional Selection (col_a > 25):\n", df[condition])
# Alternative syntax: df[df['col_a'] > 25]

condition_bool = df['col_c'] == True
print("\nConditional Selection (col_c is True):\n", df[condition_bool])
# Alternative syntax: df[df['col_c']]

combined_condition = (df['col_a'] < 30) & (df['col_c'] == True) # Use & for AND, | for OR
print("\nCombined Condition (col_a < 30 AND col_c is True):\n", df[combined_condition])

# Assigning Values
# Assign a single value to a column
df['new_col_scalar'] = 100
print("\nAssigning a scalar value to a new column:\n", df)

# Assign a list/Series to a new column (length must match)
df['new_col_list'] = [1, 2, 3, 4, 5]
print("\nAssigning a list to a new column:\n", df)

# Assigning with .loc or .iloc
df.loc['row1', 'col_a'] = 999 # Modify a specific value
print("\nAssigning value using .loc:\n", df)

df.loc[df['col_a'] > 40, 'col_b'] = 'Z' # Assign based on condition
print("\nAssigning value based on condition using .loc:\n", df)


print("\n" + "="*30 + "\n")

#%%
# --- 3. Summary Functions and Maps ---
# Extract insights from your data.

# Sample DataFrame
data_summary = {'category': ['A', 'B', 'A', 'C', 'B', 'A'],
                'value1': [10, 15, 12, 18, 20, 11],
                'value2': [100, 110, 105, 120, 115, 108]}
df_summary = pd.DataFrame(data_summary)
print("Sample DataFrame for Summary/Maps:\n", df_summary)

# describe() - Generates descriptive statistics
print("\nDescriptive Statistics (.describe()):\n", df_summary.describe())
print("\nDescribe on a specific column ('value1'):\n", df_summary['value1'].describe())

# Other summary functions
print("\nMean of 'value1':", df_summary['value1'].mean())
print("Sum of 'value2':", df_summary['value2'].sum())
print("Median of 'value1':", df_summary['value1'].median())
print("Minimum of 'value2':", df_summary['value2'].min())
print("Maximum of 'value1':", df_summary['value1'].max())
print("Standard Deviation of 'value2':", df_summary['value2'].std())

# unique() - Find unique values in a Series
print("\nUnique values in 'category':", df_summary['category'].unique())

# nunique() - Count unique values
print("Number of unique values in 'category':", df_summary['category'].nunique())

# value_counts() - Count occurrences of each unique value
print("\nValue Counts for 'category':\n", df_summary['category'].value_counts())

# map() - Substitute each value in a Series
category_map = {'A': 'Type Alpha', 'B': 'Type Beta', 'C': 'Type Gamma'}
df_summary['category_mapped'] = df_summary['category'].map(category_map)
print("\nDataFrame with mapped category:\n", df_summary)

# apply() - Apply a function along an axis of the DataFrame or on a Series
def custom_func(x):
    return x * 2

df_summary['value1_doubled'] = df_summary['value1'].apply(custom_func)
print("\nDataFrame with 'value1' doubled using apply():\n", df_summary)

# Apply function row-wise/column-wise (axis=0 for column, axis=1 for row)
df_summary['value1_plus_value2'] = df_summary.apply(lambda row: row['value1'] + row['value2'], axis=1)
print("\nDataFrame with sum of value1 and value2 using apply(axis=1):\n", df_summary)


print("\n" + "="*30 + "\n")

#%%
# --- 4. Grouping and Sorting ---
# Scale up your level of insight. The more complex the dataset, the more this matters

# Sample DataFrame (reusing df_summary)
print("Sample DataFrame for Grouping/Sorting:\n", df_summary[['category', 'value1', 'value2']])

# Grouping with groupby()
grouped_by_category = df_summary.groupby('category')

# Aggregations on grouped data
print("\nMean values grouped by category:\n", grouped_by_category.mean(numeric_only=True)) # numeric_only=True for newer pandas versions
print("\nSum of values grouped by category:\n", grouped_by_category.sum(numeric_only=True))
print("\nSize of each group:\n", grouped_by_category.size()) # Counts rows per group
print("\nCount of non-NA values per group:\n", grouped_by_category.count()) # Counts non-NA values per column per group

# Aggregate with multiple functions
agg_funcs = {'value1': ['mean', 'min', 'max'], 'value2': 'sum'}
print("\nMultiple aggregations grouped by category:\n", grouped_by_category.agg(agg_funcs))

# Grouping by multiple columns
# Add another column for multi-level grouping
df_summary['sub_category'] = ['X', 'Y', 'X', 'Y', 'X', 'Y']
print("\nDataFrame with sub_category added:\n", df_summary[['category', 'sub_category', 'value1']])
grouped_multi = df_summary.groupby(['category', 'sub_category'])
print("\nMean values grouped by category and sub_category:\n", grouped_multi.mean(numeric_only=True))

# Sorting
# Sort by values
df_sorted_value1 = df_summary.sort_values(by='value1')
print("\nDataFrame sorted by 'value1' (ascending):\n", df_sorted_value1)

df_sorted_value1_desc = df_summary.sort_values(by='value1', ascending=False)
print("\nDataFrame sorted by 'value1' (descending):\n", df_sorted_value1_desc)

# Sort by multiple columns
df_sorted_multi = df_summary.sort_values(by=['category', 'value1'], ascending=[True, False]) # Sort by category asc, then value1 desc
print("\nDataFrame sorted by 'category' (asc) then 'value1' (desc):\n", df_sorted_multi)

# Sort by index
df_indexed = df_summary.set_index('category') # Set 'category' as index first
print("\nDataFrame with 'category' as index:\n", df_indexed)
df_sorted_index = df_indexed.sort_index()
print("\nDataFrame sorted by index ('category'):\n", df_sorted_index)


print("\n" + "="*30 + "\n")

#%%
# --- 5. Data Types and Missing Values ---
# Deal with the most common progress-blocking problems

# Sample DataFrame with mixed types and missing values
data_types_missing = {'col_int': [1, 2, 3, None, 5],
                      'col_float': [1.1, 2.2, None, 4.4, 5.5],
                      'col_str': ['apple', 'banana', 'orange', 'grape', None],
                      'col_bool': [True, False, True, None, False]}
df_types = pd.DataFrame(data_types_missing)
print("Sample DataFrame for Data Types/Missing Values:\n", df_types)

# Checking Data Types
print("\nData Types (dtypes):\n", df_types.dtypes)

# Checking for Missing Values (isnull / isna)
print("\nMissing Values Check (isnull()):\n", df_types.isnull())
print("\nSum of Missing Values per Column:\n", df_types.isnull().sum())

# Handling Missing Values
# dropna() - Remove rows or columns with missing values
df_dropped_rows = df_types.dropna() # Drops rows with any NA
print("\nDataFrame after dropping rows with any NA:\n", df_dropped_rows)

df_dropped_cols = df_types.dropna(axis=1) # Drops columns with any NA
print("\nDataFrame after dropping columns with any NA:\n", df_dropped_cols)

df_dropped_subset = df_types.dropna(subset=['col_int']) # Drops rows where 'col_int' is NA
print("\nDataFrame after dropping rows where 'col_int' is NA:\n", df_dropped_subset)

# fillna() - Fill missing values
df_filled_zero = df_types.fillna(0) # Fill all NA with 0
print("\nDataFrame after filling NA with 0:\n", df_filled_zero)

fill_values = {'col_int': df_types['col_int'].mean(),
               'col_float': df_types['col_float'].median(),
               'col_str': 'Unknown',
               'col_bool': df_types['col_bool'].mode()[0]} # Mode can return multiple values, take the first
df_filled_specific = df_types.fillna(value=fill_values)
print("\nDataFrame after filling NA with specific values (mean, median, 'Unknown', mode):\n", df_filled_specific)

# Fill using forward fill (ffill) or backward fill (bfill)
df_filled_ffill = df_types.fillna(method='ffill')
print("\nDataFrame after forward fill (ffill):\n", df_filled_ffill)

df_filled_bfill = df_types.fillna(method='bfill')
print("\nDataFrame after backward fill (bfill):\n", df_filled_bfill)

# Converting Data Types (astype)
# Note: Cannot convert column with NA to int directly unless using nullable Int64 type
# First, fill or drop NAs if converting to standard int/float
df_filled_for_astype = df_types.fillna({'col_int': 0, 'col_float': 0.0})
df_filled_for_astype['col_int'] = df_filled_for_astype['col_int'].astype(int)
df_filled_for_astype['col_float'] = df_filled_for_astype['col_float'].astype(float) # Already float, but example
# df_filled_for_astype['col_bool'] = df_filled_for_astype['col_bool'].astype(bool) # Be careful with NA -> bool conversion
print("\nDataTypes after filling NA and using astype():\n", df_filled_for_astype.dtypes)

# Using Pandas nullable types (handles NA)
df_types['col_int_nullable'] = df_types['col_int'].astype('Int64') # Capital 'I'
df_types['col_bool_nullable'] = df_types['col_bool'].astype('boolean') # lowercase 'b'
print("\nDataFrame with Pandas nullable types (Int64, boolean):\n", df_types)
print("\nDataTypes with nullable types:\n", df_types.dtypes)


print("\n" + "="*30 + "\n")

#%%
# --- 6. Renaming and Combining ---
# Data comes in from many sources. Help it all make sense together

# Renaming Columns and Index
df_rename = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['row_x', 'row_y'])
print("Original DataFrame for Renaming:\n", df_rename)

# Rename columns
df_renamed_cols = df_rename.rename(columns={'A': 'Column_Alpha', 'B': 'Column_Beta'})
print("\nDataFrame with renamed columns:\n", df_renamed_cols)

# Rename index
df_renamed_index = df_rename.rename(index={'row_x': 'Index_X', 'row_y': 'Index_Y'})
print("\nDataFrame with renamed index:\n", df_renamed_index)

# Rename both
df_renamed_all = df_rename.rename(columns={'A': 'Col_A_New', 'B': 'Col_B_New'},
                                  index={'row_x': 'Idx_X_New', 'row_y': 'Idx_Y_New'})
print("\nDataFrame with renamed columns and index:\n", df_renamed_all)

# Set index name and columns name
df_rename.index.name = 'MyIndex'
df_rename.columns.name = 'MyColumns'
print("\nDataFrame with index and columns names set:\n", df_rename)


# Combining DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                   index=[0, 1, 2])

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5']},
                   index=[3, 4, 5])

df3 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']},
                   index=[0, 1, 2])

df4 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                    'value_left': ['L0', 'L1', 'L2']})

df5 = pd.DataFrame({'key': ['K0', 'K1', 'K3'], # Note K3 instead of K2
                    'value_right': ['R0', 'R1', 'R3']})


# concat() - Stacks DataFrames vertically or horizontally
# Vertical concatenation (axis=0, default)
df_concat_vertical = pd.concat([df1, df2])
print("\nVertical Concatenation (df1, df2):\n", df_concat_vertical)

# Horizontal concatenation (axis=1) - aligns on index
df_concat_horizontal = pd.concat([df1, df3], axis=1)
print("\nHorizontal Concatenation (df1, df3):\n", df_concat_horizontal)

# merge() - SQL-style joins based on common columns or indices
# Inner join (default) - keeps only matching keys
df_merged_inner = pd.merge(df4, df5, on='key', how='inner')
print("\nInner Merge on 'key' (df4, df5):\n", df_merged_inner)

# Left join - keeps all keys from left DataFrame (df4)
df_merged_left = pd.merge(df4, df5, on='key', how='left')
print("\nLeft Merge on 'key' (df4, df5):\n", df_merged_left)

# Right join - keeps all keys from right DataFrame (df5)
df_merged_right = pd.merge(df4, df5, on='key', how='right')
print("\nRight Merge on 'key' (df4, df5):\n", df_merged_right)

# Outer join - keeps all keys from both DataFrames
df_merged_outer = pd.merge(df4, df5, on='key', how='outer')
print("\nOuter Merge on 'key' (df4, df5):\n", df_merged_outer)

# join() - Combines DataFrames based on index or key column (convenience method, often uses merge internally)
df_left_join = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                             'B': ['B0', 'B1', 'B2']},
                            index=['K0', 'K1', 'K2'])
df_right_join = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                              'D': ['D0', 'D2', 'D3']},
                             index=['K0', 'K2', 'K3'])

# Join based on index (default)
df_joined_index = df_left_join.join(df_right_join, how='inner') # Default is left join
print("\nInner Join on Index (df_left_join, df_right_join):\n", df_joined_index)

df_joined_index_outer = df_left_join.join(df_right_join, how='outer')
print("\nOuter Join on Index (df_left_join, df_right_join):\n", df_joined_index_outer)


print("\n" + "="*30)
print("Lesson 4 Pandas Demo Complete.")
print("="*30 + "\n")


# %%
