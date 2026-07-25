
import pandas as pd
import numpy as np



# Set seed for reproducibility
np.random.seed(42)

# 1. CREATING DATAFRAMES
print("\n1. CREATING DATAFRAMES")
print("-"*40)

# From dictionary of lists
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']
})
print("From dictionary:")
print(df1)

# From list of dictionaries
df2 = pd.DataFrame([
    {'Name': 'Alice', 'Score': 85},
    {'Name': 'Bob', 'Score': 92},
    {'Name': 'Charlie', 'Score': 78}
])
print("\nFrom list of dictionaries:")
print(df2)

# From NumPy array
np_data = np.random.randint(30, 100, size=(10, 3))
df3 = pd.DataFrame(np_data, columns=['Math', 'Reading', 'Writing'])
print("\nFrom NumPy array (10 students, 3 subjects):")
print(df3)

# Load from CSV ()
# df = pd.read_csv('student_data.csv')

# 2. DATAFRAME ATTRIBUTES & INFO
print("\n2. DATAFRAME ATTRIBUTES & INFO")
print("-"*40)

print(f"Shape: {df3.shape}")
print(f"Columns: {df3.columns}")
print(f"Index: {df3.index}")
print(f"Size: {df3.size}")
print(f"Data types: {df3.dtypes}")
print(f"Number of dimensions: {df3.ndim}")

print("\n.info():")
print(df3.info())

print("\n.describe():")
print(df3.describe())

print("\n.head() (first 3 rows):")
print(df3.head(3))

print("\n.tail() (last 2 rows):")
print(df3.tail(2))

# 3. INDEXING WITH loc & iloc
print("\n3. INDEXING WITH loc & iloc")
print("-"*40)

# Create a richer dataset
students = pd.DataFrame({
    'Name': [f'Student_{i}' for i in range(1, 11)],
    'Math': np.random.randint(40, 100, 10),
    'Science': np.random.randint(40, 100, 10),
    'English': np.random.randint(40, 100, 10),
    'Attendance': np.round(np.random.uniform(70, 100, 10), 1)
})
print("Student Dataset:")
print(students)

# Position-based (iloc)
print("\n.iloc[0] (first row):")
print(students.iloc[0])
print("\n.iloc[2:5] (rows 2-4):")
print(students.iloc[2:5])
print("\n.iloc[:, 1:3] (columns 1-2):")
print(students.iloc[:, 1:3])
print("\n.iloc[0, 1] (row 0, col 1):", students.iloc[0, 1])

# Label-based (loc)
print("\n.loc[0] (row with index 0):")
print(students.loc[0])
print("\n.loc[1:4, ['Name', 'Math']] (rows 1-4, specific columns):")
print(students.loc[1:4, ['Name', 'Math']])
print("\n.loc[:, 'Math':'English'] (all rows, columns Math to English):")
print(students.loc[:, 'Math':'English'])

# 4. BOOLEAN FILTERING
print("\n4. BOOLEAN FILTERING")
print("-"*40)

# Single condition
top_math = students[students['Math'] >= 80]
print(f"Students with Math >= 80:\n{top_math}")

# Multiple conditions (AND)
high_achievers = students[(students['Math'] >= 80) & (students['Science'] >= 80)]
print(f"\nHigh achievers (Math >= 80 AND Science >= 80):\n{high_achievers}")

# Multiple conditions (OR)
at_risk = students[(students['Math'] < 50) | (students['Science'] < 50) | (students['English'] < 50)]
print(f"\nAt-risk students (any subject < 50):\n{at_risk}")

# Using .query() method
query_filter = students.query('Math > 70 and Attendance > 85')
print(f"\nUsing .query() - Math > 70 and Attendance > 85:\n{query_filter}")

# Using .isin()
selected_students = students[students['Name'].isin(['Student_1', 'Student_3', 'Student_5'])]
print(f"\nSelected students by name:\n{selected_students}")

# 5. ADDING & MODIFYING COLUMNS
print("\n5. ADDING & MODIFYING COLUMNS")
print("-"*40)

# Add a new column (vectorized)
students['Total'] = students['Math'] + students['Science'] + students['English']
students['Average'] = students['Total'] / 3
print("Added 'Total' and 'Average' columns:")
print(students[['Name', 'Math', 'Science', 'English', 'Total', 'Average']].head())

# Add a column with conditional logic (.apply)
def assign_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

students['Grade'] = students['Average'].apply(assign_grade)
print("\nAdded 'Grade' column using .apply():")
print(students[['Name', 'Average', 'Grade']].head())

# Add a column using lambda
students['Passed_Math'] = students['Math'].apply(lambda x: 'Yes' if x >= 60 else 'No')
print("\nAdded 'Passed_Math' column with lambda:")
print(students[['Name', 'Math', 'Passed_Math']].head())

# Add a column using .loc (assign to specific rows)
students.loc[students['Average'] >= 80, 'Honors'] = 'Yes'
students['Honors'] = students['Honors'].fillna('No')
print("\nAdded 'Honors' column (Yes if Average >= 80):")
print(students[['Name', 'Average', 'Honors']].head())

# 6. GROUPBY AGGREGATIONS
print("\n6. GROUPBY AGGREGATIONS")
print("-"*40)

# Add a 'Grade_Level' column
students['Grade_Level'] = np.random.choice(['9th', '10th', '11th', '12th'], size=len(students))

print("Data with Grade_Level:")
print(students[['Name', 'Grade_Level', 'Math', 'Science', 'English', 'Average']].head())

# Single aggregation
grade_avg = students.groupby('Grade_Level')['Average'].mean().round(2)
print(f"\nAverage score by Grade Level:\n{grade_avg}")

# Multiple aggregations on one column
grade_stats = students.groupby('Grade_Level')['Average'].agg(['mean', 'min', 'max', 'std']).round(2)
print(f"\nStatistics by Grade Level:\n{grade_stats}")

# Multiple aggregations on multiple columns
subject_stats = students.groupby('Grade_Level')[['Math', 'Science', 'English']].mean().round(2)
print(f"\nSubject averages by Grade Level:\n{subject_stats}")

# Group by multiple columns
grouped = students.groupby(['Grade_Level', 'Honors'])['Average'].mean().round(2)
print(f"\nAverage score by Grade Level AND Honors status:\n{grouped}")

# Using .agg() with custom functions
def range_calc(x):
    return x.max() - x.min()

custom_agg = students.groupby('Grade_Level').agg({
    'Math': ['mean', 'std', range_calc],
    'Science': ['mean', 'std', range_calc]
}).round(2)
print(f"\nCustom aggregations:\n{custom_agg}")

# 7. GROUPBY WITH TRANSFORM & FILTER
print("\n7. GROUPBY WITH TRANSFORM & FILTER")
print("-"*40)

# .transform() - returns same shape
students['Avg_by_Level'] = students.groupby('Grade_Level')['Average'].transform('mean').round(2)
print("Added 'Avg_by_Level' (mean of grade level):")
print(students[['Name', 'Grade_Level', 'Average', 'Avg_by_Level']].head())

# .filter() - keep only groups that meet a condition
filtered_groups = students.groupby('Grade_Level').filter(lambda x: x['Average'].mean() > 75)
print(f"\nGroups with average > 75 (keeps all rows from those groups):")
print(filtered_groups[['Name', 'Grade_Level', 'Average']].head())

# 8. MERGING & JOINING DATAFRAMES
print("\n8. MERGING & JOINING")
print("-"*40)

# Create two related DataFrames
grades_df = pd.DataFrame({
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Grade': ['A', 'B', 'A', 'C', 'B']
})

attendance_df = pd.DataFrame({
    'Student_ID': [1, 2, 3, 4, 5],
    'Attendance_%': [95, 88, 92, 75, 80]
})

print("Grades DataFrame:")
print(grades_df)
print("\nAttendance DataFrame:")
print(attendance_df)

# Inner join (default)
merged_inner = pd.merge(grades_df, attendance_df, on='Student_ID')
print(f"\nInner Join (only matching IDs):\n{merged_inner}")

# Left join
merged_left = pd.merge(grades_df, attendance_df, on='Student_ID', how='left')
print(f"\nLeft Join:\n{merged_left}")

# Concatenating vertically
more_students = pd.DataFrame({
    'Student_ID': [6, 7],
    'Name': ['Frank', 'Grace'],
    'Grade': ['A', 'D']
})

concat_df = pd.concat([grades_df, more_students], ignore_index=True)
print(f"\nConcatenated vertically:\n{concat_df}")

# 9. HANDLING MISSING DATA
print("\n9. HANDLING MISSING DATA")
print("-"*40)

# Create DataFrame with NaN
df_with_nan = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, np.nan, 78, 92, 88],
    'Science': [90, 88, np.nan, 85, 95],
    'English': [78, 92, 88, np.nan, 85]
})
print("DataFrame with NaN:")
print(df_with_nan)

print(f"\nIs null?:\n{df_with_nan.isnull()}")

# Check for any nulls per column
print(f"\nNull count per column:\n{df_with_nan.isnull().sum()}")

# Drop rows with any NaN
print(f"\nDrop rows with any NaN:\n{df_with_nan.dropna()}")

# Drop columns with any NaN
print(f"\nDrop columns with any NaN:\n{df_with_nan.dropna(axis=1)}")

# Fill NaN with specific values
print(f"\nFill NaN with mean of column:\n{df_with_nan.fillna(df_with_nan.mean())}")

# Fill NaN with forward fill
print(f"\nForward fill:\n{df_with_nan.fillna(method='ffill')}")

# Fill NaN with backward fill
print(f"\nBackward fill:\n{df_with_nan.fillna(method='bfill')}")

# 10. APPLYING FUNCTIONS TO ROWS/COLUMNS
print("\n10. APPLYING FUNCTIONS")
print("-"*40)

# Apply to columns (axis=0)
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})
print("Original DataFrame:")
print(df)

# Apply sum to each column
print(f"\nSum of each column:\n{df.apply(np.sum, axis=0)}")

# Apply sum to each row
print(f"\nSum of each row:\n{df.apply(np.sum, axis=1)}")

# Apply custom function to each row
def row_range(row):
    return row.max() - row.min()

print(f"\nRange (max-min) of each row:\n{df.apply(row_range, axis=1)}")

# Apply to a single column
df['A_squared'] = df['A'].apply(lambda x: x ** 2)
print(f"\nAdded 'A_squared' column:\n{df}")

# 11. LOOPS & ITERATION
print("\n11. LOOPS & ITERATION")
print("-"*40)

# Using .iterrows() - loop through rows
print("Iterating through rows with .iterrows():")
for idx, row in students.head(3).iterrows():
    print(f"  Row {idx}: {row['Name']} scored {row['Average']:.2f} - Grade: {row['Grade']}")

# Using .itertuples() - faster than iterrows
print("\nUsing .itertuples():")
for row in students.head(3).itertuples():
    print(f"  {row.Name} - Math: {row.Math}, Science: {row.Science}, English: {row.English}")

# Using .apply() to loop (faster)
students['Summary'] = students.apply(
    lambda row: f"{row['Name']} (Avg: {row['Average']:.1f}%) - {row['Grade']}",
    axis=1
)
print("\nAdded 'Summary' column using .apply():")
print(students[['Name', 'Summary']].head(3))

# List comprehension with DataFrame values
names_above_80 = [name for name, avg in zip(students['Name'], students['Average']) if avg >= 80]
print(f"\nList comprehension: Students with Average >= 80: {names_above_80}")

# 12. SORTING & RANKING
print("\n12. SORTING & RANKING")
print("-"*40)

print(f"Sort by Average (descending):\n{students.sort_values('Average', ascending=False)[['Name', 'Average']].head()}")

print(f"\nSort by Grade_Level then Average:\n{students.sort_values(['Grade_Level', 'Average'], ascending=[True, False])[['Name', 'Grade_Level', 'Average']].head()}")

# Rank
students['Rank'] = students['Average'].rank(ascending=False, method='dense')
print(f"\nRank by Average:\n{students[['Name', 'Average', 'Rank']].sort_values('Rank').head()}")

# 13. FINAL SUMMARY
print("\n" + "="*60)
print("FINAL SUMMARY")
print("="*60)

print(f"Total Students: {len(students)}")
print(f"Overall Average: {students['Average'].mean():.2f}")
print(f"Grade Distribution:")
print(students['Grade'].value_counts().sort_index())
print(f"Honors Students: {students[students['Honors'] == 'Yes'].shape[0]}")
print(f"At-Risk (Avg < 60): {students[students['Average'] < 60].shape[0]}")

