def bmi(w, h):
    result = w / (h ** 2)
    return result

def classify(result):
    if result < 18.5:
        return "underweight"
    elif 18.5 <= result < 25:
        return "normal weight"
    elif 25 <= result < 30:
        return "overweight"
    else:
        return "obese"

w = float(input("Enter your weight: "))
h = float(input("Enter your height in m: "))

bmi_result = bmi(w, h)
status = classify(bmi_result)

print("Your BMI is:", bmi_result)
print("You are classified as:", status)
