from throw import Throw
import random


class Player:
    def __init__(self) -> None:
        self.throw_options = [enum for enum in Throw]
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def get_throw(self) -> Throw | None:
        raise NotImplementedError()

    def record_win(self):
        self.wins += 1

    def record_loss(self):
        self.losses += 1

    def record_tie(self):
        self.ties += 1


class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def get_throw(self) -> Throw:
        return random.choice(self.throw_options)

    def __str__(self) -> str:
        return "Computer"


class HumanPlayer(Player):
    def __init__(self, name: str = "Player One") -> None:
        super().__init__()
        self.name = name

    def get_throw(self, max_tries: int = 1, quit_option: str = "q") -> Throw | None:
        num_tries = 0
        user_choice = ""
        option_prompt = ', '.join([f'{name}: {enum.value}' for name, enum in Throw._member_map_.items()])
        while num_tries < max_tries and user_choice != quit_option:
            user_choice = input(
                f"What does {self.name} want to pick? {option_prompt} "
            )
            if user_choice.isdecimal() and int(user_choice) in Throw:
                return Throw(int(user_choice))
            num_tries += 1
        return None

    def __str__(self) -> str:
        return self.name


if __name__ == "__main__":
    # simple example
    player = HumanPlayer()
    player_throw = player.get_throw()
    if player_throw is None:
        print("Try typing better, fool")
        exit()

    print(f"Player's {player_throw} {player_throw < Throw.Scissors} against Scissors")

















    # little more complicated...
    # computer = ComputerPlayer()
    # computer_throw = computer.get_throw()
    
    # print(f"Player's {player_throw} {player_throw < computer_throw} against Computer's {computer_throw}")

    # if player_throw < computer_throw == "loss":
    #     player.record_win()
    #     computer.record_loss()
    # elif player_throw == computer_throw:
    #     player.record_tie()
    #     computer.record_tie()
    # else:
    #     player.record_loss()
    #     computer.record_win()
