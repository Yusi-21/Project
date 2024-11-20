# interpreter.py

"""
Interpreter for the Educational Virtual Machine (EVM)

This script interprets a binary file containing EVM instructions and executes them.
It outputs the values from a specified range of the EVM's memory to a CSV file.

Usage:
    python interpreter.py -i <binary_file> -o <result_file> -s <start_addr> -e <end_addr>

Example:
    python interpreter.py -i program.bin -o memory_dump.csv -s 0 -e 1024
"""

import argparse
import struct
import csv
import sys

class Interpreter:
    def __init__(self, binary_file, result_file, start_addr, end_addr):
        self.binary_file = binary_file
        self.result_file = result_file
        self.start_addr = start_addr
        self.end_addr = end_addr
        self.memory = {}
        self.accumulator = 0
        self.program_counter = 0
        self.instructions = []
        self.load_binary()
        self.initialize_memory()  # Не забудьте вызвать инициализацию памяти

    def load_binary(self):
        """
        Loads the binary file into instructions list.
        """
        try:
            with open(self.binary_file, 'rb') as f:
                self.bytecode = f.read()
            self.code_size = len(self.bytecode)
        except Exception as e:
            print(f"Error loading binary file: {e}", file=sys.stderr)
            sys.exit(1)

    def initialize_memory(self):
        """
        Initializes memory with predefined values for testing.
        """
        self.memory[1000] = 5   # Binary: 101 -> popcnt = 2
        self.memory[1001] = 15  # Binary: 1111 -> popcnt = 4
        self.memory[1002] = 256 # Binary: 100000000 -> popcnt = 1
        self.memory[1003] = 7   # Binary: 111 -> popcnt = 3
        print("Memory initialized:", self.memory)

    def run(self):
        """
        Executes the instructions loaded from the binary file.
        """
        try:
            while self.program_counter < self.code_size:
                print(f"PC: {self.program_counter}, Code size: {self.code_size}")
                opcode = self.bytecode[self.program_counter]
                if opcode == 227:  # LOAD_CONST
                    self.execute_load_const()
                elif opcode == 34:  # LOAD_MEM
                    self.execute_load_mem()
                elif opcode == 183:  # STORE_MEM
                    self.execute_store_mem()
                elif opcode == 1:   # POP_CNT
                    self.execute_pop_cnt()
                else:
                    raise ValueError(f"Unknown opcode: {opcode}")
            self.write_memory_dump()
            print("Execution completed successfully.")
        except Exception as e:
            print(f"Error during execution: {e}", file=sys.stderr)
            sys.exit(1)

    def execute_load_const(self):
        """
        Executes a LOAD_CONST instruction.
        """
        opcode = self.bytecode[self.program_counter]
        B_bytes = self.bytecode[self.program_counter + 1:self.program_counter + 5]
        if len(B_bytes) < 4:
            raise ValueError(f"Not enough bytes to unpack at position {self.program_counter}")
        B = struct.unpack('<I', B_bytes)[0] & 0x7FFFFFFF  # Маска для 31 бита
        self.accumulator = B
        print(f"LOAD_CONST executed: accumulator set to {self.accumulator}")
        self.program_counter += 5  # Размер команды 5 байт

    def execute_load_mem(self):
        """
        Executes a LOAD_MEM instruction.
        """
        opcode = self.bytecode[self.program_counter]
        B_bytes = self.bytecode[self.program_counter + 1:self.program_counter + 4]
        if len(B_bytes) < 3:
            raise ValueError(f"Not enough bytes to unpack at position {self.program_counter}")
        B_bytes += b'\x00'  # Добавляем нулевой байт для получения 4 байт
        B = struct.unpack('<I', B_bytes)[0] & 0xFFFFFF  # Маска для 24 бит
        self.accumulator = self.memory.get(B, 0)
        print(f"LOAD_MEM executed: loaded value {self.accumulator} from address {B}")
        self.program_counter += 4  # Размер команды 4 байта

    def execute_store_mem(self):
        """
        Executes a STORE_MEM instruction.
        """
        opcode = self.bytecode[self.program_counter]
        B_bytes = self.bytecode[self.program_counter + 1:self.program_counter + 4]
        if len(B_bytes) < 3:
            raise ValueError(f"Not enough bytes to unpack at position {self.program_counter}")
        B_bytes += b'\x00'  # Добавляем нулевой байт для получения 4 байт
        B = struct.unpack('<I', B_bytes)[0] & 0xFFFFFF  # Маска для 24 бит
        self.memory[B] = self.accumulator
        print(f"STORE_MEM executed: stored value {self.accumulator} at address {B}")
        self.program_counter += 4  # Размер команды 4 байта

    def execute_pop_cnt(self):
        """
        Executes a POP_CNT instruction.
        """
        opcode = self.bytecode[self.program_counter]
        B_byte = self.bytecode[self.program_counter + 1]
        C_bytes = self.bytecode[self.program_counter + 2:self.program_counter + 5]
        if len(C_bytes) < 3:
            raise ValueError(f"Not enough bytes to unpack at position {self.program_counter}")
        C_bytes += b'\x00'  # Добавляем нулевой байт для получения 4 байт
        B = B_byte
        C = struct.unpack('<I', C_bytes)[0] & 0xFFFFFF  # Маска для 24 бит
        operand = self.memory.get(C, 0)
        result = bin(operand).count('1')
        dest_addr = self.accumulator + B
        self.memory[dest_addr] = result
        print(f"POP_CNT executed: operand at {C} is {operand}, popcnt={result}, stored at {dest_addr}")
        self.program_counter += 6  # Размер команды 6 байт

    def write_memory_dump(self):
        """
        Writes the memory contents within the specified range to the result CSV file.
        """
        with open(self.result_file, 'w', newline='') as csvfile:
            fieldnames = ['Address', 'Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for addr in range(self.start_addr, self.end_addr + 1):
                value = self.memory.get(addr, 0)
                writer.writerow({'Address': addr, 'Value': value})


def main():
    parser = argparse.ArgumentParser(description='Interpreter for the Educational Virtual Machine (EVM)')
    parser.add_argument('-i', '--input', required=True, help='Path to the input binary file.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output result file (CSV).')
    parser.add_argument('-s', '--start', type=int, required=True, help='Start address of memory range.')
    parser.add_argument('-e', '--end', type=int, required=True, help='End address of memory range.')
    args = parser.parse_args()

    interpreter = Interpreter(args.input, args.output, args.start, args.end)
    interpreter.run()


if __name__ == '__main__':
    main()
