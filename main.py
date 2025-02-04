
def changes():
    pass


yes_choices = ["yes", "y", "ye", "yea"]

add_player = True
list_of_players = []

# Add players to player list workflow

while add_player:
    player = input("Enter a player name: ")
    list_of_players.append(player)
    cont = input("Enter another player? ").lower()
    if cont not in yes_choices:
        print(f"List of all players: {list_of_players}")
        correct_players = input("Is this correct? ").lower()
        if correct_players in yes_choices:
            add_player = False
    else:
        continue

