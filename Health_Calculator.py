def get_input (input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print(f"Not a valid number. Please use only numerical values/n")
    return user_input

def get_choice (input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            if user_input > 2 or user_input < 1:
                raise ValueError
            break
        except ValueError:
            print(f"Not a valid option. Pick a number 1 or 2./n")

    return user_input

def help_open ():
    warning_c = "All these calculations are in metric units but we convert imperial automatically for you\n"
    p_to_kg = "Pounds to Kilograms = Pounds / 2.20462262185"
    cm_to_i = "Inches to Centimetres = Inches X 2.54\n"
    bmi_c = "BMI = Weight(KG) / Height(M)^2\n"
    mhr_yc = "MHR when you're under 40 = 220 - Age"
    mhr_oc = "MHR when you're 40 or over = 208 - (0.75 X Age)\n"
    lhr_c = "Lower Heart Rate = MHR X 0.5"
    uhr_c = "Upper Heart Rate = MHR X 0.85"
    thr_c = "Target Heart Rate = (Lower Heart Rate + Upper Heart Rate) / 2\n"
    bmr_mc = "If you are a male, your BMR = ((10 X Weight(Kg)) + (6.25 X Height(cm)) - (5 X Age)) + 5"
    bmr_fc = "If you are a female, your BMR = ((10 X Weight(Kg)) + (6.25 X Height(cm)) - (5 X Age)) - 161\n"
    calc_list = [warning_c, p_to_kg, cm_to_i, bmi_c, mhr_yc, mhr_oc, lhr_c, uhr_c, thr_c, bmr_mc, bmr_fc]
    
    for x, calc in enumerate(calc_list):
        print(calc_list[x])        

while(True):
    #data gather
    unit = get_choice("Do you use imperial(1) or metric(2) units?", int)
    
    if unit == 1:
        h = get_input("what is your height in inches", float) * 2.54
        w = get_input("what is your weight in pounds", float) / 2.20462262185
    elif unit == 2:
        h = get_input("what is your height in centimetres", float)
        w = get_input("what is your weight in kilograms", float)

    age = get_input("what is your age", int)
    gender = get_choice ("Are you male(1), or female(2)", int)
    
    #calculations
    bmi = w / ((h/100) ** 2)    
    #MHR
    if age < 40:
        mhr = 220 - age
    elif age >= 40:
        mhr = 208 - (0.75 * age)     
    #THR
    lhr = mhr * 0.5    
    uhr = mhr * 0.85    
    thr = (lhr + uhr)/2    
    #BMR
    if gender == 1:
        bmr = ((10 * w) + (6.25 * h) - (5 * age) ) + 5
    elif gender == 2:
        bmr = ((10 * w) + (6.25 * h) - (5 * age) ) - 161    
        
    #Print Information
    #BMI
    if bmi < 18.5:
        print(f"Your BMI: {round(bmi, 1)}, is underweight\n")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"Your BMI: {round(bmi, 1)}, is normal\n")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"Your BMI: {round(bmi, 1)}, is overwight\n")
    elif bmi >= 30:
        print(f"Your BMI: {round(bmi, 1)}, is obese\n")    
    bmi_warning = print("BMI's are only an indicator and do not replace medical advice from a doctor. BMI's can be inaccurate for some people such as bodybuilders or professional athletes, the elderly, children and teenagers, lactating or pregnant women and for certain ethnicities. Please seek professional medical advice if you require it\n")
    #MHR
    print(f"Your MHR is:{mhr}\n")
    #THR
    print(f"Your THR is:{thr}\n")
    #BMR
    print(f"Your BMR is:{bmr}\n")
    
    #help menu redirect
    help_menu = get_choice("Do you need to know the calculations for these? Yes(1) No(2)", int)
    if help_menu == 2:
        print("Thank you for using the health calculator")
        break
    if help_menu == 1:
        help_open()
        