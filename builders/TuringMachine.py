"""
The following code represents a class to build Turing Machines easier and swiftly.

@:author Angel Cruz Mora
@:date 11/26/2024
"""

## Dependencies
from typing import List


class Node:
    """
        Class to modelate a node of a linked list, which it will
        represent the tape of the Turing Machine.

    """
    def __init__(self, value= "", left= None, right= None) -> None:
        self.value= value
        self.left= left
        self.right= right


class TuringMachine:
    """
        Class to build Turing Machines.

        Note. The character "" is considered as the blank value.
        Attribute:
            :param transitions dict A dictionary to store the model transitions, based on the tape value.
                                    For instance.
                                        transitions = {"q0": {0: ["q1", 0, "R"], 1: ["q2", 1, "L"]}}
            :param tape Node The linked list that we will use as the Turing Machine tape.
    """
    __transitions= {}
    __tape= Node()

    def __init__(self, initial_state:str,  final_states:List[str]) -> None:
        """
            Main constructor to initiliaze the Turing Machine.

            :param initial_state: The state where the Turing Machine will start.
            :param final_states: The states where the Turing Machine will halt and accept the string.
        """
        if not type(final_states) == list:
            raise TypeError("final_states variable must be a list.")
        initial_state= str(initial_state)
        final_states= [str(x) for x in final_states]
        self.initial_state= initial_state
        self.final_state= set(final_states)

    def add_transition(self, from_state:str, to_state:str, when_tape:str, write_in_tape:str, move_to:str) -> None:
        """
            Method to add a transition to the Turing Machine.

            :param from_state: State where the transition will start.
            :param to_state: The state we are heading towards.
            :param when_tape: The value that the tape must have to execute the transition.
            :param write_in_tape: The value we will use to overwrite in the current cell.
            :param move_to: The direction in which we will move on the tape, either right (R) or left (L).
        """
        from_state= str(from_state)
        to_state= str(to_state)
        when_tape= str(when_tape)
        write_in_tape= str(write_in_tape)
        if from_state not in self.__transitions.keys():
            self.__transitions[from_state]= {when_tape : [to_state,write_in_tape,move_to]}

        self.__transitions[from_state][when_tape]= [to_state,write_in_tape,move_to]

    def del_transition(self, from_state:str, when_tape:str) -> None:
        """
            Method to remove transitions.

            :param from_state: State where the transition starts.
            :param when_tape: The value that the tape must have to execute the transition.
        """
        if from_state in self.__transitions.keys() and when_tape in self.__transitions[from_state].keys():
            del self.__transitions[from_state][when_tape]

    def get_configuration(self) -> None:
        """
            Method for displaying the configuration of the Turing Machine, for example,
            the transitions that the machine can execute.
        """
        values_in_tape= set()
        [values_in_tape.update(_dict.keys()) for (state,_dict) in self.__transitions.items()]
        states= ",".join([f"q{_}" for _ in self.__transitions.keys()])
        final_states= ",".join(f"q{_}" for _ in self.final_state)
        print("Configuration. \n\tM= ({{{}}}, NaN, {}, S, q{}, B, {{{}}})\n".format(states,values_in_tape,self.initial_state,final_states))

        for (state,_dict) in self.__transitions.items():
            for tape, action in _dict.items():
                print("S(q{},{})= (q{},{},{})".format(state,tape,action[0],action[1],action[2]), end= ";\t")
            print()

    def __insert_in_tape(self, string:str) -> None:
        """
            Method for inserting the initial string into the tape.

            :param string: The input string.
        """
        # Reset Tape
        self.__tape= Node()
        aux1= self.__tape
        for c in string:
            aux2= Node(value= c, left= aux1)
            aux1.right= aux2
            aux1= aux2
        self.__tape= self.__tape.right

    def validate_string(self, string:str) -> bool:
        """
            Method to execute the Turing Machine and validate if the input string was
            either accepted or rejected.

            :param string: The input string to validate.
            :return: Bool value, whether the string was either accepted or rejected.
        """
        self.__insert_in_tape(string)
        current_state= self.initial_state
        current_cell = self.__tape

        while current_state in self.__transitions.keys() and current_cell.value in self.__transitions[current_state].keys():
            action= self.__transitions[current_state][current_cell.value]
            # Change current state and the value on the tape
            current_state, current_cell.value= action[:2]
            # Move either right or left on the tape
            aux= current_cell
            current_cell= current_cell.right if action[-1] == "R" else current_cell.left
            # Create a new Node in case it's None
            if not current_cell:
                if action[-1] == "R":
                    current_cell= Node(left= aux)
                    aux.right= current_cell
                else:
                    current_cell= Node(right= aux)
                    aux.left= current_cell

        # Check if the current state is final.
        if current_state in self.final_state:
            return True
        else:
            return False

    def get_tape(self, reverse= False) -> str:
        """
            Method to retrieve the tape once we have validated the string,
            in case we want the final string.

            :param reverse: Reverse the final string, from back to front.
            :return: A str value, corresponding to the final string in the tape.
        """
        head= self.__tape

        tape= ""
        while head:
            tape += head.value
            head= head.right

        if reverse:
            tape= tape[::-1]

        return tape



if __name__ == "__main__":
    """
        Turing Machine for converting unary numbers into binary numbers.
    """
    machine= TuringMachine(initial_state= 0, final_states= [5])
    # Configuration
    machine.add_transition(from_state= 0, to_state= 1, when_tape= 1, write_in_tape= "", move_to= "R")
    machine.add_transition(from_state= 1, to_state= 1, when_tape= 1, write_in_tape= 1, move_to= "R")
    machine.add_transition(from_state= 1, to_state= 2, when_tape= "=", write_in_tape= "=", move_to= "R")
    machine.add_transition(from_state= 1, to_state= 2, when_tape= "", write_in_tape= "=", move_to= "R")
    machine.add_transition(from_state= 2, to_state= 2, when_tape= "1", write_in_tape= "1", move_to= "R")
    machine.add_transition(from_state= 2, to_state= 3, when_tape= "", write_in_tape= "1", move_to= "L")
    machine.add_transition(from_state= 2, to_state= 3, when_tape= "0", write_in_tape= "1", move_to= "L")
    machine.add_transition(from_state= 3, to_state= 3, when_tape= "1", write_in_tape= "0", move_to= "L")
    machine.add_transition(from_state= 3, to_state= 4, when_tape= "=", write_in_tape= "=", move_to= "L")
    machine.add_transition(from_state= 4, to_state= 4, when_tape= "1", write_in_tape= "1", move_to= "L")
    machine.add_transition(from_state= 4, to_state= 0, when_tape= "", write_in_tape= "", move_to= "R")
    machine.add_transition(from_state= 0, to_state= 5, when_tape= "=", write_in_tape= "", move_to= "R")

    machine.get_configuration()


    print("""
        Evaluating the string. '11111'
    """)
    is_accepted= machine.validate_string(string= "1" * 5)
    in_tape= machine.get_tape(reverse= True)
    print("Is accepted? {}".format(is_accepted))
    print("Tape. {}".format(in_tape))

