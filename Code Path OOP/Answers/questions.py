

# PROBLEM 1
# ---------
# Design a vending machine that uses all six concepts at least once: 

# two enums,
# one interface, 
# one composition relationship, 
# one aggregation relationship, one
# association, 
# and one injected dependency.

# Write class skeletons only - attributes and method signatures, no full bodies -
# and label each relationship in a comment naming which of the four it is.

# Note: a design is more than a pile of classes - specifically, every relationship
# must be justified by the lifetime test, not by convenience. Write the
# justification next to each label.
# Evaluate the time and space complexity of `select_product()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.


from abc import ABC, abstractmethod
from enum import Enum


# ---------- ENUM #1 ----------
class MachineState(Enum):
    IDLE = "idle"
    PRODUCT_SELECTED = "product_selected"
    DISPENSING = "dispensing"
    OUT_OF_SERVICE = "out_of_service"


# ---------- ENUM #2 ----------
class PaymentStatus(Enum):
    APPROVED = "approved"
    DECLINED = "declined"
    INSUFFICIENT_FUNDS = "insufficient_funds"


# ---------- INTERFACE ----------
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount_given_cents: int, price_cents: int) -> PaymentStatus: ...

    @abstractmethod
    def refund(self, amount_cents: int) -> None: ...


# this class is for people who paid with cash 
class CashPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount_given_cents: int, price_cents: int) -> PaymentStatus: ...
    def refund(self, amount_cents: int) -> None: ...

# this class is for people who paid with card 
class CardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount_given_cents: int, price_cents: int) -> PaymentStatus: ...
    def refund(self, amount_cents: int) -> None: ...




class Product:
    def __init__(self, name: str, price_cents: int):
        self.name: str = name
        self.price_cents: int = price_cents


class Slot:
    def __init__(self, code: str, capacity: int):
        self.code = code
        self.capacity = capacity
        self.quantity: int = 0
        # AGGREGATION (Slot -> Product)
        # Lifetime test: a Product exists in the supplier's catalog before it is
        # loaded into a slot, and keeps existing after the slot is emptied or the
        # machine is scrapped. The slot holds a long-lived reference but does not
        # create or destroy the Product. Many slots (or machines) can share it.
        self.product: Product 

    def load(self, product: Product, quantity: int) -> None: ...
    def is_available(self) -> bool: ...
    def decrement(self) -> None: ...


class VendingMachine:
    def __init__(self, slot_codes: list[str], slot_capacity: int,
                 payment_processor: PaymentProcessor):
        # COMPOSITION (VendingMachine -> Slot)
        # Lifetime test: slots are created inside this constructor and are
        # reachable only through this machine. A slot is a physical row of
        # this cabinet; it has no meaning before the machine exists and is
        # destroyed with it. No other object holds a Slot.
        
        # will look like: apple ["A1", 5]
        self._slots: dict[str, Slot] = {}
        
        for code in slot_codes:
            self._slots[code] = Slot(code, slot_capacity)

        # INJECTED DEPENDENCY (VendingMachine -> PaymentProcessor)
        # Lifetime test: the processor is created by the caller, outlives any
        # single machine, and can be swapped (cash vs. card vs. a mock in tests)
        # without changing this class. The machine depends on the interface,
        # never on a concrete class, and never constructs it.
        self._payment_processor = payment_processor

        self._state = MachineState.IDLE
        self._selected_code: str | None = None


    def select_product(self, code: str) -> int: ...          # returns price in cents
    def insert_payment(self, amount_cents: int) -> PaymentStatus: ...
    def dispense(self) -> Product: ...
    def cancel(self) -> None: ...
    def restock(self, code: str, product: Product, quantity: int) -> None: ...


class Technician:
    def __init__(self, name: str, employee_id: str):
        self.name: str = name
        self.employee_id: str = employee_id

    # ASSOCIATION (Technician -- VendingMachine)
    # Lifetime test: neither creates, owns, or stores the other. A technician
    # services many machines over a career; a machine is serviced by many
    # technicians. The link exists only for the duration of this call and both
    # objects live on independently afterward.
    def service(self, machine: VendingMachine, code: str,
                product: Product, quantity: int) -> None: ...