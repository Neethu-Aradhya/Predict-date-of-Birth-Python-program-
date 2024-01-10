def calculate_birthdate():
    month = int(input("Enter the month of your birth (1 for Jan, 2 for Feb, ..., 12 for Dec): "))
    day = int(input("Enter the day of your birth: "))
    
    result = ((month * 2 + 5) * 5 * 10) + day
    print("Your final result is:", result)
    
    final_day = (result % 100) - 50
    final_month = (result // 100) - 2
    
    print("Your date of birth is: {}-{}".format(final_month, final_day))

# Call the function
calculate_birthdate()
