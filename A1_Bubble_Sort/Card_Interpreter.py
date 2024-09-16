import sys

"""
This Python script is an interpreter for a pseudocode language.
It simulates the execution of a program written in this language,
which includes loading instructions and data from a file, parsing
and executing instructions, managing memory, and handling input/output.

The interpreter supports various operations defined by opcodes,
handles conditional and unconditional jumps, and provides debugging
features such as instruction tracing and step-by-step execution.

Key components of the interpreter:

- Memory structures: Data memory, instruction memory, and input cards.
- Loader function: Reads the program file and initializes memory.
- Instruction parsing: Extracts the sign, opcode, and operands.
- Execution loop: Fetches and executes instructions.
- Opcode functions: Implement the behavior of each opcode.
- Debugging features: Tracing and step execution.

Usage:

- Prepare a program file (e.g., 'A1.dat') with data, instructions,
  and input cards, separated by '+9999999999' flags.
- Set the filename in the script.
- Run the script to execute the program.
- Enable or disable tracing and step execution as needed.
"""

# Memory Structures
datamem = [0] * 1000  # Data Memory: an array of size 1000
instrmem = []         # Instruction Memory: list of instructions
cardmem = []          # Card Reader (Input Cards): list of input values
next_card = 0         # Index of the next input card to read
ip = 0                # Instruction Pointer: current instruction index

# Debugging Flags
INST_FLAG = True   # Set to True to enable instruction tracing
STEP_FLAG = False  # Set to True to enable step-by-step execution

# Loader Function
def loader(filename):
    """
    Loads the program from the given file into memory structures.
    Reads data memory, instruction memory, and input cards.
    """
    global datamem, instrmem, cardmem
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    FLAG = '+9999999999'  # Marker to separate sections in the file
    count = 0
    section = 'data'      # Current section: 'data', 'instructions', or 'input'

    for line in lines:
        line = line.strip()
        # Skip empty lines and comments
        if not line or line.startswith('//') or line.startswith('<'):
            continue
        if line == FLAG:
            # Switch to the next section upon encountering the FLAG
            if section == 'data':
                section = 'instructions'
                count = 0
            elif section == 'instructions':
                section = 'input'
                count = 0
            else:
                break  # No more sections
            continue
        if section == 'data':
            # Load data memory
            datamem[count] = int(line)
            count += 1
        elif section == 'instructions':
            # Load instruction memory
            instrmem.append(line)
            count += 1
        elif section == 'input':
            # Load input cards
            cardmem.append(int(line))
            count += 1

# Instruction Parsing Function
def parse_instruction(instr):
    """
    Parses an instruction string into sign, opcode, and operands.
    Returns the sign, opcode, and operands op1, op2, op3.
    """
    sign = instr[0]      # '+' or '-'
    oper = instr[1]      # Opcode character '0' to '9'
    op1 = int(instr[2:5])  # Operand 1: positions 2-4
    op2 = int(instr[5:8])  # Operand 2: positions 5-7
    op3 = int(instr[8:11]) # Operand 3: positions 8-10
    return sign, oper, op1, op2, op3

# Trace Function
def trace(ip, sign, oper, op1, op2, op3):
    """
    Outputs tracing information if tracing is enabled.
    Shows the current instruction and operand values.
    """
    if INST_FLAG:
        print(f"IP: {ip:04}")
        print(f"Instruction: {sign}{oper}{op1:03}{op2:03}{op3:03}")
        print(f"Operands:")
        print(f"  op1[{op1}] = {datamem[op1]}")
        print(f"  op2[{op2}] = {datamem[op2]}")
        print(f"  op3[{op3}] = {datamem[op3]}")
        print(f"Next Card Index: {next_card}")
        print(f"Data Memory Snapshot (0-10): {datamem[:16]}") # TODO - Change this to show the first 10 elements of datamem
        print("-" * 40)
    if STEP_FLAG:
        input("Press Enter to continue...")

# Opcode Execution Functions
def p0(op1, op2, op3):
    """Opcode +0: Move operation. datamem[op3] = datamem[op1]"""
    datamem[op3] = datamem[op1]
    print(f"Moved {datamem[op1]} from op1[{op1}] to op3[{op3}]")

def p1(op1, op2, op3):
    """Opcode +1: Addition. datamem[op3] = datamem[op1] + datamem[op2]"""
    datamem[op3] = datamem[op1] + datamem[op2]
    print(f"Added {datamem[op1]} and {datamem[op2]} to get {datamem[op3]}")

def p2(op1, op2, op3):
    """Opcode +2: Multiplication. datamem[op3] = datamem[op1] * datamem[op2]"""
    datamem[op3] = datamem[op1] * datamem[op2]
    print(f"Multiplied {datamem[op1]} and {datamem[op2]} to get {datamem[op3]}")

def p3(op1, op2, op3):
    """Opcode +3: Square. datamem[op3] = datamem[op1] squared"""
    datamem[op3] = datamem[op1] * datamem[op1]
    print(f"Squared {datamem[op1]} to get {datamem[op3]}")

def p4(op1, op2, op3):
    """Opcode +4: Conditional Jump if Equal. If datamem[op1] == datamem[op2],
    set ip to op3."""
    global ip
    if datamem[op1] == datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index
    print(f"Jumped to op3[{op3}] because {datamem[op1]} equals {datamem[op2]}")

def p5(op1, op2, op3):
    """Opcode +5: Conditional Jump if Greater or Equal.
    If datamem[op1] >= datamem[op2], set ip to op3."""
    global ip
    if datamem[op1] >= datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index
    print(f"Jumped to op3[{op3}] because {datamem[op1]} is greater than or equal to {datamem[op2]}")

def p6(op1, op2, op3):
    """Opcode +6: Array Load.
    datamem[op3] = datamem[op1 + datamem[op2]]"""
    base = op1
    index = datamem[op2]
    datamem[op3] = datamem[base + index]
    print(f"Loaded value from array at index {index} into op3[{op3}]")

def p7(op1, op2, op3):
    """Opcode +7: Increment and Test.
    Increment datamem[op1], and if it's less than datamem[op2],
    jump to op3."""
    global ip
    datamem[op1] += 1
    if datamem[op1] < datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index
    print(f"Incremented op1[{op1}] to {datamem[op1]} and checked against op2[{op2}]")

def p8(op1, op2, op3):
    """Opcode +8: Input operation. Reads input into datamem[op3]."""
    global next_card
    if next_card < len(cardmem):
        datamem[op3] = cardmem[next_card]
        next_card += 1
    else:
        value = int(input(f"Input for address {op3}: "))
        datamem[op3] = value
    print(f"Read input {datamem[op3]} for address {op3}")

def p9(op1, op2, op3):
    """Opcode +9: Halt execution."""
    print("Program halted.")
    sys.exit(0)
    

def n0(op1, op2, op3):
    """Opcode -0: No operation."""
    print("No operation.")

def n1(op1, op2, op3):
    """Opcode -1: Subtraction. datamem[op3] = datamem[op1] - datamem[op2]"""
    datamem[op3] = datamem[op1] - datamem[op2]
    print(f"Subtracted {datamem[op2]} from {datamem[op1]} to get {datamem[op3]}")

def n2(op1, op2, op3):
    """Opcode -2: Division. datamem[op3] = datamem[op1] // datamem[op2]"""
    datamem[op3] = datamem[op1] // datamem[op2]
    print(f"Divided {datamem[op1]} by {datamem[op2]} to get {datamem[op3]}")

def n3(op1, op2, op3):
    """Opcode -3: Square Root (not implemented)."""
    print("Square root operation not implemented.")

def n4(op1, op2, op3):
    """Opcode -4: Conditional Jump if Not Equal.
    If datamem[op1] != datamem[op2], set ip to op3."""
    global ip
    if datamem[op1] != datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index
    print(f"Jumped to op3[{op3}] because {datamem[op1]} is not equal to {datamem[op2]}")

def n5(op1, op2, op3):
    """Opcode -5: Conditional Jump if Less Than.
    If datamem[op1] < datamem[op2], set ip to op3."""
    global ip
    if datamem[op1] < datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index
    print(f"Jumped to op3[{op3}] because {datamem[op1]} is less than {datamem[op2]}")

def n6(op1, op2, op3):
    """Opcode -6: Array Store.
    datamem[op2 + datamem[op3]] = datamem[op1]"""
    base = op2
    index = datamem[op3]
    datamem[base + index] = datamem[op1]
    print(f"Stored {datamem[op1]} at index {index} in array at address {base}")

def n7(op1, op2, op3):
    """Opcode -7: No operation."""
    print("No operation.")

def n8(op1, op2, op3):
    """Opcode -8: Output operation. Prints datamem[op1]."""
    print(datamem[op1])

def n9(op1, op2, op3):
    """Opcode -9: No operation."""
    print("No operation.")

# Execution Loop
def run_program():
    """
    Main execution loop of the interpreter.
    Fetches, decodes, and executes instructions.
    """
    global ip
    while True:
        if ip >= len(instrmem):
            print("End of instruction memory reached.")
            break
        current_instruction = instrmem[ip]
        sign, oper, op1, op2, op3 = parse_instruction(current_instruction)
        trace(ip, sign, oper, op1, op2, op3)
        ip += 1  # Increment IP after fetching instruction

        # Execute instruction based on sign and opcode
        if sign == '+':
            if oper == '0':
                p0(op1, op2, op3)
            elif oper == '1':
                p1(op1, op2, op3)
            elif oper == '2':
                p2(op1, op2, op3)
            elif oper == '3':
                p3(op1, op2, op3)
            elif oper == '4':
                p4(op1, op2, op3)
                continue  # Jumped, so continue without incrementing IP
            elif oper == '5':
                p5(op1, op2, op3)
                continue  # Jumped, so continue without incrementing IP
            elif oper == '6':
                p6(op1, op2, op3)
            elif oper == '7':
                p7(op1, op2, op3)
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
            elif oper == '3':
                n3(op1, op2, op3)
            elif oper == '4':
                n4(op1, op2, op3)
                continue  # Jumped, so continue without incrementing IP
            elif oper == '5':
                n5(op1, op2, op3)
                continue  # Jumped, so continue without incrementing IP
            elif oper == '6':
                n6(op1, op2, op3)
            elif oper == '7':
                n7(op1, op2, op3)
            elif oper == '8':
                n8(op1, op2, op3)
            elif oper == '9':
                n9(op1, op2, op3)
        else:
            print(f"Error: Invalid sign '{sign}' at IP {ip}")
            sys.exit(1)

        if STEP_FLAG:
            input("Press Enter to continue...")

# Main Function
if __name__ == '__main__':
    filename = 'A1.dat'  # Replace with your actual filename
    loader(filename)     # Load program into memory
    run_program()        # Execute the program