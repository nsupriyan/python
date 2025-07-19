# linear search


# arr=[1,2,3,4,5,6]
# ele=3
# def linear(arr,ele):
#     for i in range(len(arr)):
#         if (arr[i]==ele):
#             return True
#     return False
# print(linear(arr,ele))

# arr=[1,2,3,3,3,3,3,4]
# ele=3
# def linn(arr,ele):
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==ele:
#             count+=1
#     return count
# print(linn(arr,ele))

# arr=[1,1,1,1,2,3,4,5]
# ele=1
# index=[]
# def linv(arr,ele):
#     for i in range(len(arr)):
#         if arr[i]==ele:
#             index.append(i)
#     return index
# print(linv(arr,ele))

# arr=[1,2,3,4,5,6,7]
# def lii(arr):
#     max=arr[0]
#     for i in arr:
#         if i>max:
#             max=i
#     return max
# print(lii(arr))

# arr=[1,2,3,4,5,6,7]
# def lii(arr):
#     min=arr[0]
#     for i in arr:
#         if i<min:
#             min=i
#     return min
# print(lii(arr))


# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# target = 8

# def search_2d(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] == target:
#                 return (i, j)
#     return -1

# print(search_2d(arr, target))

# arr=[1,2,3,4,5,6,7,1,7]
# target=1
# for i in range(len(arr)):
#     if arr[i]==target:
#         print([i])
       
# arr = [5, 12, 3, 7, 18]
# K = 6
# for i in arr:
#     if i>K:
#         print([i])

# string = "supriya"
# target = "r"
# for a in range(len(string)):
#     if string[a]==target:
#         print(a)

# arr = [4, 8, 1, 7, 3, 6]
# target=7
# for i in range(1,4):
#     if arr[i]==target:
#         print("found",i)

# arr = [1, 3, 5, 3,2, 4]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print("dulipcate found")

# arr = [2, 4, 7, 9, 6]
# counting = 0   # To count odd numbers
# counter = 0    # To count even numbers

# for i in arr:
#     if i % 2 == 0:
#         counter += 1
#     else:
#         counting += 1

# print("Even count:", counter)
# print("Odd count:", counting)

# arr = [5, 8, 12, 3, 7]
# sort1= sorted(arr, reverse=True)
# second = sort1[1]
# print(second)

# bineary search

# def binfunc(list1, target):
#     left = 0
#     right = len(list1) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if list1[mid] == target:
#             return mid
#         elif list1[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1  # If target not found

# # Example usage:
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binfunc(list1, 9))  # Output will be 9

# Input:
# arr = [1, 3, 5, 7, 9, 11]
# target = 7

# Output:
# 3 (Index of 7 in the list)
# def binse(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# arr = [1, 3, 5, 7, 9, 11]
# print(binse(arr,9))

# Input:
# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2

# Output:
# 1 (First occurrence index of 2)
# def binarysearch_first_occurrence(arr, target): 
#     left = 0
#     right = len(arr) - 1
#     result = -1  # to store the index of first occurrence
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#             result = mid  
#             right = mid - 1      # store current index     # keep looking on the left side
#         elif arr[mid] < target:
#             left = mid + 1
#         # else:
#         #     right = mid - 1
            
#     return result

# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# res = binarysearch_first_occurrence(arr, target)

# if res != -1:
#     print(target, "first occurrence at index", res)
# else:
#     print(target, "not found")

# def binarysearch_last_occurrence(arr, target): 
#     left = 0
#     right = len(arr) - 1
#     result = -1  # to store the index of last occurrence
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#             result = mid  
#             left = mid + 1   # keep looking on the right side for last occurrence
#         # elif arr[mid] < target:
#         #     left = mid + 1
#         else:
#             right = mid - 1
            
#     return result

# # Example usage:
# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# res = binarysearch_last_occurrence(arr, target)

# if res != -1:
#     print(target, "last occurrence at index", res)
# else:
#     print(target, "not found")

# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2

# def first_occ(arr,target):
#     left = 0
#     right = len(arr) - 1
#     result = -1
#     while left<= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             result = mid
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# def last_occ(arr,target):
#     left = 0
#     right = len(arr) - 1
#     result = -1
#     while left<= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             result = mid
#             left = mid + 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# def count_occurrences(arr, target):
#     first = first_occ(arr, target)
#     if first == -1:
#         return 0
#     last = last_occ(arr, target)
#     return last - first + 1
# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# print("Count of", target, "is", count_occurrences(arr, target))

#arr = [1, 3, 5, 7, 9, 11]
# def arrrr(arr,target):
#     left=0
#     right=len(arr)-1
#     result=-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return arr[mid]
#         elif arr[mid]<target:
#             result=arr[mid]
#             left=mid+1
#         else:
#             right=mid-1
# arr = [1, 3, 5, 7, 9, 11]
# target=6
# print(arrrr(arr,target))




# def int_sqrt(num):
#     left = 0
#     right = num
#     result = -1

#     while left <= right:
#         mid = (left + right) // 2

#         if mid * mid == num:
#             return mid
#         elif mid * mid < num:
#             result = mid         # store possible answer
#             left = mid + 1       # try to find larger square root
#         else:
#             right = mid - 1      # move to smaller half

#     return result

# # Example usage:
# num = 10
# print(int_sqrt(num))  # Output: 3

# bubble short
# def bubble(arr):
#     count=0
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j]>arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#                 count+=1
#     print(count)            
#     return arr 
# arr = [4, 3, 2, 1]
# print(bubble(arr))

# def binnn(arr):
#     count=0
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j]<arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#                 count+=1
#     print(count)
#     return arr
# arr=[3,1,4,2]
# print(binnn(arr))

# def binnn(arr,k):
#     for i in range(k-1,0,-1):
#         for j in range(i):
#             if arr[j]>arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#     return arr
# arr = [9, 8, 7, 6, 5, 4, 3]
# k=4
# print(binnn(arr,k))

# arr1=[1,2,3,4]
# def sortb(arr):
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j]>arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#     return arr
# arr = [1, 2, 3, 4, 5]
# print(sortb(arr))
# if arr1==arr:
#     print("same same")
# else:
#     print("but difflent")



# def sortb(arr):
#     count=0
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j]>arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#             # break
#         count+=1
#     print(count)
#     return arr
# arr=[5, 3, 2, 4, 1]
# print(sortb(arr))

#selection shot

# arr=[9,8,7,6,5,4,3,2,1,0]
# for i in range(len(arr)-1):
#     # index=i
#     for j in range(i+1,len(arr)):
#         # index=j
#         if arr[i]>arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
#     print(arr)
# print(arr)

# def ss(arr):
#     for i in range(len(arr)-1):
#         index = i
#         for j in range(i+1,len(arr)):
#              index = j
#              if arr[i]> arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr
# arr=[2,66,88,9,10]
# ss(arr)
# print(arr)

# arr = [5, 4, 3, 2, 1]
# n=len(arr)
# count=0
# for i in range(-1):
#     index=i
#     for j in range(i+1,len(arr)):
#         index=j
#         if arr[i]<arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# count+=1
# print(count)
# # print(arr)

# def selection_sort_count_swaps(arr):
#     swaps = 0
#     for i in range(len(arr)-1):
#         index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[index]:
#                 index = j
#         if index != i:
#             arr[i], arr[index] = arr[index], arr[i]
#             swaps += 1
#     return swaps

# arr = [5, 4, 3, 2, 1]
# print(selection_sort_count_swaps(arr))  # Output: 2

# arr = ["banana", "apple", "cherry", "date"]
# n=len(arr)
# for i in range(n-1):
#     index=i
#     for j in range(i+1,n):
#         if arr[j]<arr[index]:
#             index=j
#             arr[i],arr[index]=arr[index],arr[i]
# print(arr)





# arr = [2, 3, 6,6, 7, 1,1,1]
# count=0

# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):         # go backward from i to 1
#         if arr[j] < arr[j - 1]:       # if current < previous
#             arr[j], arr[j - 1] = arr[j - 1], arr[j] 
#     count+=1
#            # stop if already sorted
# print(arr,count)



# arr = [2, 3, 6,6, 7, 1,1,1]
# count=0

# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):         # go backward from i to 1
#         if arr[j] < arr[j - 1]:       # if current < previous
#             arr[j], arr[j - 1] = arr[j - 1], arr[j] 
#     count+=1
#            # stop if already sorted
# print(arr,count)


arr=[7]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):         # go backward from i to 1
        if arr[j] <arr[j-1]:       # if current < previous
            arr[j], arr[j] = arr[j - 1], arr[j] 
print(arr)













    


   





    
            



        
