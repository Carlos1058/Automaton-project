from typing import List, Set


class NFA:
    """
        Class to build a Nondeterministic Finite Automaton.

        Methods:
                - add_transition(from_state:str, to_state:str, when_input:str) -> None
                - validate_string(string:str) -> bool
    """
    def __init__(self, initial_state: str, final_states: List[str]) -> None:
        """
            Main constructor
            :param initial_state: Str value, the state where the NFA will start.
            :param final_states: Str list, the final states of the NFA.
        """
        self.__transitions = {}  # Initialize transitions here
        self.__vocabulary = set()
        self.initial_state: str = initial_state
        self.final_states: Set[str] = set(final_states)

    def add_transition(self, from_state: str, to_state: str, when_input: str) -> None:
        """
            Method to add a transition to the NFA.

            :param from_state: Str value, where the transition will begin.
            :param to_state: Str value, the state we are heading towards.
            :param when_input: Str value, the input we need to execute the transition.
        """
        # Add state if it doesn't exist
        if from_state not in self.__transitions:
            self.__transitions[from_state] = {}
        # Add character if it doesn't exist
        if when_input not in self.__transitions[from_state]:
            self.__transitions[from_state][when_input] = []

        # Append transition
        self.__transitions[from_state][when_input].append(to_state)

    def validate_string(self, string: str) -> bool:
        """
            Method to validate the string.  We will use recursion
            and something similar to a DFS to traverse along the NFA,
            if we reach a final state and the string is empty, means
            that the string is accepted.
        """
        current_state = self.initial_state
        is_accepted = False

        def exec_transition(state: str, s: str):
            """
                Recursive function to validate the string.
            """
            nonlocal is_accepted

            # If the string is empty, and we reach a final state, then accept the string
            if s == "":
                if state in self.final_states:  # Check if we reach a final state
                    is_accepted = True
                    return
                elif "" not in self.__transitions.get(state, {}):  # Check if we have a lambda transition left
                    return

            # Check if the `state` is defined in transitions
            if state not in self.__transitions:
                return

            # Execute lambda transitions
            if "" in self.__transitions[state]:
                for direction in self.__transitions[state][""]:
                    exec_transition(direction, s)
                    if is_accepted:
                        return

            # Check if the input `s[0]` has a transition in the state `state`
            if s and s[0] not in self.__transitions[state]:
                return

            # Iterate along the transitions
            if s:
                for direction in self.__transitions[state][s[0]]:
                    exec_transition(direction, s[1:])
                    if is_accepted:  # If the string was already accepted then return
                        return

        # Execute recursive function
        exec_transition(current_state, string)
        # Retrieve answer
        return is_accepted


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
        for operator in ["+", "-", "*", "/", "^"]:
            self.model.add_transition("1", "0", operator)
            self.model.add_transition("2", "0", operator)
            self.model.add_transition("4", "0", operator)

        # Final state
        self.model.add_transition("1", "5", "")
        self.model.add_transition("2", "5", "")
        self.model.add_transition("4", "5", "")

    def is_accepted(self, expression: str) -> bool:
        return self.model.validate_string(expression)


if __name__ == "__main__":
    # Example usage for operation validation
    validator = OperationValidatorNFA()
    test_expression = "1.232323251e3+20*10.111/10-100^0.2"
    if validator.is_accepted(test_expression):
        print("Valid operation")
    else:
        print("Invalid operation")
