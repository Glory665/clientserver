'''
1. Каждое из слов «разработка», «сокет», «декоратор» представить
 в строковом формате и проверить тип и содержание соответствующих
 переменных. Затем с помощью онлайн-конвертера преобразовать строковые
 представление в формат Unicode и также проверить тип и содержимое переменных
'''

print('*' * 20, 'Задача №1', '*' * 20)

first_word = 'разработка'
second_word = 'сокет'
third_word = 'декоратор'

str_list = [first_word, second_word, third_word]

first_word_unic = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
second_word_unic = '\u0441\u043e\u043a\u0435\u0442'
third_word_unic = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

unic_list = [first_word_unic, second_word_unic, third_word_unic]

for el in unic_list, str_list:
    print(type(el))
    print('#' * 20)


if first_word == first_word_unic and second_word_unic == second_word \
        and third_word_unic == third_word:
    print('true')
else:
    print('false')

print('*' * 20, 'Задача №2', '*' * 20)
##########################################################################
'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе. 
Сделать это необходимо в автоматическом, а не ручном режиме, с помощью 
добавления литеры b к текстовому значению, (т.е. ни в коем случае 
не используя методы encode, decode или функцию bytes) и определить тип, 
содержимое и длину соответствующих переменных.
'''

word1 = 'class'
word2 = 'function'
word3 = 'method'

str_words = [word3, word2, word1]

for el_str in str_words:
    el = eval(f"b'{el_str}'")
    print(el)
    print('el_type: ', type(el))
    print('#' * 20)


print('*' * 20, 'Задача №3', '*' * 20)
##########################################################################
'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» 
невозможно записать в байтовом типе. Важно: решение должно быть 
универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
'''
word_1 = 'attribute'
word_2 = 'класс'
word_3 = 'функция'
word_4 = 'type'

words = [word_4, word_3, word_2, word_1]

for word in words:
    try:
        word.encode('ascii')
    except UnicodeEncodeError:
        print(f'Слово "{word}" нельзя представить в байтовом типе')


print('*' * 20, 'Задача №4', '*' * 20)
##########################################################################

'''
4. Преобразовать слова «разработка», «администрирование», «protocol», 
«standard» из строкового представления в байтовое и выполнить обратное 
преобразование (используя методы encode и decode).
'''
word1 = 'разработка'
word2 = 'администрирование'
word3 = 'protocol'
word4 = 'standard'

words_list = [word4, word3, word2, word1]

result_b = []
for word in words_list:
    word_b = word.encode('utf-8')
    print(word_b)
    result_b.append(word_b)

print()

result_str = []
for word in result_b:
    word_str = word.decode('utf-8')
    result_str.append(word_str)

print(result_str)


print('*' * 20, 'Задача №5', '*' * 20)
##########################################################################
'''
5. Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com 
и преобразовывает результат из байтовового типа данных в строковый 
без ошибок для любой кодировки операционной системы.
'''

import platform
import subprocess
import chardet

urls = ['yandex.ru', 'youtube.com']
param = '-n' if platform.system().lower() == 'windows' else '-c'

for url in urls:
    args = ['ping', param, '4', url]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

print('*' * 20, 'Задача №6', '*' * 20)
##########################################################################
'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». Далее забыть о том, 
что мы сами только что создали этот файл и исходить из того, что перед 
нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК 
вне зависимости от того, в какой кодировке он был создан.
'''

from chardet import detect

# Создаем текстовый файл в "неизвестной" кодировке
Words_List = ['сетевое программирование', 'сокет', 'декоратор']
with open('test.txt', 'w') as f:
    for line in Words_List:
        f.write(f'{line}\n')
f.close()

# Узнаем кодировку "неизвестного файла"
with open('test.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

# открываем файл в известной кодировке
with open('test.txt', 'r', encoding=encoding) as f:
    content = f.read()
print(content)
