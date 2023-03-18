print('exercise №1')

print({num: num**2 for num in range(1, 11)})

print('-' * 50)
print('exercise №2')

price_in_dollars = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_ruble = 70

print({item: value * dollar_to_ruble for item, value in price_in_dollars.items()})

print('-' * 50)
print('exercise №3')

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

print({key: ('young' if values < 40 else 'old') for (key, values) in original_dict.items()})

