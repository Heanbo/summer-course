# Okay, great.  You found the telemetry file.

# As the colonists approach Mars, you need to help them calculate their telemetry data.  To do this, you are going to
# write a python program.  The program should ask the user if they would like to input either "Miles above Mars" or
# "Kilometers above Mars".  If they choose "Miles above Mars", the program should then prompt them to enter the number
# of miles.  Then the program should display the number of yards, feet, and inches that are in that many miles.
# If the user chooses "Kilometers above Mars", the program should then prompt them to enter the number of kilometers.
# Then the program should display the number of meters, centimeters, and millimeters that are in that many kilometers.


Miles_to_yards = 1760
Miles_to_feet = 5280
Miles_to_inches = 63360

Kilometers_to_meters = 1000
Kilometers_to_centimeters = 100000
Kilometers_to_millimeters = 1000000

user_input = (
    input(
        "Computer > Would you like to input 'Miles' or 'Kilometers' above Mars? (Miles/Kilometers) \nYou > "
    )
    .strip()
    .lower()
)

while user_input not in ["miles", "kilometers"]:
    user_input = (
        input(
            "Computer > Invalid input. Please enter 'Miles' or 'Kilometers' above Mars. (Miles/Kilometers) \nYou > "
        )
        .strip()
        .lower()
    )
if user_input == "miles":
    miles = float(input("Enter the number of miles: "))
    yards = miles * Miles_to_yards
    feet = miles * Miles_to_feet
    inches = miles * Miles_to_inches
    print(f"{miles} miles is equal to \n{yards} yards \n{feet} feet \n{inches} inches")
elif user_input == "kilometers":
    kilometers = float(input("Enter the number of kilometers: "))
    meters = kilometers * Kilometers_to_meters
    centimeters = kilometers * Kilometers_to_centimeters
    millimeters = kilometers * Kilometers_to_millimeters
    print(
        f"{kilometers} kilometers is equal to \n{meters} meters \n{centimeters} centimeters \n{millimeters} millimeters"
    )
