### look up a persons rank and years of service
unit = {
    "snuffy": {'name': 'Snuffy', 'rank': 'PFC', 'years': 2},
    "johnson": {'name': 'Johnson', 'rank': 'SGT', 'years': 5}
}
#unit["hernandez"] = {rank: sgt}

def lookup_soldier(unit, last_name):
        if last_name in unit:
            rank = unit[last_name]["rank"]
            years = unit[last_name]["years"]
            print(f"Found {last_name}")
            print(f"\t Rank: {rank}")
            print(f"\t Service: {years}")
        else:
            print(f"{last_name} Not Found.")

user_input = input("Choose a Soldier: ")
lookup_soldier(unit, user_input.strip())