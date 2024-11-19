# test_config_transformer.py

"""
Test Suite for Configuration Transformer Tool

This module contains unit tests for the Configuration Transformer tool functions using pytest.
Each function is tested to ensure correct behavior, covering all language constructs including nesting,
constants, constant expressions, and operations.
"""

import pytest
from config_transformer import (
    Transformer,
    SyntaxError
)
import sys
import io
import json


def test_is_valid_name():
    transformer = Transformer()
    assert transformer.is_valid_name('ValidName')
    assert not transformer.is_valid_name('invalid_name')
    assert not transformer.is_valid_name('123Invalid')
    assert not transformer.is_valid_name('Invalid-Name')


def test_transform_value_number():
    transformer = Transformer()
    assert transformer.transform_value(42) == '42'
    assert transformer.transform_value(3.14) == '3.14'


def test_transform_value_string():
    transformer = Transformer()
    assert transformer.transform_value('Name') == 'Name'
    assert transformer.transform_value('invalid_name') == '"invalid_name"'
    assert transformer.transform_value('Hello World') == '"Hello World"'


def test_transform_value_boolean():
    transformer = Transformer()
    assert transformer.transform_value(True) == 'True'
    assert transformer.transform_value(False) == 'False'


def test_transform_value_none():
    transformer = Transformer()
    assert transformer.transform_value(None) == 'None'


def test_transform_dictionary():
    transformer = Transformer()
    dictionary = {
        'Name': 'Value',
        'Number': 42,
        'Array': [1, 2, 3],
        'Dict': {'InnerName': 'InnerValue'},
        'Flag': True,
        'Nothing': None
    }
    expected_output = """{
    Name => Value,
    Number => 42,
    Array => '( 1 2 3 ),
    Dict => {
        InnerName => InnerValue
    },
    Flag => True,
    Nothing => None
}"""
    assert transformer.transform_dictionary(dictionary) == expected_output


def test_transform_constant():
    transformer = Transformer()
    const_dict = {'var': {'MaxValue': 100}}
    expected_output = "var MaxValue := 100;"
    assert transformer.transform_value(const_dict) == expected_output
    assert transformer.constants == {'MaxValue': 100}


def test_transform_expression():
    transformer = Transformer()
    transformer.constants = {'MaxValue': 100}
    expr_dict = {'expr': 'MaxValue + 1'}
    expected_output = "101"
    assert transformer.transform_value(expr_dict) == expected_output


def test_evaluate_expression():
    transformer = Transformer()
    transformer.constants = {'a': 5}
    assert transformer.evaluate_expression('a + 2') == 7
    assert transformer.evaluate_expression('abs(-10)') == 10
    assert transformer.evaluate_expression('mod(10, 3)') == 1


def test_transform_comment():
    transformer = Transformer()
    comment = "This is a comment"
    expected_output = '" This is a comment'
    assert transformer.transform_comment(comment) == expected_output


def test_transform_nested_structures():
    transformer = Transformer()
    data = {
        'Config': {
            'Settings': {
                'Option': True,
                'Threshold': 0.75
            },
            'Items': [1, {'SubItem': 'Value'}, [2, 3], None]
        }
    }
    expected_output = """{
    Config => {
        Settings => {
            Option => True,
            Threshold => 0.75
        },
        Items => '( 1 {
            SubItem => Value
        } '( 2 3 ) None )
    }
}"""
    assert transformer.transform_value(data) == expected_output


def test_parse_json_input_valid(monkeypatch):
    test_json = '{"Name": "Value"}'
    monkeypatch.setattr(sys, 'stdin', io.StringIO(test_json))
    transformer = Transformer()
    data = transformer.parse_json_input()
    assert data == {"Name": "Value"}


def test_parse_json_input_invalid(monkeypatch):
    test_json = '{"Name": "Value"'
    monkeypatch.setattr(sys, 'stdin', io.StringIO(test_json))
    transformer = Transformer()
    with pytest.raises(SyntaxError):
        transformer.parse_json_input()


def test_invalid_name_in_dictionary():
    transformer = Transformer()
    dictionary = {'invalid_name': 'Value'}
    with pytest.raises(SyntaxError):
        transformer.transform_dictionary(dictionary)


def test_invalid_value_in_array():
    transformer = Transformer()
    array = [1, 'ValidName', set([1, 2, 3])]
    with pytest.raises(SyntaxError):
        transformer.transform_array(array)


def test_expression_invalid():
    transformer = Transformer()
    expr_dict = {'expr': 'invalid + 1'}
    with pytest.raises(SyntaxError):
        transformer.transform_value(expr_dict)


def test_mod_function():
    transformer = Transformer()
    assert transformer.mod_function(10, 3) == 1


def test_constant_and_expression():
    transformer = Transformer()
    data = [
        {'var': {'MaxValue': 100}},
        {'expr': 'MaxValue + 1'}
    ]
    expected_output = """var MaxValue := 100;
101"""
    assert transformer.transform_data(data) == expected_output
