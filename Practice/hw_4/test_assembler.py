# test_assembler.py

import pytest
import struct
import os
from assembler import Assembler
import csv

def test_assemble_load_const(tmp_path):
    # Создаем временный файл с исходным кодом
    source_code = "LOAD_CONST 868"
    source_file = tmp_path / "test_load_const.asm"
    source_file.write_text(source_code)

    # Выходной бинарный файл и лог-файл
    output_file = tmp_path / "test_load_const.bin"
    log_file = tmp_path / "test_load_const_log.csv"

    # Ассемблируем
    assembler = Assembler(str(source_file), str(output_file), str(log_file))
    assembler.assemble()

    # Проверяем бинарный файл
    with open(output_file, 'rb') as f:
        bytecode = f.read()

    # Ожидаемое значение
    expected_bytecode = struct.pack('<BI', 227, 868)[:5]

    assert bytecode == expected_bytecode

    # Проверяем лог-файл
    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    assert len(rows) == 1
    assert int(rows[0]['Opcode']) == 227
    assert eval(rows[0]['Operands']) == {'B': 868}


def test_assemble_load_mem(tmp_path):
    source_code = "LOAD_MEM 269"
    source_file = tmp_path / "test_load_mem.asm"
    source_file.write_text(source_code)

    output_file = tmp_path / "test_load_mem.bin"
    log_file = tmp_path / "test_load_mem_log.csv"

    assembler = Assembler(str(source_file), str(output_file), str(log_file))
    assembler.assemble()

    with open(output_file, 'rb') as f:
        bytecode = f.read()

    expected_bytecode = struct.pack('<BI', 34, 269)[:4]

    assert bytecode == expected_bytecode

    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    assert len(rows) == 1
    assert int(rows[0]['Opcode']) == 34
    assert eval(rows[0]['Operands']) == {'B': 269}


def test_assemble_store_mem(tmp_path):
    source_code = "STORE_MEM 644"
    source_file = tmp_path / "test_store_mem.asm"
    source_file.write_text(source_code)

    output_file = tmp_path / "test_store_mem.bin"
    log_file = tmp_path / "test_store_mem_log.csv"

    assembler = Assembler(str(source_file), str(output_file), str(log_file))
    assembler.assemble()

    with open(output_file, 'rb') as f:
        bytecode = f.read()

    expected_bytecode = struct.pack('<BI', 183, 644)[:4]

    assert bytecode == expected_bytecode

    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    assert len(rows) == 1
    assert int(rows[0]['Opcode']) == 183
    assert eval(rows[0]['Operands']) == {'B': 644}


def test_assemble_pop_cnt(tmp_path):
    source_code = "POP_CNT 141 730"
    source_file = tmp_path / "test_pop_cnt.asm"
    source_file.write_text(source_code)

    output_file = tmp_path / "test_pop_cnt.bin"
    log_file = tmp_path / "test_pop_cnt_log.csv"

    assembler = Assembler(str(source_file), str(output_file), str(log_file))
    assembler.assemble()

    with open(output_file, 'rb') as f:
        bytecode = f.read()

    # Обратите внимание, что POP_CNT имеет формат '<BBI', но мы обрезаем до 6 байт
    expected_bytecode = struct.pack('<BBI', 1, 141, 730)[:6]

    assert bytecode == expected_bytecode

    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    assert len(rows) == 1
    assert int(rows[0]['Opcode']) == 1
    assert eval(rows[0]['Operands']) == {'B': 141, 'C': 730}

