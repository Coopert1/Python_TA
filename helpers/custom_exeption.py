class WrongOperatorError(ValueError):
    def __init__(self, message="Error: Chose ONLY operator from list"):
        self.message = message
        super().__init__(self.message)
