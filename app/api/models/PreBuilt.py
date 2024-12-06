"""
    Python module to pre-build Turing Machines

    @:author Angel Cruz
    @: 11/30/2024
"""
# Turing Machine module
from models.TuringMachine import TuringMachine


class BinaryMachineTuring:
    """
        Pre-built Turing Machine for converting unary numbers into binary numbers.
    """
    def __init__(self, *args):
        # Initialize Turing Machine
        self.machine= TuringMachine(initial_state= 0, final_states= [5])
        # Add Configuration
        self.machine.add_transition(from_state=0, to_state=1, when_tape=1, write_in_tape="", move_to="R")
        self.machine.add_transition(from_state=1, to_state=1, when_tape=1, write_in_tape=1, move_to="R")
        self.machine.add_transition(from_state=1, to_state=2, when_tape="=", write_in_tape="=", move_to="R")
        self.machine.add_transition(from_state=1, to_state=2, when_tape="", write_in_tape="=", move_to="R")
        self.machine.add_transition(from_state=2, to_state=2, when_tape="1", write_in_tape="1", move_to="R")
        self.machine.add_transition(from_state=2, to_state=3, when_tape="", write_in_tape="1", move_to="L")
        self.machine.add_transition(from_state=2, to_state=3, when_tape="0", write_in_tape="1", move_to="L")
        self.machine.add_transition(from_state=3, to_state=3, when_tape="1", write_in_tape="0", move_to="L")
        self.machine.add_transition(from_state=3, to_state=4, when_tape="=", write_in_tape="=", move_to="L")
        self.machine.add_transition(from_state=4, to_state=4, when_tape="1", write_in_tape="1", move_to="L")
        self.machine.add_transition(from_state=4, to_state=0, when_tape="", write_in_tape="", move_to="R")
        self.machine.add_transition(from_state=0, to_state=5, when_tape="=", write_in_tape="", move_to="R")

    def is_accepted(self, string:str, *args) -> bool:
        return self.machine.validate_string(string)

    def get_tape(self, *args) -> str:
        return self.machine.get_tape(reverse= True)



if __name__ == "__main__":
    model= BinaryMachineTuring()

    if model.is_accepted("1111111"): # Number 7
        print(model.get_tape())