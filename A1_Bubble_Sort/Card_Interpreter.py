import sys
import os

# Memory Structures
datamem = [0] * 1000  # Data Memory
instrmem = []         # Instruction Memory
cardmem = []          # Card Reader (Input Cards)
next_card = 0         # Next card index
ip = 0                # Instruction Pointer

# Breakpoints and Debugging
BREAKPOINTS = set()
INSTRUCTION_VISITS = {}  # Track visits to each instruction pointer for loop detection
INFINITE_LOOP_THRESHOLD = 100  # Max allowed instruction visits to detect infinite loops

# Debugging Flags
INST_FLAG = True   # Set to True to enable instruction tracing
STEP_FLAG = False  # Set to True to enable step-by-step execution

# Exception Classes
class InterpreterError(Exception):
    """Base class for interpreter exceptions."""
    pass

class LogicError(InterpreterError):
    """Exception raised for logic errors in execution."""
    pass

class InfiniteLoopError(InterpreterError):
    """Exception raised for detecting an infinite loop."""
    pass

# Loader Function
def loader(filename):
    """Loads data, instructions, and input cards from the file."""
    global datamem, instrmem, cardmem
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    file_path = os.path.join(script_dir, filename)  # Construct the full file path

    with open(file_path, 'r') as infile:
        lines = infile.readlines()

    FLAG = '+9999999999'
    count = 0
    section = 'data'

    for line in lines:
        line = line.split('//')[0].strip()
        if not line or line.startswith('//') or line.startswith('<'):
            continue
        if line == FLAG:
            if section == 'data':
                section = 'instructions'
                count = 0
            elif section == 'instructions':
                section = 'input'
                count = 0
            else:
                break
            continue
        if section == 'data':
            datamem[count] = int(line.split()[0])  # Split to remove comment part
            count += 1
        elif section == 'instructions':
            instrmem.append(line.split()[0])  # Split to remove comment part
            count += 1
        elif section == 'input':
            cardmem.append(int(line.split()[0]))  # Split to remove comment part
            count += 1



# Instruction Parsing Function
def parse_instruction(instr):
    """Parses an instruction and returns the sign, operation, and operands."""
    sign = instr[0]
    oper = instr[1]
    op1 = int(instr[2:5])
    op2 = int(instr[5:8])
    op3 = int(instr[8:11])
    return sign, oper, op1, op2, op3

# Detect Infinite Loops and Logic Issues
def detect_logic_issues():
    """Detect potential logic errors and infinite loops during execution."""
    global ip

    # Detecting infinite loops: Count how often the same instruction is hit
    if ip not in INSTRUCTION_VISITS:
        INSTRUCTION_VISITS[ip] = 0
    INSTRUCTION_VISITS[ip] += 1

    if INSTRUCTION_VISITS[ip] > INFINITE_LOOP_THRESHOLD:
        raise InfiniteLoopError(f"Potential infinite loop detected at IP {ip}.")
    
# Trace Function
def trace(ip, sign, oper, op1, op2, op3):
    """Prints tracing information if tracing is enabled."""
    if INST_FLAG:
        print(f"IP: {ip:04}")
        print(f"Instruction: {sign}{oper}{op1:03}{op2:03}{op3:03}")
        print(f"Operands: op1={datamem[op1]}, op2={datamem[op2]}, op3={datamem[op3]}")
        print(f"Next Card Index: {next_card}")
        print(f"Data Memory Snapshot (0-10): {datamem[:25]}")
        print("-" * 40)
    if STEP_FLAG:
        input("Press Enter to continue...")

# Opcode Execution Functions
def p0(op1, op2, op3):
    """Opcode +0: Copy data."""
    datamem[op3] = datamem[op1]

def p1(op1, op2, op3):
    """Opcode +1: Add data."""
    datamem[op3] = datamem[op1] + datamem[op2]

def p2(op1, op2, op3):
    """Opcode +2: Multiply data."""
    datamem[op3] = datamem[op1] * datamem[op2]

def p5(op1, op2, op3):
    """Opcode +5: Jump if greater or equal."""
    global ip
    if datamem[op1] >= datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

# def p8(op1, op2, op3):
#     """Opcode +8: Input card reader."""
#     global next_card
#     if next_card < len(cardmem):
#         datamem[op3] = cardmem[next_card]
#         next_card += 1
#     else:
#         value = int(input(f"Input for address {op3}: "))
#         datamem[op3] = value

def p8(op1, op2, op3):
    """Opcode +8: Input card reader."""
    global next_card
    if next_card < len(cardmem):
        datamem[op3] = cardmem[next_card]
        next_card += 1
    else:
        # Use a default value for input to avoid manual intervention during testing
        default_value = 0  # You can change this to any default value you want
        print(f"No more cards in card reader. Using default value {default_value} for address {op3}.")
        datamem[op3] = default_value


def p9(op1, op2, op3):
    """Opcode +9: Halt the program."""
    print("Program halted.")
    sys.exit(0)

def n0(op1, op2, op3):
    """Opcode -0: No operation."""
    print("No operation.")

def n1(op1, op2, op3):
    """Opcode -1: Subtract data."""
    datamem[op3] = datamem[op1] - datamem[op2]

def n2(op1, op2, op3):
    """Opcode -2: Divide data."""
    if datamem[op2] != 0:
        datamem[op3] = datamem[op1] // datamem[op2]
    else:
        raise LogicError(f"Division by zero at IP {ip}.")

def n5(op1, op2, op3):
    """Opcode -5: Jump if less."""
    global ip
    if datamem[op1] < datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

def n8(op1, op2, op3):
    """Opcode -8: Print memory."""
    print(f"Memory[{op1}] = {datamem[op1]}")

# Execution Loop
def run_program():
    """
    Main execution loop of the interpreter.
    Fetches, decodes, and executes instructions, and detects issues.
    """
    global ip
    try:
        while True:
            if ip >= len(instrmem):
                print("End of instruction memory reached.")
                break
            current_instruction = instrmem[ip]
            sign, oper, op1, op2, op3 = parse_instruction(current_instruction)
            trace(ip, sign, oper, op1, op2, op3)

            # Detect logic issues and infinite loops before executing the instruction
            detect_logic_issues()

            ip += 1  # Increment IP after fetching instruction

            # Execute instruction based on sign and opcode
            if sign == '+':
                if oper == '0':
                    p0(op1, op2, op3)
                elif oper == '1':
                    p1(op1, op2, op3)
                elif oper == '2':
                    p2(op1, op2, op3)
                elif oper == '5':
                    p5(op1, op2, op3)
                    continue  # Jumped, so continue without incrementing IP
                elif oper == '8':
                    p8(op1, op2, op3)
                elif oper == '9':
                    p9(op1, op2, op3)
            elif sign == '-':
                if oper == '0':
                    n0(op1, op2, op3)
                elif oper == '1':
                    n1(op1, op2, op3)
                elif oper == '2':
                    n2(op1, op2, op3)
                elif oper == '5':
                    n5(op1, op2, op3)
                    continue  # Jumped, so continue without incrementing IP
                elif oper == '8':
                    n8(op1, op2, op3)
            else:
                raise LogicError(f"Invalid sign '{sign}' at IP {ip}.")

        # If the program reaches this point, it successfully finished
        print("Program finished successfully.")

    except InterpreterError as e:
        print(f"Interpreter Error: {e}")
    except InfiniteLoopError as e:
        print(f"Error: {e}")
        print(f"Potential infinite loop detected at IP {ip}.")
    except LogicError as e:
        print(f"Logic Error: {e}")

# Main Function
if __name__ == '__main__':
    filename = 'A1.dat'  # Replace with your actual filename
    loader(filename)
    run_program()