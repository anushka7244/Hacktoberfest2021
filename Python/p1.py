sum =0
while(True):
    number = input('Enter a number: \n')
    if(number!='q'):
        sum = sum+ int(number)
        print(f"Order total so far : {sum}")

    else:
        print(f"Your bill total is {sum}")
        print("Thanks")
        break
    
        
    
