#Lesson 05 Notes - Neville

games_list = [1, 3, 5, 7, 9]
total_games = int(input("How many games would you like to play (1-9), odd number only:  "))

while total_games not in games_list:
    print("Please enter an odd number between 1 and 9")
    total_games = int(input("How many games would you like to play (1-9), odd number only:  "))

user_wins = 0
cpu_wins = 0
wins_needed = (total_games //2) + 1

#Test
print(total_games)
print(wins_needed)
while user_wins < wins_needed and cpu_wins < wins_needed:
    #Game logic
    user_choice = get_user_choice()
    cpu_choice = get_cpu_choice()
    rps_logic()

