name1 = "psp"
height1 = 5.10
weight1 = 84

name2 = "psp's sister"
height2 = 5.6
weight2 = 65

name3 = "psp's brother"
height3 = 5.9
weight3 = 45


def function_bmi(name, height, weight):
    bmi = weight / (height ** 2)
    print ("BMI is : ", bmi)
    if bmi < 2:
        return name + " is not overweight"
    else:
        return name + " is overweight"


result1 = function_bmi(name1, height1, weight1)
result2 = function_bmi(name2, height2, weight2)
result3 = function_bmi(name3, height3, weight3)


print (result1)
print (result2)
print (result3)
