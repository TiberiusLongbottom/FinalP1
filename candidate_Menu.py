class CandidateMenu:

    def __init__(self, candidates):
        self.candidates = candidates

    def display_menu(self):
        print("Candidate Menu:")
        for index, candidate in enumerate(self.candidates, start=1):
            print(f"{index}. {candidate}")

    def get_choice(self):
        while True:
            try:
                response = int(input("Candidate: ").strip())
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if 1 <= response <= len(self.candidates):
                return response
            else:
                print(f"Invalid candidate number. Please choose between 1 and {len(self.candidates)}.")
