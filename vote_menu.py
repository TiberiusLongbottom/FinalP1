class VoteMenu:

    def __init__(self):
        self.options = {"v": "Vote", "x": "Exit"}

    def display_menu(self):
        print("Vote Menu:")
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def get_choice(self):
        while True:
            response = input("Option: ").strip().lower()
            if response in self.options:
                return self.options[response]
            else:
                print("Invalid option. Please choose (v/x)")
