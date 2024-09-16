import sys

def load_program(filename):
    memory = {}
    with open(filename, 'r') as file:
        address = 0
        for line in file:
            line = line.strip()
            if not line or line.startswith('//') or line.startswith('<'):
                continue
            # Handle special end-of-program marker
            if line == '+999999999':
                break
            # Store instruction or data in memory
            memory[address] = line
            address += 1
    return memory

def parse_instruction(instruction):
    sign = instruction[0]
    opcode = int(instruction[1])
    operand1 = int(instruction[2:5])
    operand2 = int(instruction[5:8])
    operand3 = int(instruction[8:11])
    return sign, opcode, operand1, operand2, operand3

def run_program(memory):
    pc = 0  # Program counter
    registers = [0] * 1000  # Memory/registers
    stack = []
    input_buffer = []
    halted = False

    # Preload input data into the input buffer
    input_start = max(memory.keys()) + 1
    input_address = input_start
    while True:
        if input_address in memory:
            value = int(memory[input_address])
            input_buffer.append(value)
            input_address += 1
        else:
            break

    while not halted and pc in memory:
        instr = memory[pc]
        sign, opcode, op1, op2, op3 = parse_instruction(instr)
        # Debug output
        print(f'PC: {pc}, Instruction: {instr}, Sign: {sign}, Opcode: {opcode}, Operands: {op1}, {op2}, {op3}')

        if opcode == 0:  # Move
            if sign == '+':
                registers[op3] = registers[op1]
        elif opcode == 1:  # Add/Subtract
            if sign == '+':
                registers[op3] = registers[op1] + registers[op2]
            elif sign == '-':
                registers[op3] = registers[op1] - registers[op2]
        elif opcode == 4:  # Unconditional Jump
            if sign == '+':
                pc = op3
                continue
        elif opcode == 5:  # Conditional Jump
            if sign == '+':  # If Greater or Equal
                if registers[op1] >= registers[op2]:
                    pc = op3
                    continue
            elif sign == '-':  # If Less Than
                if registers[op1] < registers[op2]:
                    pc = op3
                    continue
        elif opcode == 6:  # Array Operations
            if sign == '+':  # Load from array into address
                base = op1
                index = registers[op2]
                destination = op3
                address = base + index
                if address < len(registers):
                    registers[destination] = registers[address]
                else:
                    print(f'Error: Invalid memory access at address {address}')
                    sys.exit(1)
            elif sign == '-':  # Store to array from address
                source = op1
                base = op2
                index = registers[op3]
                address = base + index
                if address < len(registers):
                    registers[address] = registers[source]
                else:
                    print(f'Error: Invalid memory access at address {address}')
                    sys.exit(1)
        elif opcode == 8:  # Input/Output
            if sign == '+':  # Read
                if input_buffer:
                    registers[op3] = input_buffer.pop(0)
                else:
                    value = int(input(f'Input for address {op3}: '))
                    registers[op3] = value
            elif sign == '-':  # Print
                print(registers[op1])
        elif opcode == 9:  # Stop
            halted = True
            print('Program halted.')
        else:
            print(f'Error: Unknown opcode {opcode}')
            sys.exit(1)
        pc += 1

# Usage example
if __name__ == '__main__':
    filename = 'A1.dat'  # Replace with your actual filename
    memory = load_program(filename)
    run_program(memory)
