# config_transformer.py

"""
Configuration Transformer Tool

This script is a command-line tool that reads JSON input from standard input and transforms it into an educational configuration language, writing the output to a specified file. It detects syntax errors in the input JSON and outputs error messages accordingly.

It supports the following constructs:
- Single-line comments
- Arrays
- Dictionaries
- Constants and constant expressions, including operations and functions:
  - Addition
  - abs()
  - mod()

Usage:
    python C:\Users\user\PycharmProjects\pythonProject\hw_3\config_transformer.py -o output.conf < C:\Users\user\PycharmProjects\pythonProject\hw_3\examples\math_constants.json
    
Example:
    cat input.json | python config_transformer.py -o output.conf
"""

import argparse
import json
import sys
import re

class SyntaxError(Exception):
    """Custom exception for syntax errors."""
    pass

class Transformer:
    """Class responsible for transforming JSON input into the configuration language."""
    def __init__(self):
        self.constants = {}  # Symbol table for constants
        self.indent_level = 0  # Current indentation level

    def parse_json_input(self):
        """
        Reads JSON data from standard input and parses it.

        Returns:
            dict/list: Parsed JSON data.

        Raises:
            SyntaxError: If the input is not valid JSON.
        """
        try:
            data = json.load(sys.stdin)
            return data
        except json.JSONDecodeError as e:
            raise SyntaxError(f"Syntax Error: {e}")

    def is_valid_name(self, name):
        """
        Checks if the given name is valid according to the language specification.

        Args:
            name (str): The name to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return re.match(r'^[a-zA-Z]+$', name) is not None

    def transform(self, data):
        """
        Transforms the parsed JSON data into the configuration language.

        Args:
            data: The parsed JSON data.

        Returns:
            str: The transformed configuration.
        """
        return self.transform_value(data)

    def transform_value(self, value):
        """
        Transforms a JSON value into the equivalent configuration language value.

        Args:
            value: The JSON value to transform.

        Returns:
            str: The transformed value.

        Raises:
            SyntaxError: If an invalid value is encountered.
        """
        if isinstance(value, dict):
            # Check for constant declaration
            if 'var' in value:
                return self.transform_constant(value['var'])
            # Check for constant expression
            elif 'expr' in value:
                return self.transform_expression(value['expr'])
            else:
                return self.transform_dictionary(value)
        elif isinstance(value, list):
            return self.transform_array(value)
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            # For strings that are valid names, return as is
            if self.is_valid_name(value):
                return value
            else:
                # Wrap strings that are not valid names in quotes
                return f'"{value}"'
        elif isinstance(value, bool):
            return 'True' if value else 'False'
        elif value is None:
            return 'None'
        else:
            raise SyntaxError(f"Unsupported value type: {type(value)}")

    def transform_array(self, array):
        """
        Transforms a JSON array into the equivalent configuration language array.

        Args:
            array (list): The JSON array to transform.

        Returns:
            str: The transformed array.
        """
        transformed_items = [self.transform_value(item) for item in array]
        return "'( " + ' '.join(transformed_items) + " )"

    def transform_dictionary(self, dictionary):
        """
        Transforms a JSON object into the equivalent configuration language dictionary.

        Args:
            dictionary (dict): The JSON object to transform.

        Returns:
            str: The transformed dictionary.
        """
        items = []
        self.indent_level += 1
        indent = '    ' * self.indent_level
        for key, value in dictionary.items():
            if not self.is_valid_name(key):
                raise SyntaxError(f"Invalid key '{key}' in dictionary. Keys must match [a-zA-Z]+.")
            transformed_value = self.transform_value(value)
            items.append(f"{indent}{key} => {transformed_value}")
        self.indent_level -= 1
        opening_brace = '{\n'
        closing_brace = '\n' + ('    ' * self.indent_level) + '}'
        return opening_brace + ',\n'.join(items) + closing_brace

    def transform_constant(self, const_dict):
        """
        Transforms a constant declaration.

        Args:
            const_dict (dict): Dictionary containing constant declarations.

        Returns:
            str: The transformed constant declaration.
        """
        lines = []
        for name, value in const_dict.items():
            if not self.is_valid_name(name):
                raise SyntaxError(f"Invalid constant name '{name}'. Names must match [a-zA-Z]+.")
            transformed_value = self.transform_value(value)
            self.constants[name] = value
            lines.append(f"var {name} := {transformed_value};")
        return '\n'.join(lines)

    def transform_expression(self, expr):
        """
        Transforms and evaluates a constant expression.

        Args:
            expr (str): The expression string.

        Returns:
            str: The evaluated result as a value.

        Raises:
            SyntaxError: If the expression is invalid.
        """
        try:
            result = self.evaluate_expression(expr)
            return str(result)
        except Exception as e:
            raise SyntaxError(f"Invalid expression '{expr}': {e}")

    def evaluate_expression(self, expr):
        """
        Evaluates a constant expression.

        Args:
            expr (str): The expression string.

        Returns:
            The result of the expression.

        Raises:
            Exception: If the expression cannot be evaluated.
        """
        # Define allowed names (constants and functions)
        allowed_names = self.constants.copy()
        allowed_names.update({
            'abs': abs,
            'mod': self.mod_function
        })

        # Only allow safe characters
        if not re.match(r'^[a-zA-Z0-9_,+\-*/()\s]+$', expr):
            raise Exception("Expression contains invalid characters.")

        # Evaluate the expression
        return eval(expr, {"__builtins__": {}}, allowed_names)

    def mod_function(self, a, b):
        """
        Custom mod function for expressions.

        Args:
            a (int): Dividend.
            b (int): Divisor.

        Returns:
            int: The remainder after division.
        """
        return a % b

    def transform_comment(self, comment):
        """
        Transforms a comment.

        Args:
            comment (str): The comment text.

        Returns:
            str: The transformed comment.
        """
        return f'" {comment}'

    def transform_data(self, data):
        """
        Entry point for transforming data.

        Args:
            data: The parsed JSON data.

        Returns:
            str: The transformed configuration.
        """
        output_lines = []
        if isinstance(data, list):
            for item in data:
                output_lines.append(self.transform_value(item))
        else:
            output_lines.append(self.transform_value(data))
        return '\n'.join(output_lines)

    def main(self, output_path):
        try:
            data = self.parse_json_input()
            transformed_data = self.transform_data(data)
            with open(output_path, 'w') as f:
                f.write(transformed_data)
            print("Transformation successful. Output written to:", output_path)
        except SyntaxError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Transform JSON input into an educational configuration language.')
    parser.add_argument('-o', '--output', help='Path to the output file.', required=True)
    args = parser.parse_args()

    transformer = Transformer()
    transformer.main(args.output)


if __name__ == '__main__':
    main()
