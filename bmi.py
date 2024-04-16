w=float(input("Enter weight in kg:"))
h=float(input("Enter height in metres:"))
b=w/(h*h)
if b<18.5:
		print("BMI is:", b)
		print("Underweight")
elif b<25:
		print("BMI is:", b)
		print("Normal")
elif b<30:
		print("BMI is:", b)
		print("Overweight")
else:
		print("BMI is:", b)
		print("obesity")