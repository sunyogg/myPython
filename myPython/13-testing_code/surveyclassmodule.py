class AnonymousSurvey:
    """Collect anonymous answer to the survey question."""

    def __init__(self,question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []


    def show_question(self):
        """Show the survey question."""
        print(self.question)


    def store_responses(self,new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)


    def show_responses(self):
        """Show responses of the survey."""
        print("\nSurvey result: ")
        for response in self.responses:
            print(f"-> {response}")






