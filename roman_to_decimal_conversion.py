# converting roman numbers to decimals numbers
# specify the decimal equivalent
tallies = {
    "I": 1,
    "V": 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,

}


# XVI, 2(0,1), l=x,r=v, 10

def romanToDecimal(roman_numbers):
    sum = 0

    for i in range (len(roman_numbers) - 1):
        left = roman_numbers[i]  # 1-V
        right = roman_numbers[i + 1]  # 2-I
        if tallies[left] < tallies[right]:  # 5,1
            sum -= tallies[left]
        else:  # 5>1
            sum += tallies[left]  # 10+5=15
            # 0+10=10,
    sum += tallies[roman_numbers[-1]]
    return sum


roman = input("put a roman number :")
deci = romanToDecimal(roman)
print("The decimal conversion of the roman number is :", deci)
# Roman_Number=input("Enter any Roman number")
# Equilant_Decimal=romanToDecimal(Roman_Number)
# print(Equilant_Decimal)
