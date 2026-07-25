
import pandas as pd
import numpy as np



# 1. CREATING SERIES

print("\n1. CREATING SERIES")
print("-"*40)

# From a list
s1 = pd.Series([10, 20, 30, 40, 50])
print("From list:")
print(s1)

# With custom index
s2 = pd.Series([85, 92, 78, 65, 88], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
print("\nWith custom index:")
print(s2)

# From a dictionary (keys become index)
s3 = pd.Series({'Math': 85, 'Science': 90, 'English': 78, 'History': 92})
print("\nFrom dictionary:")
print(s3)

# From a scalar (repeated)
s4 = pd.Series(5, index=range(5))
print("\nFrom scalar (repeated):")
print(s4)

# From NumPy array
np_arr = np.array([1.5, 2.3, 3.7, 4.1])
s5 = pd.Series(np_arr, index=['a', 'b', 'c', 'd'])
print("\nFrom NumPy array:")
print(s5)

# 2. SERIES ATTRIBUTES

print("\n2. SERIES ATTRIBUTES")
print("-"*40)

print(f"Values (as array): {s2.values}")
print(f"Index: {s2.index}")
print(f"Shape: {s2.shape}")
print(f"Size: {s2.size}")
print(f"Data type: {s2.dtype}")
print(f"Is empty? {s2.empty}")
print(f"Has nans? {s2.hasnans}")
print(f"Number of dimensions: {s2.ndim}")

# 3. INDEXING & SLICING
print("\n3. INDEXING & SLICING")
print("-"*40)

# Position-based indexing (iloc)
print(f"First element (iloc[0]): {s2.iloc[0]}")
print(f"Last element (iloc[-1]): {s2.iloc[-1]}")
print(f"First 3 (iloc[:3]):")
print(s2.iloc[:3])
print(f"Every 2nd (iloc[::2]):")
print(s2.iloc[::2])

# Label-based indexing (loc)
print(f"Alice's score (loc['Alice']): {s2.loc['Alice']}")
print(f"Alice to Charlie (loc['Alice':'Charlie']):")
print(s2.loc['Alice':'Charlie'])
print(f"Specific labels (loc[['Alice', 'Eva']]):")
print(s2.loc[['Alice', 'Eva']])

# Boolean indexing
print(f"Scores > 80:")
print(s2[s2 > 80])

# 4. VECTORIZED OPERATIONS
print("\n4. VECTORIZED OPERATIONS")
print("-"*40)

scores = pd.Series([85, 92, 78, 65, 88], index=['A', 'B', 'C', 'D', 'E'])

# Arithmetic operations
print(f"Original: {scores}")
print(f"Add 5: {scores + 5}")
print(f"Multiply by 2: {scores * 2}")
print(f"Power of 2: {scores ** 2}")
print(f"Square root (np.sqrt): {np.sqrt(scores).round(2)}")
print(f"Log (np.log): {np.log(scores + 1).round(2)}")

# Two series operations
bonus = pd.Series([2, 5, 3, 1, 4], index=['A', 'B', 'C', 'D', 'E'])
print(f"Bonus: {bonus}")
print(f"Scores + Bonus: {scores + bonus}")
print(f"Scores * Bonus: {scores * bonus}")

# 5. BOOLEAN FILTERING
print("\n5. BOOLEAN FILTERING")
print("-"*40)

# Create a series of random scores
student_scores = pd.Series(np.random.randint(30, 100, size=20),
                           index=[f'Student_{i}' for i in range(1, 21)])
print(f"All scores: {student_scores}")

# Single condition
passing = student_scores[student_scores >= 60]
print(f"\nPassing (>=60): {passing}")

# Multiple conditions (AND)
high_and_attending = student_scores[(student_scores >= 80) & (student_scores <= 95)]
print(f"High performers (80-95): {high_and_attending}")

# Multiple conditions (OR)
at_risk = student_scores[(student_scores < 40) | (student_scores > 95)]
print(f"At-risk (<40 or >95): {at_risk}")

# Using .between()
range_filter = student_scores.between(70, 85)
print(f"Between 70-85 (boolean): {range_filter}")
print(f"Values between 70-85: {student_scores[range_filter]}")

# Using .isin()
specific_students = student_scores.isin([85, 90, 95, 100])
print(f"Students with perfect scores (85,90,95,100): {student_scores[specific_students]}")

# 6. STATISTICAL METHODS
print("\n6. STATISTICAL METHODS")
print("-"*40)

print(f"Mean: {student_scores.mean():.2f}")
print(f"Median: {student_scores.median():.2f}")
print(f"Standard Deviation: {student_scores.std():.2f}")
print(f"Variance: {student_scores.var():.2f}")
print(f"Min: {student_scores.min()}")
print(f"Max: {student_scores.max()}")
print(f"Range (max-min): {student_scores.max() - student_scores.min()}")
print(f"25th Percentile: {student_scores.quantile(0.25)}")
print(f"75th Percentile: {student_scores.quantile(0.75)}")
print(f"IQR: {student_scores.quantile(0.75) - student_scores.quantile(0.25)}")
print(f"Sum: {student_scores.sum()}")
print(f"Count (non-null): {student_scores.count()}")
print(f"Number of unique values: {student_scores.nunique()}")

# 7. MISSING DATA HANDLING
print("\n7. MISSING DATA HANDLING")
print("-"*40)

# Create series with NaN values
s_with_nan = pd.Series([10, np.nan, 20, np.nan, 30, 40])
print(f"Series with NaN: {s_with_nan}")

# Check for nulls
print(f"Is null? {s_with_nan.isnull()}")
print(f"Is not null? {s_with_nan.notnull()}")

# Drop NaN
print(f"Drop NaN: {s_with_nan.dropna()}")

# Fill NaN
print(f"Fill with 0: {s_with_nan.fillna(0)}")
print(f"Forward fill: {s_with_nan.fillna(method='ffill')}")
print(f"Backward fill: {s_with_nan.fillna(method='bfill')}")
print(f"Fill with mean: {s_with_nan.fillna(s_with_nan.mean())}")

# 8. APPLYING FUNCTIONS (.apply() & .map())
print("\n8. APPLYING FUNCTIONS")
print("-"*40)

# .apply() - Apply a custom function
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

grades = student_scores.apply(grade)
print(f"Grades: {grades}")

# .map() - Replace values with a dictionary
grade_map = {'A': 'Excellent', 'B': 'Good', 'C': 'Average', 'D': 'Below Average', 'F': 'Fail'}
grade_descriptions = grades.map(grade_map)
print(f"Grade descriptions: {grade_descriptions}")

# .apply() with lambda function
half_scores = student_scores.apply(lambda x: x / 2)
print(f"Half scores: {half_scores.round(2)}")

# 9. SORTING & RANKING
print("\n9. SORTING & RANKING")
print("-"*40)

print(f"Sorted (ascending): {student_scores.sort_values()}")
print(f"Sorted (descending): {student_scores.sort_values(ascending=False)}")
print(f"Sorted by index: {student_scores.sort_index()}")
print(f"Rank (dense): {student_scores.rank(method='dense')}")

# 10. STRING OPERATIONS (.str)
print("\n10. STRING OPERATIONS")
print("-"*40)

names = pd.Series(['  Alice', 'Bob  ', 'Charlie', '   David   '])
print(f"Original: {names}")
print(f"Strip whitespace: {names.str.strip()}")
print(f"Lowercase: {names.str.lower()}")
print(f"Uppercase: {names.str.upper()}")
print(f"Length: {names.str.len()}")
print(f"Contains 'a': {names.str.contains('a')}")

# 11. DATETIME OPERATIONS
print("\n11. DATETIME OPERATIONS")
print("-"*40)

dates = pd.Series(pd.date_range('2024-01-01', periods=10, freq='D'))
print(f"Date range: {dates}")
print(f"Day: {dates.dt.day}")
print(f"Month: {dates.dt.month}")
print(f"Year: {dates.dt.year}")
print(f"Day of week: {dates.dt.day_name()}")

