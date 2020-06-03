
# 비만도 계산 방법...BMI지수= 몸무게(kg) ÷ (신장(m) × 신장(m))

import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Python37_Project\\20200603\\student.csv")
# print(data)
print(data['weight'] / data['height'])
filter = data['sex'] == 'male'
df_male = data[filter]
filter2 = data['sex'] == 'female'
df_female = data[filter2]
print(df_male)
print(df_female)
data['bmi'] = 2 * 2 * 10
print(data)




