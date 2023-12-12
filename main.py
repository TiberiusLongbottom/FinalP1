from PyQt6 import QtWidgets
from election import Election

candidates = ["Cameron", "Allison", "Diego"]
election = Election(candidates)

class VoteWindow(QtWidgets.QWidget):

    def __init__(self, election, parent=None):
        super().__init__(parent)
        self.election = election

        # Create layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Add candidate buttons
        for i, candidate in enumerate(self.election.candidates):
            button = QtWidgets.QPushButton(candidate)
            button.clicked.connect(lambda _, i=i: self.submit_vote(i))
            self.layout.addWidget(button)

        # Add vote tally label
        self.vote_tally_label = QtWidgets.QLabel("Current Vote Tally:")
        self.layout.addWidget(self.vote_tally_label)

        # Add exit button
        self.exit_button = QtWidgets.QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def submit_vote(self, candidate_index):
        self.election.vote_count[candidate_index] += 1
        self.update_vote_tally()

    def update_vote_tally(self):
        vote_tally_text = ""
        for candidate, count in zip(self.election.candidates, self.election.vote_count):
            vote_tally_text += f"{candidate}: {count} votes\n"
        self.vote_tally_label.setText(vote_tally_text)

app = QtWidgets.QApplication([])
window = VoteWindow(election)
window.show()
app.exec()

election.display_results()  # display final results after exiting the GUI
