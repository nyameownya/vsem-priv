def the_final_countdown(number):
    print (number)
    if number != 1: 
        the_final_countdown(number - 1)
    else:
        print("We are done")
        return 

print(the_final_countdown(5))
