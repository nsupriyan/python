# # n=6
# # a=''
# # for i in range(1,n+1):
# #     a=i*i
# #     print(a)

# # n=6
# # s=0
# # for i in range(1,n):
# #     if(n%i==0):
# #         s += i
# # print(s)
# # if(s==n):
# #     print("perfect number")
# # else:
# #     print("not")

# # count = 0
# # num = 1

# # while count < 6:
# #     s = 0
# #     for i in range(1, num):
# #         if num % i == 0:
# #             s += i
# #     if s == num:
# #         print(num)
# #         count += 1
# #     num += 1

# # n=10
# # a=n+1
# # i=1
# # is_perfect=False
# # while i*i<=a:
# #     if i*i==a:
# #         is_perfect=True
# #         break
# #     i+=1
# # print(a)
# # if is_perfect:
# #     print("perfect square")
# # else:
# #     print("NO")

# # x, y, z, *res, la1, la2, la3 = [
# #     "apple", "banana",
# #     "grapes", "lemon",
# #     "pineapple", "guava",
# #     "mango", "kiwi",
# #     "orange", "strawberry", "blueberry"
# # ]

# # # print( x)
# # # print( y)
# # # print(z)
# # print(res)
# # # print(la1)
# # # print(la2)
# # # print(la3)
# sentence = input("Enter a sentence: ")

# # Split the sentence into words
# words = sentence.split()

# # Total number of words
# total_words = len(words)

# # Find unique words using set
# unique_words = set(words)
# num_unique = len(unique_words)

# # Frequency of each word
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# # Output
# print("Total number of words:", total_words)
# print("Number of unique words:", num_unique)
# print("Frequency of each word:")
# print(freq)




















