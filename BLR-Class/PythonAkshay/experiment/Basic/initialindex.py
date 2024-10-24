# WAP to get the initial index of particular charcter in a string between the limits
# def index1(key,string,start_index=0,end_index=0):
#     if end_index==0:
#         end_index=len(string)
#     if key in string[start_index:end_index]:
#         for i in range(start_index,end_index):
#             if string[i]==key:
#                 return i
#     return None
# print(index1("l","dsaaldksjglsdcghsklll",5))
                
# def index1(key,string,start_index=0,end_index=0):
#     if end_index==0:
#         end_index=len(string)
#     flag=0
#     if key in string[start_index:end_index]:
#         for i in range(start_index,end_index):
#             if string[i]==key:
#                 flag=1
#                 break
#         if flag==1:
#             return i
#         return None
# print(index1("l","dsaaldksjglsdcghsklll",5))


def index1(key,string,start_index=0,end_index=0):
    if end_index==0:
        end_index=len(string)
    flag=0
    if key in string[start_index:end_index]:
        for i in range(start_index,end_index):
            if string[i]==key:
                flag+=1
                if flag==2:
                    break
        if flag==2:
            return i
        return None
print(index1("l","dsaaldksjglsdcghsklll",5))
                




