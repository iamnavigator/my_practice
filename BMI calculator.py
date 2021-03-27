height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / (height ** 2)

if BMI < 18.5 :
  print("You are underweight")
elif 18.5 > BMI < 25 :
    print("You have normal weight")
elif 25 > BMI < 30 :
    print("You are slightly overweight")
elif 30 > BMI < 35 :
    print("You are Obese")
else:
    print("You are clinically Obese")
