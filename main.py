import os
os.chdir('files')
# удаляется результат предыдущего запуска (если первый запуск - печатается пустая строка)
try:
    os.remove('result.txt')
except FileNotFoundError:
    print()

# получаем словарь (название файла - кол-во строк)
files_list=os.listdir()
files_dict={}
for my_file in files_list:
    with open(my_file, encoding='utf-8') as f:
        len_count = 0
        for line in f.readlines():
            len_count+=1
        files_dict[my_file] = len_count 

# сортировка словаря с файлами по кол-ву строк
sorted_files_dict = {}
sorted_keys = sorted(files_dict, key=files_dict.get)
for w in sorted_keys:
    sorted_files_dict[w] = files_dict[w]
print(sorted_files_dict)

# собираем результат, используя отсортированный словарь
with open('result.txt', 'a', encoding='utf-8') as f:
    for file in sorted_files_dict:
        text_len = sorted_files_dict.get(file)
        f.write(f'{file}\n{text_len}\n')
        with open (file, encoding='utf-8') as ff:
            for line in ff.readlines():
                f.write(f'{line}\n')

