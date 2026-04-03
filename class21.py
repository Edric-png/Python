# list1 = []
# list2 = [1,2,3,4]
# list3 = [1,2,3,4]*2
# list4 = list2[::-1]
# print(list1,list2,list3,list4)
# def match_words(words):
#     ctr = 0
#     lst = []
#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             ctr += 1
#             lst.append(word)
#     print("List of words with first and last character same\n", lst)
#     return ctr
# count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
# print("Number of words having first and last character same:", count)
list1 = [12,43,72,91,58]
count = 0
for i in list1:
    count += i
avg = count/len(list1)
print(avg)
list1.sort()
print(list1)