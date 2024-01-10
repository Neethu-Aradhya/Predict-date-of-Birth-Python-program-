def calculate_birthdate():
    '''
    month = int(input("Enter the month of your birth (1 for Jan, 2 for Feb, ..., 12 for Dec): "))
    day = int(input("Enter the day of your birth: "))
    
    result = ((month * 2 + 5) * 5 * 10) + day
    print("Your final result enter your :", result)
    '''
    print("Hi Bubby,\n i am going to Predict your date of birth using few simple math calculations.\n     Are u ready for it.....!!!!")
    print("Think in mind ")
    print("the number of the month when you was born i.e.  1 for Jan until 12 for Dec.:-> ")
    print("double your month number and then add 5 to it.")
    print("Now Multiply the answer in the previous step by 50.")
    print("Add date of birth ")
    print("for Example - month x 2 +5 x 50 + date")


    ''''
    year = input("Enter the current year: ")
    month = input("Enter the current month: ")
    day = input("Enter the current day: ")
    # Converting user inputs to integer values.
    year = int(year)
    month = int(month)
    day = int(day)
    # Checking if the entered date is valid or not.
    while True:
        try:
            assert 1 <= month <= 12 and 1 <= day <= 31
            break
        except AssertionError:
            print("Invalid Date Entered! Please re-enter a valid")
            day = input("Enter the current day again: ")
            month = input("Enter the current month again: ")
            day = int(day)
            month = int(month)
            # Calculating the age based on the given date.
            result = year - day // 365 - (month < 3 - (day)
                                          % 365 // 31) // 12 - (month
                                                                == 2 and day % 31 >= 28 or month !=
                                                                2 and day % 31 >= 29) // 4
            return result
        '''
  
    result = int(input("Enter your final Result: "))
    final_day = (result % 100) - 50
    final_month = (result // 100) - 2
    
    print("Your date of birth is: Month is :{}- date is :{}".format(final_month, final_day))

# Call the function
calculate_birthdate()
