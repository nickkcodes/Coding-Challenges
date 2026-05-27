import pandas as pd

df = pd.read_csv('students_2.csv')
df['Average'] = (df['Math'] + df['Science'] + df['English'] + df['PE']) /4
highest_oa = df[df['Average'] == df['Average'].max()]
failing = df[df['Average'] < 75]
high_low = df.sort_values('Average', ascending=False)
df.to_csv('students_report.csv', index=False)

print(df)
print()
print(f'Highest overall average: \n{highest_oa}')
print()
print(f'Failing below 75 average: \n{failing}')
print()
print(f'Highest to lowest: \n{high_low}')
print()
print('Saved!')
