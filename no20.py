def res():
    percentage= float(input("enter your percentage :"))
    if percentage < 41 :
        print("Failed")
    elif percentage >=41 and percentage<55:
        print("Fair")
    elif percentage >= 55 and percentage<65:
        print("good")
    elif percentage >=65:
        print("Excellent")
    else:
        print("enter valid percentage")
res()