import pandas as pd
#print("\nТаблица успеваемости студентов:")
sap = {'ID': ['256', '384', '546', '132', '11', '78', '36'],
    'History': ['5', '3', '3', '4', '5', '3', '5'],
    'Maths': ['4', '3', '4', '5', '4', '4', '4'],
    'Physics': ['4', '3', '5', '4', '4', '3', '5'],
    'Chemistry': ['3', '3', '4', '4', '5', '5', '5'],
    'Percentage': ['91.2 %', '63.5 %', '90.23 %', '92.7 %', '98.2 %', '88.1 %', '95.0 %'],
    }
df = pd.DataFrame(data=sap)
# print(df)
