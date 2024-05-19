#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class.

This module contains unit tests for the methods and attributes
of the HBNBCommand class from the console module.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import console


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up the test case environment"""
        self.cmd = console.HBNBCommand()

    def test_prompt(self):
        """Test if the prompt is correctly displayed"""
        self.assertEqual("(hbnb) ", self.cmd.prompt)

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd("quit"))
            self.assertTrue(self.cmd.do_quit(''))

    def test_eof_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd("EOF"))
            self.assertIn("", fake_out.getvalue().strip())

    def test_empty_line(self):
        """Test behavior on empty line input"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("\n")
            self.assertEqual("", fake_out.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
