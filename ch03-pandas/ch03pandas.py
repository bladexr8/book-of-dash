import pandas as pd

# create simple series object
# s = pd.Series([42, 21, 7, 3.5])
# print(s)

# create a DataFrame
df = pd.DataFrame({'age': 18,
                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]})
print('Printing DataFrame...')
print(df)

# select a column
print('\nSelecting a DataFrame Column...')
print(df['age'])

# select by index and slice
print('\nSelecting one row by index/slice...')
print(df[2:3])

# access third row and second column
print('\nSelecting third row, second column...')
print(df.iloc[2, 1])

# access rows where cardio > 60
print('\nSelecting cardio > 60...')
print(df[df['cardio'] > 60])

# access column by label
print('\nSelecting column by label...')
print(df.loc[:, 'name'])

# access multiple columns by label
print('\nSelecting multiple columns by label...')
print(df.loc[:, ['age', 'cardio']])

# modify a column
print('\nModify a column...')
df['age'] = 16
print(df)

# add a column
print('\nAdding a column...')
df['friend'] = 'Alice'
print(df)


# rebuild DataFrame and modify 2nd & 3rd columns
df2 = pd.DataFrame({'age': 18,
                    'name': ['Alice', 'Bob', 'Carl'],
                    'cardio': [60, 70, 80]})
print('\nModify a column in 2nd & 3rd rows only...')
df2.loc[1:, 'age'] = 16
print(df2)



