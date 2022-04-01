import requests



# import json
# json_string = """{
#     "Dan": [
#         20,
#         "London",
#         13242252
#     ],
#     "Maria": [
#         25,
#         "Madrid",
#         34232424
#     ]
# }"""
#
# obj = json.loads(json_string)
# print(type(obj))
# print(obj)


# import json
# friends = {
# 	"Miro": (20, "Poprad", 4219478254321),
# 	"Alzbeta": (21, "Trstena", 4219254321587),
# 	"Fero": (35, "Podhorany", 421587698745)
# }
#
# with open('friends.json', 'wt') as f:
# 	json.dump(friends, f, indent=4)
#
# json_string = json.dumps(friends , indent=4)
# print(json_string)
#
#
# with open('friends.json') as f:
# 	obj = json.load(f)
#
# 	print(type(obj))
# 	print(obj)

# import pickle
#
# friends = {"Miro": [20, "Poprad", 4219478254321], "Alzbeta": [21, "Trstena", 4219254321587],}
#
# with open('friends.dat', 'wb') as f:
# 	pickle.dump(friends, f)
#
#
# with open('friends.dat', 'rb') as f:
# 	obj = pickle.load(f)
# 	print(type(obj))
# 	print(obj)


# import csv
#
# people = [
# 	['Dan', 34, 'Košice'],
# 	['Andrej', 21, 'Bratislava'],
# 	['Maria', 45, 'Poprad']
# ]
#
#
# with open('people2.csv', 'w') as f:
# 	writer = csv.writer(f, delimiter=':')
# 	for item in people:
# 		writer.writerow(item)
# with open('people2.csv', 'r') as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		print(row)

# with open('american-english.txt') as f:
# 	words = f.read().splitlines()
#
# 	words_and_length = dict()
# 	for w in words:
# 		words_and_length[w] = len(w)
#
# 	for k, v in words_and_length.items():
# 		print(f'{k} -> {v}')
#
#





# def wc(file):
# 	with open(file, 'r') as f:
# 		content = f.read().splitlines()
#
# 		lines = len(content)
#
# 		words = 0
# 		for line in content:
# 			words += len (line.split())
#
# 		chars = 0
# 		for line in content:
# 			chars += len(list(line))
#
# 			return lines, words, chars
# print(wc('sample_file.txt'))

		# last = content[len(content) - n:]
		# my_str = '\n'.join(last)
		# return my_str

# with open('banking.txt', 'r') as f:
# 	content = f.read().splitlines()
# 	deposit, withdrawal = 0,0
# 	for item in content:
# 		tmp = item.split(':')
# 		if tmp[0] == 'D':
# 			deposit += int(tmp[1])
# 		elif tmp[0] == 'W':
# 			withdrawal += int(tmp[1])
# 		else:
# 			print('File format error')
# 	balance = deposit - withdrawal
# 	print(balance)


