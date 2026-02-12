


# Context keeps a reference to current State.
# State is an interface/abstract class with common actions (handle(), pay(), etc.).
# Each ConcreteState(sub class of different states) implements behavior for that state only.
# Context delegates work to current state (no big if/elif in context).
# State transition happens by updating context’s state (context.set_state(...)).
# Keep transition rules clear: either state decides next state, or context decides (pick one style).
# Add new states by new classes, not by editing old condition blocks.
# Good use case: same action behaves differently by status/mode (Order, Vending Machine, Document lifecycle).
#here some functions in a state might not valid , 
# like in atm if someone called withdraw function in no card state it should not work and throw some error
# but in card inserted state
#it should work so we can have two different states for that and we can have different behavior for each state


from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, ctx: "Context") -> None:
        pass

class ConcreteStateA(State):
    def handle(self, ctx: "Context") -> None:
        print("A behavior")
        ctx.set_state(ConcreteStateB())  # transition

class ConcreteStateB(State):
    def handle(self, ctx: "Context") -> None:
        print("B behavior")
        ctx.set_state(ConcreteStateA())  # transition

class Context:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State) -> None:
        self._state = state

    def request(self) -> None:
        self._state.handle(self)
