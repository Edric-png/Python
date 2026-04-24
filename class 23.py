# student_data = {
#     "id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
# "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
# "id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
# "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
# }
# result = {}
# seen_keys = []
# for student_id, details in student_data.items():
#     unique_key = (details["name"], details["class"], details["subject_integration"])
#     if unique_key not in seen_keys:
#         seen_keys.append(unique_key)
#         result[student_id] = details
# for k, v in result.items():
#     print(k, ":", v)
# test_dict = {'Coding' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coded' : 1}
# print("The original dictionary : " + str(test_dict))
# K = 2
# res = 0
# for key in test_dict:
#     if test_dict[key] == K:
#         res = res + 1
# print("Frequency of K is : " + str(res))
country_code = {'India' : '0091',
'Australia' : '0025',
'Nepal' : '00977'}
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
