# write a program to demonstrate the binary search algorithm
a=[1,2,3,4,5,6,7]
key=4
# low,high=0,len(a)-1
# flag=0
# while low<=high:
#     mid=(low+high)//2
#     if a[mid]==key:
#         flag=1
#         break
#     elif key>a[mid]:
#         low=mid+1
#     else:
#         high=mid-1
# if flag==1:
#     print('element found at', mid)
# else:
#     print('element is not found')

#write a program to demonstrate to binary search by recuerssion function in sorted collection
a=[1,2,3,4,5,6,7,8,9]
def binary_search(key,coll,low=0,high=0):
    if high==0 or high>len(coll):
        high=len(coll)-1
    mid = (low + high) // 2
    if a[mid] == key:
        return mid
    elif key > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    return binary_search(key, coll, low, high)

print(binary_search(10,a,1,7))

