#!/usr/bin/python3
"""This module writes a class myint that inherits from the
int class but reverses the == to != and vice versa
"""
class MyInt(int):
    """Reverses the equality to inequality"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
