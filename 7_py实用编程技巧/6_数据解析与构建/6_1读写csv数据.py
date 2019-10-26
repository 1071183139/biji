# import csv
# with open('eggs.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



# import csv
# with open('eggs.csv', 'r') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


# import csv
#
# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name1', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name1': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name1': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name1': 'Wonderful', 'last_name': 'Spam'})


import csv

headers = ['name', 'age', 'six']
data = [
    ('张三', '21', '男'),
    ('张四', '22', '男')
]
with open('ceshi.csv', 'w', encoding='gbk') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(headers)
    for i in data:
        writer.writerow(i)

with open('ceshi.csv', 'r', encoding='gbk') as f:
    reader = csv.reader(f)
    next(reader)
    for book in reader:
        print(book)










#
# import csv
# with open('ceshi.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['name'], row['age'])