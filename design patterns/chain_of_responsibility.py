from abc import ABC, abstractmethod
from typing import Optional



# Core implementation points
# Every handler keeps a reference to next_handler (nullable).
# Base handler provides set_next() to build the chain.
# set_next() often returns the passed handler to allow fluent chaining.
# Base handler should provide common forwarding logic (forward()), so concrete handlers stay clean.
# Each concrete handler follows rule:
# if it can process request -> handle and return
# else -> forward to next
# Define clear behavior when no handler can process:
# return None, or
# return default response, or
# raise exception (decide upfront).


class Handler(ABC):
    def __init__(self):
        self._next: Optional["Handler"] = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler  # allows chaining

    @abstractmethod
    def handle(self, request):
        pass

    def _forward(self, request):
        if self._next:
            return self._next.handle(request)
        return None




class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Handled by A"
        return self._forward(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "Handled by B"
        return self._forward(request)
h1 = ConcreteHandlerA()
h2 = ConcreteHandlerB()
h1.set_next(h2)

print(h1.handle("B"))   # Handled by B
print(h1.handle("X"))   # None (unhandled)
