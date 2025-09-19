# PLP Week 5-Object-Oriented Programming (OOP) Assignment

This repository contains a short Python assignment from PLP that demonstrates basic Object-Oriented Programming (OOP) concepts: classes, encapsulation, constructors, methods, inheritance/polymorphism, and simple usage examples.

## Files

- `oop.py` — The assignment source file. It defines a `Smartphone` class that demonstrates encapsulation and methods for describing and upgrading storage. It also includes a small polymorphism example using `car` and `plane` classes with a shared `move()` method.

## Learning objectives

- Practice defining Python classes and constructors
- Use instance attributes (public and private) and methods
- Demonstrate encapsulation via name-mangled (private) attributes
- Implement and observe polymorphism (multiple classes implementing the same method name)
- Run simple examples and inspect output

## What the code does (summary)

- `Smartphone` class:
  - Constructor: `__init__(self, color, type, storage)` — initializes `color`, `type`, and a private storage attribute (`__storage`).
  - `describe_phone(self)` — returns a human-readable description string.
  - `get_storage(self)` — accessor that returns the private storage value.
  - `upgrade_storage(self, extra)` — increases storage by `extra` if `extra > 0` and returns a success message; otherwise it prints an error.

- Polymorphism example:
  - Two simple classes, `car` and `plane`, each implement a `move()` method. A small loop instantiates each and calls `move()` to demonstrate that classes can implement the same interface differently.

## How to run

Open a terminal (PowerShell on Windows) in the project folder and run:

```powershell
python oop.py
```

Expected output (example):

```
This is a white samsung with 8GB storage.
You have upgraded your samsung to 72GB successfully
Car is driving
Plane is cruising
```

Note: exact output may vary if you edit the example objects in `oop.py`.

## OOP concepts mapped to the code

- Encapsulation: `Smartphone.__storage` is a private attribute (name-mangled) that cannot be accessed directly as `instance.__storage` from outside the class.
- Constructors: `__init__` initializes object state with unique values per instance.
- Methods: `describe_phone`, `get_storage`, and `upgrade_storage` operate on instance state.
- Polymorphism: `car.move()` and `plane.move()` implement the same method name with different behavior.

