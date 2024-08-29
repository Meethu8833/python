m=float(input("Enter your height in meters: "))
kg=float(input("Enter your weight in kilogram: "))
bmi=kg/(m*m)
print("BMI is:",bmi)
if(bmi>0 and bmi<18.5):
    print("Underweight")
elif(bmi>=18.5 and bmi<24.9):
    print("Normal weight")
elif(bmi>=30):
    print("Obese")
else:
    print("Invalid weight")
