# 1.regular expression
# 2.dictionary sort 
# 3.['sarthak','sachan','python','sarthak','sachan']>>{}
# 4. with open how to print all data of file
# 5. class self


class Phone:
    def tuv(self):
        print('this is tuv parent')

    def pqrst(self):
        print('this is parent function')
        self.tuv()

class Mobile(Phone):
    def tuv(self):
        print('this is tuv child function')

p1=Mobile()
p1.pqrst()

# student2=[
    #     {'score':90,'age':25},
    #     {'score':60,'age':24},
    #     {'score':500,'age':20}
    # ]


# print(sorted(student2, key=lambda a:a['score'],reverse=True))
# print(sorted(student2,key=lambda g: g['score'],reverse=True))

# a={'a':12,'b':55,'e':3,'d':15}
# print({k:v for k,v in sorted(a.items(),key=lambda v: v)})
# print(sorted(a,key=lambda d:d[]))
# sortedbyKey= {k:v for k,v in sorted(a.items())}
# sortedbyValue= {k:v for k,v in sorted(a.items(), key=lambda v:v[1])}
# print(sortedbyKey)
# print(sortedbyValue)