from enum import Enum

INPUT_FILE = './input/day1.txt'

class Turn(Enum):
    LEFT = "L"
    RIGHT = "R"

class Input:
    def __init__(self, turn: Turn, num: int):
        self.turn: Turn = turn
        self.num: int = num

class DialState:
    def __init__(self, curr_state: int = 0, num_zeros: int = 0):
        self.curr_state: int = curr_state
        self.num_zeros: int = num_zeros

    def turn_dial(self, inp: Input):
        if inp.turn == Turn.RIGHT:
            self.curr_state += inp.num
        else:
            self.curr_state -= inp.num

        if self.curr_state % 100 == 0:
            self.num_zeros += 1

def parse_inputs(inputs_str: str) -> list[Input]:
    lines = inputs_str.splitlines()
    inputs = []

    for line in lines:
        if line[0] == "R":
            inp = Input(Turn.RIGHT, int(line[1:]))
        else:
            inp = Input(Turn.LEFT, int(line[1:]))
        inputs.append(inp)

    return inputs

def main():
    with open(INPUT_FILE, 'r') as input_file:
        input_content = input_file.read()

    inputs = parse_inputs(input_content)
    state = DialState(50)

    for inp in inputs:
        state.turn_dial(inp)

    print(state.num_zeros)

if __name__ == '__main__':
    main()