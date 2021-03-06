"""
author: Richard Sherman
2018-12-05
lab15-num-to-phrase.py, converts numbers to numerals (words)
also tries to convert to roman numerals
"""

#version 1, arabic numbers 0-999
numerals = {
            0   : '',
            1   :   'one',
            2   :   'two',
            3   :   'three',
            4   :   'four',
            5   :   'five',
            6   :   'six',
            7   :   'seven',
            8   :   'eight',
            9   :   'nine',
            10  :   'ten',
            11  :   'eleven',
            12  :   'twelve',
            13  :   'thirteen',
            14  :   'fourteen',
            15  :   'fifteen',
            16  :   'sixteen',
            17  :   'seventeen',
            18  :   'eighteen',
            19  :   'nineteen'
            }

tens =      {
            2  :   'twenty',
            3  :   'thirty',
            4  :   'forty',
            5  :   'fifty',
            6  :   'sixty',
            7  :   'seventy',
            8  :   'eighty',
            9  :   'ninety'
            }
print('This program turns numbers into numerals (words). You enter a number, and I\'ll give it to you in words.')
number = int(input('Please enter an integer between 0 and 999 (inclusive): '))
if number < 20:
    word = numerals[number]
elif number > 19 and number < 100:
    word = tens[number // 10] + '-' + numerals[number % 10]
# print(f'\n{number}\t:\t{word}')
elif number > 99:
    if number % 100 < 20:
        word = numerals[number // 100] + ' hundred ' + numerals[number % 100]
    else:
        word = numerals[number // 100] + ' hundred ' + tens[(number % 100) // 10] + '-' + numerals[(number % 100) % 10]
print(word)

#version 2, roman numerals 0-99
romans_1_9 = {
            1   :   'I',
            2   :   'II',
            3   :   'III',
            4   :   'IV',
            5   :   'V',
            6   :   'VI',
            7   :   'VII',
            8   :   'VIII',
            9   :   'IX',

            }

romans_tens =  {
                1   :   'X',
                2   :   'XX',
                3   :   'XXX',
                4   :   'XL',
                5   :   'L',
                6   :   'LX',
                7   :   'LXX',
                8   :   'LXXX',
                9   :   'XC'
                }
print('\nThis program turns numbers into Roman numerals.')
number = int(input('Please enter an integer between 0 and 99 (inclusive): '))
if number < 10:
    word = romans_1_9[number]
elif number > 9 and number < 100:
    word = romans_tens[number // 10] +  romans_1_9[number % 10]
# print(f'\n{number}\t:\t{word}')
print(word)

#version 3, time in xx:xx to words

minutes =   {
            '00'    :   'o\'clock',
            '01'    :   'o-one',
            '02'    :   'o-two',
            '03'    :   'o-three',
            '04'    :   'o-four',
            '05'    :   'o-five',
            '06'    :   'o-six',
            '07'    :   'o-seven',
            '08'    :   'o-eight',
            '09'    :   '0-nine',
            '10'    :   'ten',
            '11'    :   'eleven',
            '12'    :   'twelve',
            '13'    :   'thirteen',
            '14'    :   'fourteen',
            '15'    :   'fifteen',
            '16'    :   'sixteen',
            '17'    :   'seventeen',
            '18'    :   'eighteen',
            '19'    :   'nineteen',
            '20'    :   'twenty'
            }
print('This program takes the time of day in numbers and returns it in words.')
time = input('Please enter a time in the form xx:xx, for example 3:15 ')
time_split = time.split(':')
if time_split[1] < '20':
        word = numerals[int(time_split[0])] +' ' + minutes[time_split[1]]
elif time_split[1] > '19':
        word = numerals[int(time_split[0])] + ' ' + tens[int(time_split[1]) // 10] + '-' + numerals[int(time_split[1]) % 10]
print(word)