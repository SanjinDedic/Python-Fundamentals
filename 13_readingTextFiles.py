text = open('HarryPotter.txt')
text = text.read()

text = text[0:5600]

d = {}

d['Harry'] = '__Kid Magic__'
d['Harry Potter'] = '__Kid Magic__'
d['Dudley'] = '__Mean Kid__'
d['Mr. Dursley'] = '___Father of Mean Kid___'

for key in d:
    text = text.replace(key,d[key])

print(text)
