from enum import Enum, auto


class State(Enum):
    NO_TOKEN = auto()
    ONE_TOKEN = auto()
    DISPENSING = auto()
    SOLD_OUT = auto()


class GiftBall:
    """Représente la machine distributrice de balles surprise"""

    def __init__(self, initial_balls: int = 0):
        self.ball_count = max(0, int(initial_balls))
        self.current_state = State.SOLD_OUT if self.ball_count == 0 else State.NO_TOKEN

    def insert_token(self):
        """Insère un jeton dans la machine"""
        if self.current_state == State.NO_TOKEN:
            if self.ball_count > 0:
                self.current_state = State.ONE_TOKEN
                return True
            else:
                self.current_state = State.SOLD_OUT
                return False
        return False

    def eject_token(self):
        """Ejecte le jeton si présent"""
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.NO_TOKEN
            return True
        return False

    def turn_crank(self):
        """Tourner la manivelle pour tenter d'obtenir une balle"""
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.DISPENSING
            self.dispense()
            return True
        return False

    def dispense(self):
        """Distribue une balle si possible"""
        if self.current_state != State.DISPENSING:
            return False
        if self.ball_count <= 0:
            self.current_state = State.SOLD_OUT
            return False

        # délivrer une balle
        self.ball_count -= 1
        # après distribution, si plus de balles -> NO_TOKEN sinon SOLD_OUT
        if self.ball_count == 0:
            self.current_state = State.SOLD_OUT
        else:
            self.current_state = State.NO_TOKEN
        return True

    def refill(self, count: int):
        """Remplit la machine de `count` balles"""
        add = max(0, int(count))
        if add == 0:
            return False
        self.ball_count += add
        if self.current_state == State.SOLD_OUT and self.ball_count > 0:
            self.current_state = State.NO_TOKEN
        return True

    def __repr__(self):
        return f"<GiftBall state={self.current_state.name} balls={self.ball_count}>"
