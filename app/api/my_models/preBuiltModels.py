"""
    Python module to pre-build Turing Machines and Nondeterministic Finite Automatons (NFAs)

    @:author Angel Cruz
    @: 11/30/2024
"""

# Turing Machine package
from .TuringMachine import TuringMachine
from .NFA import NFA

"""
    Pre-Built Turing Machines ======================================================================
"""

class BinaryTuringMachine:
    """
        Pre-built Turing Machine for converting unary numbers into binary numbers.
    """
    def __init__(self, *args):
        # Initialize Turing Machine
        self.machine= TuringMachine(initial_state= 0, final_states= [5])
        # Add Configuration
        self.machine.add_transition(from_state="0", to_state="1", when_tape="1", write_in_tape="", move_to="R")
        self.machine.add_transition(from_state="1", to_state="1", when_tape="1", write_in_tape="1", move_to="R")
        self.machine.add_transition(from_state="1", to_state="2", when_tape="=", write_in_tape="=", move_to="R")
        self.machine.add_transition(from_state="1", to_state="2", when_tape="", write_in_tape="=", move_to="R")
        self.machine.add_transition(from_state="2", to_state="2", when_tape="1", write_in_tape="1", move_to="R")
        self.machine.add_transition(from_state="2", to_state="3", when_tape="", write_in_tape="1", move_to="L")
        self.machine.add_transition(from_state="2", to_state="3", when_tape="0", write_in_tape="1", move_to="L")
        self.machine.add_transition(from_state="3", to_state="3", when_tape="1", write_in_tape="0", move_to="L")
        self.machine.add_transition(from_state="3", to_state="4", when_tape="=", write_in_tape="=", move_to="L")
        self.machine.add_transition(from_state="4", to_state="4", when_tape="1", write_in_tape="1", move_to="L")
        self.machine.add_transition(from_state="4", to_state="0", when_tape="", write_in_tape="", move_to="R")
        self.machine.add_transition(from_state="0", to_state="5", when_tape="=", write_in_tape="", move_to="R")

    def is_accepted(self, string:str, *args) -> bool:
        return self.machine.validate_string(string)

    def get_tape(self, *args) -> str:
        return self.machine.get_tape(reverse= True)




    """
        Pre-Built Non-Deterministic Finite Automaton ======================================================================
    """

class OperationValidatorNFA:
    """
        Pre-built NFA to validate mathematical operations with numbers, operators, and scientific notation.
    """
    def __init__(self):
        self.model = NFA(initial_state="0", final_states=["5"])
        self._build_model()

    def _build_model(self):
        # States for numbers
        self.model.add_transition("0", "1", '-')
        self.model.add_transition("0", "1", '+')
        for digit in "0123456789":
            self.model.add_transition("0", "1", digit)
            self.model.add_transition("1", "1", digit)
            self.model.add_transition("2", "2", digit)
            self.model.add_transition("3", "3", digit)

        # Decimal points
        self.model.add_transition("1", "2", ".")

        # Scientific notation
        self.model.add_transition("1", "3", "e")
        self.model.add_transition("2", "3", "e")
        self.model.add_transition("3", "4", "-")
        self.model.add_transition("3", "4", "+")
        for digit in "0123456789":
            self.model.add_transition("3", "4", digit)
            self.model.add_transition("4", "4", digit)

        # Operators
        for operator in ["+", "-", "*", "/"]:
            self.model.add_transition("1", "0", operator)
            self.model.add_transition("2", "0", operator)
            self.model.add_transition("4", "0", operator)

        # Final state
        self.model.add_transition("1", "5", "")
        self.model.add_transition("2", "5", "")
        self.model.add_transition("4", "5", "")

    def is_accepted(self, expression: str) -> bool:
        return self.model.validate_string(expression)
