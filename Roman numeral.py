#Input Roman Numeral
rom = input('Enter Roman Numeral: ')
# Create Dictionary
roman_values = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
# Compute Decimal
num = 0
for i in range(len(rom)):
    if i > 0 and roman_values[rom[i]] > roman_values[rom[i-1]]:
        num += roman_values[rom[i]] - 2 * roman_values[rom[i-1]]
    else:
        num += roman_values[rom[i]]
print('Decimal Representation of Roman Numeral is ' + str(num))