# T1
city = 'London'
print(city)


# T2
city = 'berlin'
population = 645000

print(city.capitalize(), ': ',population, sep='')


# T3
city = 'london'
population = 9000000

# print('City: ', city.capitalize(), type(city) == str)
print('City: ', city.capitalize(), city.isalpha())
print('Population:', population)


# T4
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
word = 'capital'

if word in text:
    print(word, ': ',text.find(word), sep='')


# T5
text = 'Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.'
text_list = text.split()

print(text_list[0: ])       # [0: ] not necessary, just testing stuff


# T6
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
word = 'capital'

if word in text:
    text = text.replace(word, 'capital of Germany')

print(text)
