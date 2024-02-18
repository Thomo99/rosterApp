def entershifts():
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("Day? ").lower()

        shifts = {
            'monday' : [],
            'tuesday' : [],
            'wednesday' : [],
            'thursday' : [],
            'friday' : [],
            'saturday' : [],
            'sunday' : []
        }

        valid = False
        while not valid:
            if day in days:
                start_time = input("Start time? ")
                end_time = input("End time? ")


                if len(start_time) == len(end_time) == 4 and start_time.isdigit() and end_time.isdigit():
                    shifts[day].append(int(start_time))
                    shifts[day].append(int(end_time))
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


print("Options: \n1. Enter shifts")

user_int = input("What would you like to do?(Enter number) ")

if user_int == '1':
    entershifts()

else:
    quit()