height=float(input("Height (in meters) : "))
weight=float(input("Weight (in kgs) : "))

div= height*height

bmi= weight/div

if bmi< 18.5:
     print("Underweight")
elif bmi>=18.5 and bmi< 25:
     print ("NORMAL")
elif bmi >= 25 and bmi < 30:
     print("Overweight")
elif bmi > 30:
     print("Obese")
