def count(Key,String,Start_index=0,end_index=0):
    if end_index==0:
        end_index=len(String)
    c=0
    if Key in String[Start_index:end_index]:
        for i in range(Start_index,end_index):
            if Key==String[i]:
                c+=1
    return c
print(count("l","hello world",end_index=5))
