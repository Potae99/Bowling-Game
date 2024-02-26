class BowlingGame:
    def __init__(self):
        self.frames = [BowlingFrame() for _ in range(9)]
        self.frames.append(BowlingFrame10())
        self.current_frame = 0

    def roll(self, pins):
        frame = self.frames[self.current_frame]
        frame.roll(pins)
        if frame.is_complete() and self.current_frame < 9:
            self.current_frame += 1

    def score(self):
        total_score = 0
        for i, frame in enumerate(self.frames):
            total_score += frame.score()
            # Handling strike/spare bonus
            if i < 9:
                next_frame = self.frames[i + 1]
                if frame.is_strike():
                    if next_frame.is_strike():
                        total_score += next_frame.score() + self.frames[i + 2].rolls[0]
                    else:
                        total_score += next_frame.score()
                elif frame.is_spare():
                    total_score += next_frame.rolls[0]
        return total_score


class BowlingFrame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        return sum(self.rolls)

    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def is_complete(self):
        return len(self.rolls) == 2 or self.is_strike()


class BowlingFrame10(BowlingFrame):
    def __init__(self):
        super().__init__()
        self.max_roll = 3

    def is_complete(self):
        return len(self.rolls) == 3 or (len(self.rolls) == 2 and not self.is_strike())
