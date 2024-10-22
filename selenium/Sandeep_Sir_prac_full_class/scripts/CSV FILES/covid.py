# a=[1,2,3,4]
# print(dir(a))
# print(type(a))
# it=iter(a)
# print(dir(it))
# print(type(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(it.__next__())
import csv
filename='F:\selenium\Sandeep_Sir\scripts\CSV FILES\covid.csv'

#MAKING A TUPLE
def make_tuple(row):
    return row[2],row[3],int(row[5])

#MAKING A DICTIONARY
def make_dict(row):
    return {
        'country': row[2],
        'date':row[3],
        "cases":row[5]
    }

#MAKING A CLASS INSTANCE
class Covid:
    def __init__(self,row):
        self.country=row[2]
        self.date=row[3]
        self.cases=row[5]

# from collections import namedtuple
# Covid=namedtuple("Covid",['country','date','cases'])
def read_csv(filename):
    records=[]
    with open(filename,"r") as f:
        rows= csv.reader(f)
        headers=next(rows)   #skipping headers
        for row in rows:
            # records.append(make_tuple(row))
            # records.append(make_dict(row))
            records.append(Covid(row))
    return records
data=read_csv(filename)
# print(len(data))
# print(data[0].country)
# print(data[2].cases)
# print(data[445].date)
# print(data[34874].country)
#

#  ALL COUNTRIES AFFECTED BY COVID
# c={item.country for item in data}
# print(c)
# print(len(c))


#TOTAL NUMBER OF COVID CASES IN EACH COUNTRY
from collections import Counter
c=Counter()
for item in data:
    c[item.country]+=int(item.cases)

# print(c)
# print(c['India'])

# 10 Top Countries which has most number of Covid Cases
# top_10 = sorted(c.items(), key=lambda item: item[-1])
# print(top_10[-10:])
# Countries with less than 1000 cases
less_1000 = {item.country: item.cases for item in data if int(item.cases) < 1000}
print(less_1000)
# How many cases were reported on  26/07/2020 in India
# dd = Counter()
#
# for item in data:
#     dd[(item.country, item.date_)] += int(item.cases)