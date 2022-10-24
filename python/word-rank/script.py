# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

'''sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]'''
sentences = input()
sentences = list(map(lambda x : x.replace(',', '').split(' '), sentences))

words =[]
for x in sentences:
    for y in x:
        words.append(y)

words = list(map(lambda x : x.lower(), words))

words1 = list(set(words))
words1 = list(map(lambda x : [x, 0], words1))

for x in words:
    for y in words1:
        if x == y[0]:
            y[1] += 1

r = sorted(words1, key=lambda x: x[1], reverse=1)[:3]

print('1. '+ r[0][0] + ' - "' + str(r[0][1]) + '"\n' + '2. '+ r[1][0] + ' - "' + str(r[1][1]) + '"\n' + '3. '+ r[2][0] + ' - "' + str(r[2][1]) + '"')

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
