# myFile=open('helloworld.txt','w')
# myFile.close()
# try:
#     myFile=open('helloworld.txt','w')
#     try:
#         print('Работа с файлом')
#     finally:
#         myFile.close()
# except Exception as ex:
#     print(ex)

# with open('Python47','w') as myFile:
#     print('Работает с файлом Python47')
# with open('python471','w') as file:
#     file.write('Something')
# print('Файл записан')
# with open('python471','a') as file:
#     file.write('\nSomething new')
# print('Файл записан')
# list=['Ilya\n','Regina\n','Artem']
# with open('python471','a') as file:
#     file.writelines(list)
# with open('python471','r') as file:
#     for line in file:
#         print(line,end='-')
# with open('python471','r') as file:
#     str1=file.readline()
#     print(str1)
#     str2=file.readline()
#     print(str2)
# with open('python471','r',encoding='utf8') as file:
#     content=file.readlines()
#     str1=content[0]
#     str2=content[1]
#     print(str1,str2)

# value=input('Введите ключ нужной функции: w,r,a')
# if value=='w':
#     value_w1=input('Введите название файла:')
#     value_w2=input('Введите что нужно записать:')
#     with open(value_w1, 'w') as file:
#         file.write(value_w2)
# elif value=='r':
#     value_r1=input('Введите название файла:')
#     with open(value_r1, 'r') as file:
#         value_read=file.read()
#         print(value_read)
# elif value=='a':
#     value_a1=input('Введите название файла:')
#     value_a2=input('Введите что нужно записать:')
#     with open(value_a1, 'a') as file:
#         file.write(value_a2)
# else:
#     print('Неверный ключ')

# with open('hello.txt','w+') as file:
#     file.write('Hello\n hello')
#     file.seek(0)
#     content=file.read()
#     print(content)

import csv
filename='user.csv'
user=[
    ['Ilya',19],
    ['Egor',5],
    ['Artem',18]
]
with open(filename, 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(user)
with open(filename,'a',newline='') as file:
    user =['Regina',18]
    writer=csv.writer(file)
    writer.writerow(user)