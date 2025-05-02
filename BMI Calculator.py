import os, math
from colorama import just_fix_windows_console, Fore

just_fix_windows_console()
while True:
    os.system('cls')
    print('Welcome to the BMI Calculator Tool...')
    
    try:
        w = float(input('[+] WEIGHT(kg)>>'))
        h = float(input('[+] HEIGHT(meter)>>'))
        bmi = w / math.pow(h,2)
        bmi = round(bmi,2)
        print('BMI>>',bmi)
        if bmi < 18.5:
            status = print(Fore.GREEN + 'UNDER WEIGHT')
        elif 18.5 <= bmi < 24.9:
            status = print(Fore.GREEN + 'NORMAL')
        elif 24.9 <= bmi < 29.9:
            status = print(Fore.YELLOW + 'OVER WEIGHT')
        elif 29.9 <= bmi < 39.9:
            status = print(Fore.RED + 'OBESE')
        elif 40 < bmi:
            status = print(Fore.RED + 'EXTREMELY OBESE')
    except:
        print('Error! Please Enter Numeric Values!')
        
    print(Fore.RESET + 'AGAIN? Y)Yes N)No')
    res = input('#>>>').strip().lower()
    if res in ['y', 'yes']:
        continue
    else:
        break