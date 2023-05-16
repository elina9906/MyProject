import numpy as np
import pandas as pd
import collections
import openpyxl


a = 'Карл у Клары украл коралы, Клара у Карла украла Кларнет '
b = 'На дворе трава на траве дрова Не руби дрова на траве двора'
c = 'Ехал Гpека чеpез pеку видит Гpека в pеке pак Сунул Гpека pуку в pеку pак за pуку Гpеку цап'

words_A = a.split()
words_B = b.split()
words_C = c.split()
counterA = collections.Counter(words_A)
counterB = collections.Counter(words_B)
counterC = collections.Counter(words_C)
m_c_A = counterA.most_common()[0]
m_c_B = counterB.most_common()[0]
m_c_C = counterC.most_common()[0]
#print(m_c_A, m_c_B, m_c_C)

df1 = pd.DataFrame(m_c_A)
df2 = pd.DataFrame(m_c_B)
df3 = pd.DataFrame(m_c_C)
df4 = pd.concat([df1, df2, df3], axis=1)
df4.to_excel("test.xlsx")

