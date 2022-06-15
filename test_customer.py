"""CSC148 Assignment 1: Tests for Customer

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the Customer class.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Jacqueline Smith
"""
from store import Customer, Item

def test_attribute() -> None:
    c1 = Customer('pyh', [])
    assert c1.arrival_time == -1


def test_num_items() -> None:
    time = 1000
    lst = []
    while time > 0:
        lst.append(Item('orange', 5))
        time -= 1
    c1 = Customer('pyh', [])
    c2 = Customer('lpy', lst)
    assert c1.num_items() == 0
    assert c2.num_items() == 1000


def test_get_item_time() -> None:
    time = 1000
    lst = []
    while time > 0:
        lst.append(Item('orange', 5))
        time -= 1
    c1 = Customer('pyh', [])
    c2 = Customer('lpy', lst)
    assert c1.get_item_time() == 0
    assert c2.get_item_time() == 5000


if __name__ == '__main__':
    import pytest
    pytest.main(['test_customer.py'])
