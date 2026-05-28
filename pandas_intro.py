import pandas as pd

df = pd.read_csv('students.csv')
print(df)
print(df.head(3))
print(df.tail(2))
print(len(df))
print(df[df['Math_Grade'] == df['Math_Grade'].max()])
print(df[df['Math_Grade'] == df['Math_Grade'].min()])
print(df.sort_values('Math_Grade', ascending=True))
print(df.sort_values('Science_Grade', ascending=True))
print(df)
print(df.sort_values('Math_Grade', ascending=True))
df['Average'] = (df['Math_Grade'] + df['Science_Grade']) / 2
print(df.loc[df['Average'].idxmin()])


import pandas as pd

df = pd.read_csv('students.csv')
top = df[df['Math_Grade'] == df['Math_Grade'].max()]
lowest = df[df['Math_Grade'] == df['Math_Grade'].min()]
failing = df[df['Math_Grade'] < 80]
print(df)
print()
print(f'Top student:\n {top}')
print()
print(f'Lowest student:\n {lowest}')
print()
print(f'Math average: {df["Math_Grade"].mean():.2f}')
print(f'Science average: {df["Science_Grade"].mean():.2f}')
print()
print(f'Failing students:\n {failing}')

import pandas as pd

df = pd.read_csv('students.csv')
top = df[df['Math_Grade'] == df['Math_Grade'].max()]
lowest = df[df['Math_Grade'] == df['Math_Grade'].min()]
math_average = f'Math average: {df['Math_Grade'].mean():.2f}'
science_average = f'Science average: {df['Science_Grade'].mean():.2f}'
failing =df[df['Math_Grade'] < 80]

import pandas as pd

df = pd.read_csv('employees.csv')
df['Annual_Bonus'] = df['Salary'] * 0.10
df.to_csv('employees_with_bonus.csv', index=False)
df = df.drop(columns=['Annual_Bonus'])
highest = df[df['Salary'] == df['Salary'].max()]
average_salary = f'Average salary: {df['Salary'].mean():.2f}'
engineering_employees = df[df['Department'] == 'Engineering']
four_years_experience = df[df['Years_Experience'] > 3]

print(df)
print()
print(highest)
print()
print(average_salary)
print()
print(engineering_employees)
print()
print(four_years_experience)
print()
print('Saved!')

import pandas as pd

df = pd.read_csv('employees.csv')
result = df.groupby('Department')['Salary'].mean()
print(df.groupby('Department')['Salary'].sum())
print(df.groupby('Department').agg({'Salary': 'mean', 'Years_Experience': 'mean'}))
print(result.round(2))