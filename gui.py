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

        # Add exit button
        self.exit_button = QtWidgets.QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def submit_vote(self, candidate_index):
        self.election.vote_count[candidate_index] += 1
        self.close()
