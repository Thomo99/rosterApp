shifts = {
    'monday' : ['0600', '1200', '0800', '1600', '1200', '2000'],
    'tuesday' : ['0600', '1200', '0800', '1600', '1200', '2000'],
    'wednesday' : ['0600', '1200', '0800', '1600', '1200', '2000'],
    'thursday' : ['0600', '1200', '1000', '1600', '1200', '2000'],
    'friday' : ['0600', '1400', '1000', '1600', '1500', '2000'],
    'saturday' : ['0600', '1400', '0900', '1600', '1200', '2000'],
    'sunday' : ['0600', '1400', '0600', '1600', '1400', '2000']
}


#--------------------------------------------Enter Shifts--------------------------------------------------------

def entershifts():
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("Day? ").lower()

        

        valid = False
        while not valid:
            if day in days:
                start_time = input("Start time? ")
                end_time = input("End time? ")


                if len(start_time) == len(end_time) == 4 and start_time.isdigit() and end_time.isdigit():
                    shifts[day].append(start_time)
                    shifts[day].append(end_time)
                    print(f'{start_time} - {end_time} added to {day}.')
                    valid = True
                
                else:
                    print("Please enter proper times \nFor example: 1000 for 10AM or 2200 for 10PM.")

            else:
                print("Invalid day, try again")

        go_again = input("Press Y to add another shift:  ").upper()

        if go_again == 'Y':
            continue
        else:
            break

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------Remove Shifts-----------------------------------------------------------
        
def remove_shifts():
    print()

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------Display Shifts----------------------------------------------------------
    
def display_shifts():
    print('*'*50)
    for day, day_shifts in shifts.items():
        print(day.capitalize() + " shifts:")
        for i in range(0, len(day_shifts), 2):
            start_time = day_shifts[i]
            end_time = day_shifts[i + 1]
            print(f"  Shift {i//2 + 1}: {start_time}-{end_time}")
        print()
    print('*'*50)
    print()


#-------------------------------------------------------------------------------------------------------------------
    

print("Options: \n1. Enter shifts\n2. Remove shifts")

while True:
    user_int = input("What would you like to do?(Enter number) or \'quit\' to exit  ")

    if user_int == '1':
        display_shifts()

    elif user_int == '2':
        entershifts()
    
    elif user_int =='3':
        remove_shifts()
        
    elif user_int == 'quit':
        break