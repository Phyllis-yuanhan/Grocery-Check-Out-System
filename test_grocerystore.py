"""CSC148 Assignment 1: Tests for GroceryStore

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the GroceryStore class.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Jacqueline Smith
"""
from io import StringIO
from store import GroceryStore, Item, Customer, CheckoutLine,\
    RegularLine, ExpressLine, SelfServeLine

# Note - your tests should use StringIO to simulate opening a configuration file
# rather than requiring separate files.
# See the Assignment 0 sample test for an example of using StringIO in testing.
CONFIG_FILE = '''{
  "regular_count": 1,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''


def test_attributes() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    assert store.regular_count == 1
    assert store.express_count == 0
    assert store.self_serve_count == 0
    assert store.line_capacity == 1


def test_enter_line() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
    assert store.enter_line(c) == 0


def test_line_is_ready() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
    line_num = 0
    store.enter_line(c)
    assert store.line_is_ready(line_num)


def test_start_checkout() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
    line_num = 0
    store.enter_line(c)
    assert store.start_checkout(line_num) == 10


def test_complete_checkout() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
    line_num = 0
    store.enter_line(c)
    assert store.complete_checkout(line_num) == 0


def test_close_line() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    line_num = 0
    assert store.close_line(line_num) == []
    assert not store.list_lines[0].is_open


def test_get_first_in_line() -> None:
    store = GroceryStore(StringIO(CONFIG_FILE))
    c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
    store.enter_line(c)
    line_num = 0
    assert store.get_first_in_line(line_num) == c


if __name__ == '__main__':
    import pytest
    pytest.main(['test_grocerystore.py'])
