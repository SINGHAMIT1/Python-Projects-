# BMI= WEIGHT(KG)/HEIGHT(M)^2
weight = float(input("Enter your weight in KG :"))
height = float(input("Enter your height in Centimeter :"))
height = height / 100
BMI = weight / (height * height)
print("Your Body Mass index is :", BMI)
if BMI > 0:
    if BMI <= 16:
        print("You are severally Underweight")
    elif BMI <= 18.5:
        print("You are Underweight")
    elif BMI <= 25:
        print("You are Healthy")
    elif BMI <= 30:
        print("You are Overweight")
    elif BMI >= 31:
        print("Obesity")
else:
    print("Enter valid weight and height value")
