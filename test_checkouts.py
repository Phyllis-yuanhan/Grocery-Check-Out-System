"""CSC148 Assignment 1: Tests for checkout classes

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the checkout classes.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Jacqueline Smith
"""
from store import RegularLine, ExpressLine, SelfServeLine, Customer, Item


def test_len_() -> None:
    line1 = RegularLine(1)
    line2 = ExpressLine(1)
    line3 = SelfServeLine(1)

    c1 = Customer('lpy', [Item('cheese', 3)])
    c2 = Customer('pyh', [Item('chips', 4), Item('gum', 1)])
    c3 = Customer('lpy', [Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3)])
    line1.accept(c1)
    line2.accept(c3)
    line3.accept(c2)
    assert len(line1) == 1
    assert len(line2) == 0
    assert len(line3) == 1


def test_can_accept() -> None:
    line1 = RegularLine(1)
    line2 = ExpressLine(1)
    line3 = SelfServeLine(1)

    c1 = Customer('lpy', [Item('cheese', 3)])
    c2 = Customer('pyh', [Item('chips', 4), Item('gum', 1)])
    c3 = Customer('lpy', [Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3)])
    line1.accept(c1)
    line3.accept(c1)
    assert line1.can_accept(c2) is False
    assert line2.can_accept(c3) is False
    assert line3.can_accept(c2) is False


def test_accept() -> None:
    line1 = RegularLine(1)
    line2 = ExpressLine(1)
    line3 = SelfServeLine(1)

    c1 = Customer('lpy', [Item('cheese', 3)])
    c2 = Customer('pyh', [Item('chips', 4), Item('gum', 1)])
    c3 = Customer('lpy', [Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3)])
    line1.accept(c1)
    line2.accept(c1)
    line3.accept(c1)
    assert line1.accept(c2) is False
    assert line2.accept(c3) is False
    assert line3.accept(c2) is False
    assert line1.queue[-1] == c1
    assert line2.queue[-1] == c1
    assert line3.queue[-1] == c1


def test_start_checkout() -> None:
    line1 = RegularLine(1)
    line2 = ExpressLine(1)
    line3 = SelfServeLine(1)

    c1 = Customer('lpy', [Item('cheese', 3)])
    c2 = Customer('pyh', [Item('chips', 4), Item('gum', 1)])
    c3 = Customer('lpy', [Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3)])
    line1.accept(c1)
    line2.accept(c3)
    line3.accept(c2)
    assert line1.start_checkout() == 3
    assert line2.start_checkout() == 0
    assert line3.start_checkout() == 10


def test_complete_checkout() -> None:
    line1 = RegularLine(2)
    line2 = ExpressLine(2)
    line3 = SelfServeLine(2)

    c1 = Customer('lpy', [Item('cheese', 3)])
    c2 = Customer('pyh', [Item('chips', 4), Item('gum', 1)])
    c3 = Customer('lpy', [Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3)])
    line1.accept(c1)
    line1.accept(c2)
    line2.accept(c3)
    line2.accept(c1)
    line3.accept(c1)
    line3.accept(c2)
    assert line1.complete_checkout()
    assert not line2.complete_checkout()
    assert line3.complete_checkout()


def test_close() -> None:
    line1 = RegularLine(2)
    line2 = ExpressLine(2)
    line3 = SelfServeLine(2)

    c1 = Customer('lpy', [Item('cheese', 3)])
    c2 = Customer('pyh', [Item('chips', 4), Item('gum', 1)])
    c3 = Customer('lpy', [Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3),
                          Item('cheese', 3), Item('cheese', 3)])
    line1.accept(c1)
    line1.accept(c2)
    line2.accept(c3)
    line2.accept(c1)
    line3.accept(c1)
    line3.accept(c2)

    assert line1.close() == [c2]
    assert line2.close() == []
    assert line3.close() == [c2]


if __name__ == '__main__':
    import pytest
    pytest.main(['test_checkouts.py'])
