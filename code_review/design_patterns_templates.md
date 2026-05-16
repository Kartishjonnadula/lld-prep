# Design Pattern Templates (Python)

Use this in two passes:
1. Read the notes under each pattern.
2. Read the code skeleton and map each role to a real system.

Interview tip:
- First state intent.
- Then map classes to roles.
- Then mention one tradeoff.

## Creational Patterns

### 1) Singleton
- Intent: Ensure only one instance exists and provide global access.
- Use when: One shared coordinator is required (for example config registry).
- Watch out: Hidden global state hurts tests and increases coupling.
- Review signal: Many modules call the singleton directly.

```python
class ConfigSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 2) Factory Method
- Intent: Defer object creation to subclasses.
- Use when: Creation varies by runtime type, but flow stays same.
- Watch out: If simple branching is enough, avoid over-engineering.
- Review signal: Large if/else creation logic in one method.

```python
from abc import ABC, abstractmethod

class ReportFile(ABC):
    @abstractmethod
    def write(self, content: str): ...

class PdfReportFile(ReportFile):
    def write(self, content: str):
        return f"PDF<{content}>"

class CsvReportFile(ReportFile):
    def write(self, content: str):
        return f"CSV<{content}>"

class ReportExporter(ABC):
    # Factory Method
    @abstractmethod
    def create_file(self) -> ReportFile: ...

    def export(self, content: str):
        file = self.create_file()
        return file.write(content)

class PdfReportExporter(ReportExporter):
    def create_file(self) -> ReportFile:
        return PdfReportFile()

class CsvReportExporter(ReportExporter):
    def create_file(self) -> ReportFile:
        return CsvReportFile()

# client code
def run_export(exporter: ReportExporter):
    return exporter.export("daily-sales")
```

### 3) Abstract Factory
- Intent: Create families of related objects without concrete class coupling.
- Use when: You must switch entire product family together (web/mobile theme).
- Watch out: More interfaces/classes than small apps need.
- Review signal: Button/Input/Checkbox families repeated per platform.

```python
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self): ...

class Input(ABC):
    @abstractmethod
    def render(self): ...

class WebButton(Button):
    def render(self):
        return "<button class='web'>Submit</button>"

class MobileButton(Button):
    def render(self):
        return "[MobileButton: Submit]"

class WebInput(Input):
    def render(self):
        return "<input class='web' />"

class MobileInput(Input):
    def render(self):
        return "[MobileInput]"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_input(self) -> Input: ...

class WebUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WebButton()
    def create_input(self) -> Input:
        return WebInput()

class MobileUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MobileButton()
    def create_input(self) -> Input:
        return MobileInput()

def render_login_form(factory: UIFactory):
    btn = factory.create_button()
    inp = factory.create_input()
    return inp.render(), btn.render()
```

### 4) Builder
- Intent: Build complex object step-by-step.
- Use when: Object has many optional combinations/construction steps.
- Watch out: Do not use builder for trivial objects.
- Review signal: Constructor with too many parameters/flags.

```python
class House:
    def __init__(self):
        self.parts = []

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_walls(self):
        self.house.parts.append("walls")
        return self

    def add_roof(self):
        self.house.parts.append("roof")
        return self

    def add_garden(self):
        self.house.parts.append("garden")
        return self

    def build(self):
        return self.house
```

### 5) Prototype
- Intent: Create new objects by copying existing instances.
- Use when: Construction is expensive or runtime configs vary.
- Watch out: Deep vs shallow copy bugs.
- Review signal: Repeated expensive initialization for similar objects.

```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ReportTemplate(Prototype):
    def __init__(self, sections):
        self.sections = sections
```

## Structural Patterns

### 6) Adapter
- Intent: Convert one interface into another expected by clients.
- Use when: Integrating legacy/third-party API without changing client code.
- Watch out: Adapter should translate, not own domain rules.
- Review signal: New code leaks old API shape everywhere.

```python
class LegacyPaymentAPI:
    def make_payment(self, amount):
        return f"legacy-paid:{amount}"

class PaymentPort:
    def pay(self, amount): ...

class PaymentAdapter(PaymentPort):
    def __init__(self, legacy: LegacyPaymentAPI):
        self.legacy = legacy

    def pay(self, amount):
        return self.legacy.make_payment(amount)
```

How this code maps to Adapter roles:
- Target interface (what client expects): `PaymentPort.pay(...)`
- Adaptee (existing incompatible API): `LegacyPaymentAPI.make_payment(...)`
- Adapter (translator): `PaymentAdapter`
- Call flow: client calls `pay(amount)` -> adapter delegates to `legacy.make_payment(amount)`

### 7) Bridge
- Intent: Separate abstraction from implementation so both vary independently.
- Use when: You have two dimensions of change (remote type x device type).
- Watch out: Adds indirection; keep it justified.
- Review signal: Class explosion from Cartesian combinations.

```python
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def on(self): ...

    @abstractmethod
    def off(self): ...

class TV(Device):
    def on(self): return "tv on"
    def off(self): return "tv off"

class Remote:
    def __init__(self, device: Device):
        self.device = device

    def toggle_on(self):
        return self.device.on()
```

### 8) Composite
- Intent: Treat part and whole uniformly in tree structures.
- Use when: Nested menu/folder/organization hierarchies.
- Watch out: Leaf operations should remain meaningful.
- Review signal: Client code checks node type repeatedly.

```python
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def operation(self): ...

class Leaf(Node):
    def operation(self):
        return "leaf"

class Composite(Node):
    def __init__(self):
        self.children = []

    def add(self, node: Node):
        self.children.append(node)

    def operation(self):
        return [child.operation() for child in self.children]
```

### 9) Decorator
- Intent: Add responsibilities dynamically without subclass explosion.
- Use when: Optional combinations of behaviors (email + sms + push).
- Watch out: Many small wrappers can complicate debugging order.
- Review signal: Dozens of subclasses for feature combinations.

```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, msg): ...

class EmailNotifier(Notifier):
    def send(self, msg):
        return [f"email:{msg}"]

class SMSDecorator(Notifier):
    def __init__(self, wrappee: Notifier):
        self.wrappee = wrappee

    def send(self, msg):
        return self.wrappee.send(msg) + [f"sms:{msg}"]
```

### 10) Facade
- Intent: Provide a simplified interface over complex subsystem.
- Use when: You want one entry point for common workflow.
- Watch out: Facade should not become god-object.
- Review signal: Callers orchestrate too many subsystem steps.

```python
class InventoryService:
    def reserve(self, sku, qty):
        return True

class PaymentService:
    def charge(self, user_id, amount):
        return "txn-1"

class CheckoutFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payment = PaymentService()

    def place_order(self, user_id, sku, qty, amount):
        self.inventory.reserve(sku, qty)
        return self.payment.charge(user_id, amount)
```

### 11) Flyweight
- Intent: Share intrinsic immutable state to reduce memory footprint.
- Use when: Huge number of similar objects (characters, map tiles).
- Watch out: Separate intrinsic vs extrinsic state correctly.
- Review signal: Memory blowup from repeated identical data.

```python
class CharacterStyle:
    def __init__(self, font, size, color):
        self.font, self.size, self.color = font, size, color

class StyleFactory:
    _cache = {}

    @classmethod
    def get_style(cls, font, size, color):
        key = (font, size, color)
        if key not in cls._cache:
            cls._cache[key] = CharacterStyle(*key)
        return cls._cache[key]
```

### 12) Proxy
- Intent: Control access to a real object (lazy load, auth, caching).
- Use when: You need pre/post checks around existing object.
- Watch out: Proxy and real subject interfaces must stay aligned.
- Review signal: Repeated access checks around same calls.

```python
class RealImage:
    def __init__(self, path):
        self.path = path

    def display(self):
        return f"displaying {self.path}"

class ImageProxy:
    def __init__(self, path):
        self.path = path
        self._real = None

    def display(self):
        if self._real is None:
            self._real = RealImage(self.path)
        return self._real.display()
```

## Behavioral Patterns

### 13) Chain of Responsibility
- Intent: Pass request through handler chain until handled.
- Use when: Validation/filter pipelines.
- Watch out: Missing default handler or incorrect chain order.
- Review signal: Large validation block with many independent checks.

```python
class Handler:
    def __init__(self, nxt=None):
        self.nxt = nxt

    def handle(self, request):
        if self.nxt:
            return self.nxt.handle(request)
        return "unhandled"

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("auth"):
            return "401"
        return super().handle(request)
```

### 14) Command
- Intent: Encapsulate request as object.
- Use when: Queue, retry, undo, audit of actions.
- Watch out: Too many tiny commands with no shared abstraction value.
- Review signal: UI/business logic tightly coupled in click handlers.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): ...

class Light:
    def on(self):
        return "light on"

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        return self.light.on()
```

### 15) Interpreter
- Intent: Represent grammar and evaluate expressions.
- Use when: Small DSL/rules engine.
- Watch out: For complex grammars, prefer parser libraries.
- Review signal: Many ad-hoc string parses with nested conditionals.

```python
from abc import ABC, abstractmethod

class Expr(ABC):
    @abstractmethod
    def interpret(self, ctx): ...

class Number(Expr):
    def __init__(self, value):
        self.value = value

    def interpret(self, ctx):
        return self.value

class Add(Expr):
    def __init__(self, left, right):
        self.left, self.right = left, right

    def interpret(self, ctx):
        return self.left.interpret(ctx) + self.right.interpret(ctx)
```

### 16) Iterator
- Intent: Traverse collection without exposing internals.
- Use when: Need consistent traversal interface.
- Watch out: Iterator should be independent from collection mutation surprises.
- Review signal: Callers depend on internal storage structure.

```python
class NameCollection:
    def __init__(self, names):
        self.names = names

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i >= len(self.names):
            raise StopIteration
        val = self.names[self._i]
        self._i += 1
        return val
```

### 17) Mediator
- Intent: Centralize communication among objects.
- Use when: Many-to-many object interactions are hard to maintain.
- Watch out: Mediator can become overly complex.
- Review signal: Colleagues directly reference each other in a mesh.

```python
class ChatMediator:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def send(self, sender, msg):
        return [u.receive(sender, msg) for u in self.users if u != sender]

class User:
    def __init__(self, name, mediator):
        self.name, self.mediator = name, mediator

    def receive(self, sender, msg):
        return f"{self.name} got {msg} from {sender.name}"
```

### 18) Memento
- Intent: Capture and restore object state without exposing internals.
- Use when: Undo/rollback features.
- Watch out: Large snapshots can consume memory.
- Review signal: Undo implemented by duplicating many mutable fields manually.

```python
class EditorMemento:
    def __init__(self, text):
        self.text = text

class Editor:
    def __init__(self):
        self.text = ""

    def type(self, txt):
        self.text += txt

    def save(self):
        return EditorMemento(self.text)

    def restore(self, memento):
        self.text = memento.text
```

### 19) Observer
- Intent: One-to-many notification on state changes.
- Use when: Event-driven updates (UI refresh, async notifications).
- Watch out: Memory leaks if observers are never unsubscribed.
- Review signal: Subject calls dependent modules directly.

```python
class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, obs):
        self.observers.append(obs)

    def notify(self, data):
        return [obs.update(data) for obs in self.observers]

class Observer:
    def update(self, data):
        return f"got {data}"
```

### 20) State
- Intent: Change behavior by swapping state objects.
- Use when: Workflows with explicit lifecycle states.
- Watch out: Transition rules must be explicit and test-covered.
- Review signal: Giant state-based if/elif blocks.

```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def next(self, ctx): ...

class Draft(State):
    def next(self, ctx):
        ctx.state = Published()

class Published(State):
    def next(self, ctx):
        return "already published"

class Document:
    def __init__(self):
        self.state = Draft()

    def publish(self):
        return self.state.next(self)
```

### 21) Strategy
- Intent: Encapsulate interchangeable algorithms behind one interface.
- Use when: Different policies/rules selected at runtime.
- Watch out: If only one strategy exists, keep it simple first.
- Review signal: Algorithm choice through repeated conditionals.

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): ...

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        return sorted(data)

class SortContext:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def run(self, data):
        return self.strategy.sort(data)
```

### 22) Template Method
- Intent: Define algorithm skeleton and let subclasses fill steps.
- Use when: Shared workflow with variable stages.
- Watch out: Deep inheritance can reduce flexibility.
- Review signal: Copy-paste workflows with only one step different.

```python
from abc import ABC, abstractmethod

class DataPipeline(ABC):
    def run(self):
        raw = self.read()
        cooked = self.transform(raw)
        return self.write(cooked)

    @abstractmethod
    def read(self): ...

    @abstractmethod
    def transform(self, data): ...

    @abstractmethod
    def write(self, data): ...
```

### 23) Visitor
- Intent: Add new operations over object structure without changing element classes.
- Use when: Stable object model, frequently changing operations.
- Watch out: Adding new element type requires all visitors to change.
- Review signal: Same traversal logic duplicated across many operations.

```python
from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor): ...

class FileNode(Element):
    def accept(self, visitor):
        return visitor.visit_file(self)

class Visitor(ABC):
    @abstractmethod
    def visit_file(self, file_node): ...

class SizeVisitor(Visitor):
    def visit_file(self, file_node):
        return 100
```

## Quick Revision Order (high interview frequency)
1. Strategy
2. Factory Method
3. Abstract Factory
4. Adapter
5. Decorator
6. Observer
7. State
8. Facade
9. Builder
10. Command
