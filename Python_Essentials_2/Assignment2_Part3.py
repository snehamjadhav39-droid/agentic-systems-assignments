class StudentPerformance:
    def __init__(self, scores): self.scores = scores
    def score_difference(self):
        try: print("Difference between last and first score is:", self.scores[-1]-self.scores[0])
        except: print("No scores available to calculate difference")

StudentPerformance([55,65,75,85]).score_difference()
