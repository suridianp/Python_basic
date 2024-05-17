#1. Manipulasi List dan Fungsi
numbers = [3,6,7,9,14,10,7,3,5,1]
numbers2 = [1,2,5,6,3,5,1]
def find_average(x, name):
    jumlah = sum(x)
    anggota = len(x)
    average = jumlah/anggota
    print(f'rata-rata nilai {name} : {average}')
find_average(numbers,'numbers')
find_average(numbers2, 'numbers2')

#2. Pemahaman String dan Fungsi
word = 'manggo is green'

def reverse_words(sentence):
    rw = sentence[::-1]
    print(rw)
reverse_words(word)

#3. Pemahaman Data Casting dan Fungsi
#parameter = degrees, from_unit, to_unit
print('Pilihan unit : C,K,F ') 
d = input('Masukkan nilai derajat yang diinginkan : ')
f = input('Masukkan from unit yang diinginkan : ')
t = input('Masukkan to unit yang diinginkan : ')
def convert_temperature(degrees, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'K':
        degrees_to_unit = float(degrees)+273.15
        print(f'nilai {degrees} Celcius adalah {degrees_to_unit} derajat Kelvin')
    elif from_unit == 'C' and to_unit == 'F':
        degrees_to_unit = degrees+32
        print(f'nilai {degrees} Celcius adalah {degrees_to_unit} derajat Fahrenheit')
    elif from_unit == 'F' and to_unit == 'K':
        degrees_to_unit = float(degrees)+255.372
        print(f'nilai {degrees} Fahrenheit adalah {degrees_to_unit} derajat Kelvin')
    elif from_unit == 'F' and to_unit == 'C':
        degrees_to_unit = float(degrees)-17.7778
        print(f'nilai {degrees} Fahrenheit adalah {degrees_to_unit} derajat Celcius')
    elif from_unit == 'K' and to_unit == 'C':
        degrees_to_unit = float(degrees)-273.15
        print(f'nilai {degrees} Kelvin adalah {degrees_to_unit} derajat Celcius')
    elif from_unit == 'K' and to_unit == 'F':
        degrees_to_unit = float(degrees)-459.67
        print(f'nilai {degrees} Kelvin adalah {degrees_to_unit} derajat Fahrenheit')
    else:
        print('unit yang anda masukkan salah :)')  
convert_temperature(d,f,t)

#4. Manipulasi Dictionary dan fungsi
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
example_string = 'skincare'
result = count_characters(example_string)
print(result)

#5. Pemahaman List Comprehension dan Fungsi
def even_square_numbers(n):
    return [x**2 for x in range(2, n+1, 2)]
# Contoh 
n = input('Masukkan nilai n : ')
result = even_square_numbers(int (n))
print(result)