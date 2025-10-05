# assignment-1-superhero-class
# 🦸 Assignment 1: Superhero Class Design

## 📚 Overview

This project is a Python class-based design for a **Superhero**, created as part of Assignment 1. The goal is to demonstrate object-oriented programming concepts including:

- Class creation
- Constructors (`__init__`)
- Methods
- Inheritance
- Polymorphism
- Encapsulation

---

## 🧱 Classes

### `Superhero`
Represents a generic superhero.

#### Attributes:
- `name`: The superhero's name
- `power`: Main superpower
- `health`: Current health points

#### Methods:
- `attack(target)`: Performs a basic attack on a target
- `heal(amount)`: Restores health
- `display_stats()`: Shows the superhero’s stats

### `FlyingSuperhero` (inherits from `Superhero`)
Represents a superhero that can fly.

#### Additional Attribute:
- `flight_speed`: Flying speed in km/h

#### Additional Method:
- `fly()`: Displays a flying message

#### Overridden Method:
- `attack(target)`: Customized attack message from the air (polymorphism)

---

## 💡 Concepts Demonstrated

| Concept         | Explanation                                        |
|-----------------|----------------------------------------------------|
| Class & Object  | Created with `class Superhero` and `FlyingSuperhero` |
| Constructor     | `__init__()` is used to initialize attributes      |
| Inheritance     | `FlyingSuperhero` inherits from `Superhero`        |
| Polymorphism    | `attack()` is overridden in the child class        |
| Encapsulation   | Attributes use underscore prefix (e.g., `_health`) |

---

## ▶️ How to Run

1. Clone or download the repository
2. Run the Python file using:

```bash
python superhero.py
