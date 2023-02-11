import pandas

jobs = pandas.read_csv("data_analyst.csv")
# print(jobs)
# print(jobs.columns)  # sloupce tabulky
# print(len(jobs))
print(jobs.iloc[10])
print(jobs.iloc [12:21,6])