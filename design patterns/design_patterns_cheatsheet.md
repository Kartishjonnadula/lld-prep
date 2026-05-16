# Essential Design Patterns Cheat Sheet

## 1. Singleton Pattern

### Purpose
Only one instance of a class should exist.

### Use Cases
- Logger
- Config manager
- Cache manager

### Example
```python
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Mental Model
> Global shared object

---

# 2. Factory Pattern

### Purpose
Create objects without exposing creation logic.

### Bad Code
```python
if payment_type == "upi":
    return UPIPayment()
elif payment_type == "card":
    return CardPayment()
```

### Better Factory Version
```python
class UPIPayment:
    pass

class CardPayment:
    pass

class PaymentFactory:

    registry = {
        "upi": UPIPayment,
        "card": CardPayment
    }

    @classmethod
    def create(cls, payment_type):

        payment_class = cls.registry.get(payment_type)

        if not payment_class:
            raise ValueError("Unsupported payment")

        return payment_class()
```

### Mental Model
> Centralize object creation

### Why It Helps
- Removes scattered if-else
- Easier extension
- Cleaner code

---

# 3. Strategy Pattern

### Purpose
Switch behavior dynamically.

### Example
```python
class UPIPayment:
    def pay(self):
        print("UPI")

class CardPayment:
    def pay(self):
        print("CARD")

class PaymentService:

    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self):
        self.strategy.pay()
```

### Mental Model
> Interchangeable behaviors

### Real Example
- Payment methods
- Sorting strategies
- Compression algorithms

---

# 4. Observer Pattern

### Purpose
Notify multiple objects automatically.

### Example
```python
class Subscriber:
    def update(self, msg):
        print(msg)

class Channel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, msg):
        for sub in self.subscribers:
            sub.update(msg)
```

### Mental Model
> Publish → Subscribers react

### Used In
- Kafka
- Event systems
- Notifications
- Webhooks

---

# 5. Builder Pattern

### Purpose
Build complex objects step-by-step.

### Example
```python
class UserBuilder:

    def set_name(self, name):
        return self

    def set_age(self, age):
        return self

    def build(self):
        return User()
```

### Mental Model
> Piece-by-piece object creation

---

# 6. Decorator Pattern

### Purpose
Add features without modifying original class.

### Example
```python
class Coffee:
    def cost(self):
        return 100

class MilkDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20
```

### Mental Model
> Wrap object to add behavior

### Used In
- Middleware
- Logging
- Authentication

---

# 7. Adapter Pattern

### Purpose
Make incompatible interfaces work together.

### Example
```python
class OldPrinter:
    def old_print(self):
        print("printing")

class Adapter:

    def __init__(self, printer):
        self.printer = printer

    def print(self):
        self.printer.old_print()
```

### Mental Model
> Translator between systems

---

# 8. Command Pattern

### Purpose
Convert action into object.

### Example
```python
class Light:
    def on(self):
        print("ON")

class LightCommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
```

### Mental Model
> Actions as objects

### Used In
- Job queues
- Undo/Redo
- Task schedulers

---

# 9. Template Method Pattern

### Purpose
Define algorithm skeleton.

### Example
```python
class Parser:

    def parse(self):
        self.read()
        self.process()

    def read(self):
        pass

    def process(self):
        pass
```

### Mental Model
> Common flow with customizable steps

---

# 10. Repository Pattern

### Purpose
Separate business logic from database logic.

### Example
```python
class UserRepository:

    def get_user(self, user_id):
        pass

class UserService:

    def __init__(self, repo):
        self.repo = repo
```

### Mental Model
> Database access abstraction

---

# Most Important Patterns For Interviews

## Must Know
1. Factory
2. Strategy
3. Observer
4. Singleton
5. Builder

---

# Pattern Identification Cheat Sheet

| Situation | Pattern |
|---|---|
| Too many if-else | Factory / Strategy |
| Need interchangeable behavior | Strategy |
| Need notifications | Observer |
| Need shared object | Singleton |
| Need wrapper functionality | Decorator |
| Need translation layer | Adapter |
| Complex object creation | Builder |

---

# Learning Order

1. Factory
2. Strategy
3. Observer
4. Singleton
5. Builder
6. Decorator
7. Adapter
8. Command
9. Template Method

---

# Golden Rule

Design patterns are reusable solutions to recurring software design problems.

Always ask:
1. What problem does this solve?
2. What bad code does it avoid?
3. Where is it used in real systems?
