"""
The following code represents a class to build Turing Machines easier and swiftly.

@:author Angel Cruz Mora
@:date 11/26/2024
"""
from array import ArrayType
##
## Dependencies
from typing import List

class Node:
    """
        Class to modelate a node of a linked list, which it will
        represent the tape of the Turing Machine.

    """
    def __init__(self, value= "", left= None, right= None) -> None:
        self.value= value
        self.left= None
        self.right= None


class TuringMachine:
    """
        Class to build Turing Machines

        Attribute:
                    transitions dict A dictionary to store the model transitions, based on the
                                     tape value.
                                     For instance.
                                            transitions = {"q0": {0: ["q1", 0, "R"], 1: ["q2", 1, "L"]}}
    """
    __transitions= {}
    __tape= Node()

    def __init__(self, initial_state:int,  final_states:List[int]) -> None:
        """
            Main constructor to initiliaze the Turing Machine.

            :param initial_state: The state where the Turing Machine will start.
            :param final_states: The states where the Turing Machine will halt and accept the string.
        """
        self.initial_state= initial_state
        self.final_state= set(final_states)

    def add_transition(self, from_state, to_state, when_tape, write_in_tape, move_to) -> None:
        """
            Method to add a transition to the Turing Machine.

            :param from_state: State where the transition will start.
            :param to_state: The state we are heading towards.
            :param when_tape: The value that the tape must have to execute the transition.
            :param write_in_tape: The value we will use to overwrite in the current cell.
            :param move_to: The direction in which we will move on the tape, either right (R) or left (L).
        """
        if from_state not in self.__transitions.keys():
            self.__transitions[from_state]= {when_tape : [to_state,write_in_tape,move_to]}

        self.__transitions[from_state][when_tape]= [to_state,write_in_tape,move_to]

    def del_transition(self, from_state, when_tape) -> None:
        if from_state in self.__transitions.keys() and when_tape in self.__transitions[from_state].keys():
            del self.__transitions[from_state][when_tape]

    def get_configuration(self) -> None:
        values_in_tape= set()
        [values_in_tape.update(_dict.keys()) for (state,_dict) in self.__transitions.items()]
        states= ",".join([f"q{_}" for _ in self.__transitions.keys()])
        final_states= ",".join(f"q{_}" for _ in self.final_state)
        print("Configuration. \n\tM= ({{{}}}, NaN, {}, S, q{}, B, {{{}}})\n".format(states,values_in_tape,self.initial_state,final_states))

        for (state,_dict) in self.__transitions.items():
            for tape, action in _dict.items():
                print("S(q{},{})= (q{},{},{})".format(state,tape,action[0],action[1],action[2]), end= ";\t")
            print()


if __name__ == "__main__":
    machine= TuringMachine(initial_state= 0, final_states= [2])
    machine.add_transition(from_state= 0, to_state= 1, when_tape= 0, write_in_tape= "X", move_to= "R")
    machine.add_transition(from_state= 1, to_state= 2, when_tape= 1, write_in_tape= "X", move_to= "R")

    # Remove the transition S(q0, 0)= (q1,X,'R')
    machine.del_transition(from_state= 0, when_tape= 0)
    machine.get_configuration()


