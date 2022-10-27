def bmi (berat,tinggi):
    bmi = berat / (tinggi **2)

    if (bmi < 17.0):
        print("anda sangat kurus")
    elif (bmi >= 17.0 and bmi < 18.0):
        print("anda cukup kurus")
    elif (bmi >=18.0 and bmi <=25.0):
        print("normal")
    elif (bmi >25.0 and bmi <= 27.0):
        print("anda cukup gemuk")
    else:
        print("obesitas")
