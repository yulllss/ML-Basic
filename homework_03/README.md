# Домашнее задание: Функции
## Занятие: Функции. Часть 1

* Будем работать в директории `homework_03`
* Используйте нотбук `homework_03.ipynb` для выполнения задания

<br>

## Задание 1: Конвертер регистров

Написать функцию, которая будет переводить snake_case в PascalCase и наоборот. 

Функция должна сама определять - какой формат ей передали. Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.

<br>

**Примеры:**
* `otus_course     -> OtusCourse`
* `PythonIsTheBest -> python_is_the_best`

<br>

## Задание 2: Проверка валидности даты

Написать функцию проверяющую валидность введенной даты.

<br>

**Примеры:**
* `29.02.2000 -> True`
* `29.02.2001 -> False`
* `31.04.1962 -> False`

<br>

## Задание 3: Проверка на простое число

Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.

<br>

**Примеры:**
* `17 -> True`
* `20 -> False`
* `23 -> True`

<br>

## Задание 4: Учет пользователей

Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID. Ввод продолжается до тех пор, пока не будет введено пустое поле. 

Пользователи заносятся в словарь, где ключ это ID пользователя, а остальные данные записываются в виде кортежа. 

**Программа должна проверять:**
* имя и фамилия состоят только из символов и начинаются с большой буквы - если не с большой, то заменяет букву на большую;
* возраст должен быть числом от 18 до 60;
* ID - целое число, дополненное до 8 знаков незначащими нулями, ID должен быть уникальным.

**Дополнительно:** написать функцию, которая будет выводить полученный словарь в виде таблицы.