class Election:

    def __init__(self, candidates):
        self.candidates = candidates
        self.vote_count = [0 for _ in candidates]
        self.is_running = True

    def run(self):
        # Display candidate information
        print("** Election Candidates:")
        for i, candidate in enumerate(self.candidates):
            print(f"{i + 1}. {candidate}")
        print("-" * 20)

        # Create and display the voting window
        app = QtWidgets.QApplication([])
        window = VoteWindow(self)
        window.show()
        app.exec()

        # Check if any votes were cast
        if not any(self.vote_count):
            print("No votes cast.")
        else:
            # Display election results
            print("** Election Results:")
            for candidate, count in zip(self.candidates, self.vote_count):
                print(f"{candidate}: {count} votes")
    def display_results(self):
        if self.is_running:
            for candidate, count in zip(self.candidates, self.vote_count):
                print(f"{candidate}: {count} votes")
        else:
            print("No votes cast.")

    def set_running(self, running):
        self.is_running = running
