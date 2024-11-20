# test_interpreter.py

import pytest
import struct
import os
from assembler import Assembler
from interpreter import Interpreter
import csv

def test_interpreter_load_const(tmp_path):
    # Создаем исходный код и ассемблируем
    source_code = "LOAD_CONST 12345"
    source_file = tmp_path / "test_load_const.asm"
    source_file.write_text(source_code)

    binary_file = tmp_path / "test_load_const.bin"
    log_file = tmp_path / "test_load_const_log.csv"

    assembler = Assembler(str(source_file), str(binary_file), str(log_file))
    assembler.assemble()

    # Создаем интерпретатор и выполняем программу
    result_file = tmp_path / "test_load_const_result.csv"
    interpreter = Interpreter(str(binary_file), str(result_file), 0, 0)
    interpreter.run()

    # Проверяем, что аккумулятор содержит правильное значение
    assert interpreter.accumulator == 12345

def test_interpreter_load_mem(tmp_path):
    # Создаем исходный код и ассемблируем
    source_code = "LOAD_MEM 500"
    source_file = tmp_path / "test_load_mem.asm"
    source_file.write_text(source_code)

    binary_file = tmp_path / "test_load_mem.bin"
    log_file = tmp_path / "test_load_mem_log.csv"

    assembler = Assembler(str(source_file), str(binary_file), str(log_file))
    assembler.assemble()

    # Инициализируем память
    result_file = tmp_path / "test_load_mem_result.csv"
    interpreter = Interpreter(str(binary_file), str(result_file), 0, 0)
    interpreter.memory[500] = 6789
    interpreter.run()

    # Проверяем, что аккумулятор содержит значение из памяти
    assert interpreter.accumulator == 6789

def test_interpreter_store_mem(tmp_path):
    # Создаем исходный код и ассемблируем
    source_code = "STORE_MEM 600"
    source_file = tmp_path / "test_store_mem.asm"
    source_file.write_text(source_code)

    binary_file = tmp_path / "test_store_mem.bin"
    log_file = tmp_path / "test_store_mem_log.csv"

    assembler = Assembler(str(source_file), str(binary_file), str(log_file))
    assembler.assemble()

    # Устанавливаем аккумулятор
    result_file = tmp_path / "test_store_mem_result.csv"
    interpreter = Interpreter(str(binary_file), str(result_file), 600, 600)
    interpreter.accumulator = 9876
    interpreter.run()

    # Проверяем, что значение записано в память
    assert interpreter.memory[600] == 9876

def test_interpreter_pop_cnt(tmp_path):
    # Создаем исходный код и ассемблируем
    source_code = "LOAD_CONST 1000\nPOP_CNT 0 1000"
    source_file = tmp_path / "test_pop_cnt.asm"
    source_file.write_text(source_code)

    binary_file = tmp_path / "test_pop_cnt.bin"
    log_file = tmp_path / "test_pop_cnt_log.csv"

    assembler = Assembler(str(source_file), str(binary_file), str(log_file))
    assembler.assemble()

    # Инициализируем память
    result_file = tmp_path / "test_pop_cnt_result.csv"
    interpreter = Interpreter(str(binary_file), str(result_file), 1000, 1000)
    interpreter.memory[1000] = 15  # Binary 1111, popcnt = 4
    interpreter.run()

    # Проверяем, что результат записан в память по адресу 1000
    assert interpreter.memory[1000] == 4

def test_interpreter_full_program(tmp_path):
    # Создаем исходный код и ассемблируем
    source_code = """LOAD_CONST 1000
POP_CNT 0 1000
POP_CNT 1 1001
POP_CNT 2 1002
POP_CNT 3 1003
"""
    source_file = tmp_path / "test_program.asm"
    source_file.write_text(source_code)

    binary_file = tmp_path / "test_program.bin"
    log_file = tmp_path / "test_program_log.csv"

    assembler = Assembler(str(source_file), str(binary_file), str(log_file))
    assembler.assemble()

    # Инициализируем память
    result_file = tmp_path / "test_program_result.csv"
    interpreter = Interpreter(str(binary_file), str(result_file), 1000, 1003)
    interpreter.memory[1000] = 5    # popcnt = 2
    interpreter.memory[1001] = 15   # popcnt = 4
    interpreter.memory[1002] = 256  # popcnt = 1
    interpreter.memory[1003] = 7    # popcnt = 3
    interpreter.run()

    # Проверяем результаты
    assert interpreter.memory[1000] == 2
    assert interpreter.memory[1001] == 4
    assert interpreter.memory[1002] == 1
    assert interpreter.memory[1003] == 3

