"""
    The following class represents an implementation of a
    Nondeterministic Finite Automaton, which you can use to build any
    NFA or DFA that you like. This is a general class to implement
    more easily Automatons.

    @author Angel Cruz
    @date 12/08/2024
"""
from typing import List, Set


class NFA:
    """
        Class to build a Nondeterministic Finite Automaton.

        Methods:
                - add_transition(from_state:str, to_state:str, when_input:str) -> None
                - validate_string(string:str) -> bool
    """
    __transitions= {}
    __vocabulary= set()

    def __init__(self, initial_state:str, final_states:List[str]) -> None:
        """
            Main constructor
            :param initial_state: Str value, the state where the NFA will start.
            :param final_states: Str list, the final states of the NFA.
        """
        self.initial_state:str= initial_state
        self.final_states:Set[str]= set(final_states)


    def add_transition(self, from_state:str, to_state:str, when_input:str) -> None:
        """
            Method to add a transition to the NFA.

            :param from_state: Str value, where the transition will begin.
            :param to_state: Str value, the state we are heading towards.
            :param when_input: Str value, the input we need to execute the transition.
        """
        # Add state if it doesn't exist
        if not from_state in self.__transitions.keys():
            self.__transitions[from_state]= {}
        # Add character if it doesn't exist
        if not when_input in self.__transitions[from_state].keys():
            self.__transitions[from_state][when_input]= []

        # Append transition
        self.__transitions[from_state][when_input].append(to_state)

    def validate_string(self, string:str) -> bool:
        """
            Method to validate the string.  We will use recursion
            and something similar to a DFS to traverse along the NFA,
            if we reach a final state and the string is empty, means
            that the string is accepted.
        """
        current_state= self.initial_state
        is_accepted= False

        def exec_transition(state:str, s:str):
            """
                Recursive function to validate the string.
            """
            nonlocal is_accepted

            # If the string is empty, and we reach a final state, then accept the string
            if s == "":
                if state in self.final_states: # Check if we reach a final state
                    is_accepted= True
                    return
                elif not "" in self.__transitions[state].keys(): # Check if we have a lambda transition left
                    return

            # Check if the `state` is defined in transitions
            if not state in self.__transitions.keys():
                return

            # Execute lambda transitions
            if "" in self.__transitions[state].keys():
                for direction in self.__transitions[state][""]:
                    exec_transition(direction, s)
                    if is_accepted:
                        return

            # Check if the input `s[0]` has a transition in the state `state`
            if not s[0] in self.__transitions[state].keys():
                return

            # Iterate along the transitions
            for direction in self.__transitions[state][s[0]]:
                exec_transition(direction, s[1:])
                if is_accepted: # If the string was already accepted then return
                    return

        # Execute recursive function
        exec_transition(current_state, string)
        # Retrieve answer
        return is_accepted


if __name__ == "__main__":
    """
        NFA to accept strings formed with n `a`s,
        where n could be:
                            - an even number
                            - 3 or 5
    """
    # model= NFA(initial_state= "0", final_states= ["3", "5", "7"])
    #
    # # q0
    # model.add_transition(from_state="0", to_state="1", when_input="a")
    # model.add_transition(from_state="0", to_state="4", when_input="a")
    # #q1
    # model.add_transition(from_state="1", to_state="2", when_input="a")
    # # q2
    # model.add_transition(from_state="2", to_state="3", when_input="a")
    # # q3
    # model.add_transition(from_state="3", to_state="6", when_input="a")
    # # q4
    # model.add_transition(from_state="4", to_state="5", when_input="a")
    # # q5
    # model.add_transition(from_state="5", to_state="4", when_input="a")
    # # q6
    # model.add_transition(from_state="6", to_state="7", when_input="a")

    """
        NFA to test the following strings:
                - 00
                - 01001 # Accepted
                - 10010
                - 000   # Accepted
                - 0000
                
    """
    model = NFA(initial_state="0", final_states=["1"])
    # q0
    model.add_transition(from_state="0", to_state="1", when_input="0")
    model.add_transition(from_state="0", to_state="1", when_input="1")
    # q1
    model.add_transition(from_state="1", to_state="2", when_input="0")
    model.add_transition(from_state="1", to_state="2", when_input="")
    model.add_transition(from_state="1", to_state="1", when_input="1")
    model.add_transition(from_state="1", to_state="0", when_input="0")
    # q2
    model.add_transition(from_state="2", to_state="1", when_input="1")

    if model.validate_string(string= "000"):
        print("Aceptada")
    else:
        print("No Aceptada")
