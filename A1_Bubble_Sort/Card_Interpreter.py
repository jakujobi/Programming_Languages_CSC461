import sys

# Memory Structures
datamem = [0] * 1000  # Data Memory
instrmem = []         # Instruction Memory
cardmem = []          # Card Reader (Input Cards)
next_card = 0         # Next card index
ip = 0                # Instruction Pointer

# Debugging Flags
INST_FLAG = True   # Set to True to enable instruction tracing
STEP_FLAG = False  # Set to True to enable step-by-step execution

# Loader Function
def loader(filename):
    global datamem, instrmem, cardmem
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    FLAG = '+9999999999'
    count = 0
    section = 'data'

    for line in lines:
        line = line.strip()
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
            datamem[count] = int(line)
            count += 1
        elif section == 'instructions':
            instrmem.append(line)
            count += 1
        elif section == 'input':
            cardmem.append(int(line))
            count += 1

# Instruction Parsing Function
def parse_instruction(instr):
    sign = instr[0]
    oper = instr[1]
    op1 = int(instr[2:5])
    op2 = int(instr[5:8])
    op3 = int(instr[8:11])
    return sign, oper, op1, op2, op3

# Trace Function
def trace(ip, sign, oper, op1, op2, op3):
    if INST_FLAG:
        print(f"IP: {ip:04}")
        print(f"Instruction: {sign}{oper}{op1:03}{op2:03}{op3:03}")
        print(f"Operands: op1={datamem[op1]}, op2={datamem[op2]}, op3={datamem[op3]}")
        print("-" * 40)
    if STEP_FLAG:
        input("Press Enter to continue...")

# Opcode Execution Functions
def p0(op1, op2, op3):
    datamem[op3] = datamem[op1]

def p1(op1, op2, op3):
    datamem[op3] = datamem[op1] + datamem[op2]

def p2(op1, op2, op3):
    datamem[op3] = datamem[op1] * datamem[op2]

def p3(op1, op2, op3):
    datamem[op3] = datamem[op1] * datamem[op1]

def p4(op1, op2, op3):
    global ip
    if datamem[op1] == datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

def p5(op1, op2, op3):
    global ip
    if datamem[op1] >= datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

def p6(op1, op2, op3):
    base = op1
    index = datamem[op2]
    datamem[op3] = datamem[base + index]

def p7(op1, op2, op3):
    global ip
    datamem[op1] += 1
    if datamem[op1] < datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

def p8(op1, op2, op3):
    global next_card
    if next_card < len(cardmem):
        datamem[op3] = cardmem[next_card]
        next_card += 1
    else:
        value = int(input(f"Input for address {op3}: "))
        datamem[op3] = value

def p9(op1, op2, op3):
    print("Program halted.")
    sys.exit(0)

def n0(op1, op2, op3):
    print("No operation.")

def n1(op1, op2, op3):
    datamem[op3] = datamem[op1] - datamem[op2]

def n2(op1, op2, op3):
    datamem[op3] = datamem[op1] // datamem[op2]

def n3(op1, op2, op3):
    print("Square root operation not implemented.")

def n4(op1, op2, op3):
    global ip
    if datamem[op1] != datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

def n5(op1, op2, op3):
    global ip
    if datamem[op1] < datamem[op2]:
        ip = op3 - 1  # Adjust for zero-based index

def n6(op1, op2, op3):
    base = op2
    index = datamem[op3]
    datamem[base + index] = datamem[op1]

def n7(op1, op2, op3):
    print("No operation.")

def n8(op1, op2, op3):
    print(datamem[op1])

def n9(op1, op2, op3):
    print("No operation.")

# Execution Loop
def run_program():
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
    loader(filename)
    run_program()
