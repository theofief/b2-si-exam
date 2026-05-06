from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def insert_token(self):
        raise NotImplementedError

    @abstractmethod
    def eject_token(self):
        raise NotImplementedError

    @abstractmethod
    def turn_crank(self):
        raise NotImplementedError

    @abstractmethod
    def dispense(self):
        raise NotImplementedError

    @abstractmethod
    def refill(self, count: int):
        raise NotImplementedError


class NoTokenState(State):
    def insert_token(self):
        if self.machine.ball_count > 0:
            self.machine.current_state = OneTokenState(self.machine)
            return True
        self.machine.current_state = SoldOutState(self.machine)
        return False

    def eject_token(self):
        return False

    def turn_crank(self):
        return False

    def dispense(self):
        return False

    def refill(self, count: int):
        add = max(0, int(count))
        if add <= 0:
            return False
        self.machine.ball_count += add
        return True


class OneTokenState(State):
    def insert_token(self):
        return False

    def eject_token(self):
        self.machine.current_state = NoTokenState(self.machine)
        return True

    def turn_crank(self):
        self.machine.current_state = DispensingState(self.machine)
        self.machine.current_state.dispense()
        return True

    def dispense(self):
        return False

    def refill(self, count: int):
        add = max(0, int(count))
        if add <= 0:
            return False
        self.machine.ball_count += add
        return True


class DispensingState(State):
    def insert_token(self):
        return False

    def eject_token(self):
        return False

    def turn_crank(self):
        return False

    def dispense(self):
        if self.machine.ball_count <= 0:
            self.machine.current_state = SoldOutState(self.machine)
            return False

        self.machine.ball_count -= 1
        if self.machine.ball_count == 0:
            self.machine.current_state = SoldOutState(self.machine)
        else:
            self.machine.current_state = NoTokenState(self.machine)
        return True

    def refill(self, count: int):
        add = max(0, int(count))
        if add <= 0:
            return False
        self.machine.ball_count += add
        return True


class SoldOutState(State):
    def insert_token(self):
        return False

    def eject_token(self):
        return False

    def turn_crank(self):
        return False

    def dispense(self):
        return False

    def refill(self, count: int):
        add = max(0, int(count))
        if add <= 0:
            return False
        self.machine.ball_count += add
        if self.machine.ball_count > 0:
            self.machine.current_state = NoTokenState(self.machine)
        return True


class GiftBall:
    def __init__(self, initial_balls: int = 0):
        self.ball_count = max(0, int(initial_balls))
        self.current_state = SoldOutState(self) if self.ball_count == 0 else NoTokenState(self)

    def insert_token(self):
        return self.current_state.insert_token()

    def eject_token(self):
        return self.current_state.eject_token()

    def turn_crank(self):
        return self.current_state.turn_crank()

    def dispense(self):
        return self.current_state.dispense()

    def refill(self, count: int):
        return self.current_state.refill(count)

    def __repr__(self):
        return f"<GiftBall state={self.current_state.__class__.__name__} balls={self.ball_count}>"
