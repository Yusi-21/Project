# assembler.py

"""
Assembler for the Educational Virtual Machine (EVM)

This script assembles a source file containing readable EVM instructions into a binary file.
It also generates a log file containing the assembled instructions in a CSV format.

Usage:
    python assembler.py -i <input_file> -o <output_file> -l <log_file>

Example:
    python assembler.py -i source.asm -o program.bin -l assembly_log.csv
"""

import argparse
import struct
import csv
import sys

# Instruction opcodes
OPCODES = {
    'LOAD_CONST': 227,   # 0xE3
    'LOAD_MEM': 34,      # 0x22
    'STORE_MEM': 183,    # 0xB7
    'POP_CNT': 1,        # 0x01
}

class Assembler:
    def __init__(self, input_file, output_file, log_file):
        self.input_file = input_file
        self.output_file = output_file
        self.log_file = log_file
        self.instructions = []

    def assemble(self):
        """
        Reads the source file, assembles instructions, and writes the binary and log files.
        """
        try:
            with open(self.input_file, 'r') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue  # Skip empty lines and comments
                parts = line.split()
                opcode = parts[0]
                if opcode not in OPCODES:
                    raise ValueError(f"Unknown opcode: {opcode}")
                method_name = f"assemble_{opcode.lower()}"
                method = getattr(self, method_name, None)
                if method is None:
                    raise NotImplementedError(f"Assembler method not implemented for opcode: {opcode}")
                instruction = method(parts)
                self.instructions.append(instruction)
            self.write_binary()
            self.write_log()
            print("Assembly completed successfully.")
        except Exception as e:
            print(f"Error during assembly: {e}", file=sys.stderr)
            sys.exit(1)

    def assemble_load_const(self, parts):
        """
        Assembles a LOAD_CONST instruction.

        Syntax:
            LOAD_CONST value
        """
        if len(parts) != 2:
            raise ValueError("LOAD_CONST requires 1 operand.")
        A = OPCODES['LOAD_CONST']
        B = int(parts[1]) & 0x7FFFFFFF  # 31 bits
        instruction = struct.pack('<BI', A, B)
        instruction = instruction[:5]  # Truncate to 5 bytes
        return {'Opcode': A, 'Operands': {'B': B}, 'Bytes': instruction}

    def assemble_load_mem(self, parts):
        """
        Assembles a LOAD_MEM instruction.

        Syntax:
            LOAD_MEM address
        """
        if len(parts) != 2:
            raise ValueError("LOAD_MEM requires 1 operand.")
        A = OPCODES['LOAD_MEM']
        B = int(parts[1]) & 0xFFFFFF  # 24 bits
        instruction = struct.pack('<BI', A, B)
        instruction = instruction[:4]  # Truncate to 4 bytes
        return {'Opcode': A, 'Operands': {'B': B}, 'Bytes': instruction}


    def assemble_store_mem(self, parts):
        """
        Assembles a STORE_MEM instruction.

        Syntax:
            STORE_MEM address
        """
        if len(parts) != 2:
            raise ValueError("STORE_MEM requires 1 operand.")
        A = OPCODES['STORE_MEM']
        B = int(parts[1]) & 0xFFFFFF  # 24 bits
        instruction = struct.pack('<BI', A, B)
        instruction = instruction[:4]  # Truncate to 4 bytes
        return {'Opcode': A, 'Operands': {'B': B}, 'Bytes': instruction}


    def assemble_pop_cnt(self, parts):
        """
        Assembles a POP_CNT instruction.

        Syntax:
            POP_CNT offset address
        """
        if len(parts) != 3:
            raise ValueError("POP_CNT requires 2 operands.")
        A = OPCODES['POP_CNT']
        B = int(parts[1]) & 0xFF  # 8 bits
        C = int(parts[2]) & 0xFFFFFF  # 24 bits
        instruction = struct.pack('<BBI', A, B, C)
        instruction = instruction[:6]  # Truncate to 6 bytes
        return {'Opcode': A, 'Operands': {'B': B, 'C': C}, 'Bytes': instruction}



    def write_binary(self):
        """
        Writes the assembled instructions to the binary output file.
        """
        with open(self.output_file, 'wb') as f:
            for instr in self.instructions:
                f.write(instr['Bytes'])

    def write_log(self):
        """
        Writes the assembly log to a CSV file.
        """
        with open(self.log_file, 'w', newline='') as csvfile:
            fieldnames = ['Opcode', 'Operands']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for instr in self.instructions:
                opcode = instr['Opcode']
                operands = instr['Operands']
                writer.writerow({'Opcode': opcode, 'Operands': operands})


def main():
    parser = argparse.ArgumentParser(description='Assembler for the Educational Virtual Machine (EVM)')
    parser.add_argument('-i', '--input', required=True, help='Path to the input source file.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output binary file.')
    parser.add_argument('-l', '--log', required=True, help='Path to the assembly log file (CSV).')
    args = parser.parse_args()

    assembler = Assembler(args.input, args.output, args.log)
    assembler.assemble()


if __name__ == '__main__':
    main()
