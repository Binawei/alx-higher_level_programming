#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_b = (0, None)
    tuple_b = len(sentence), sentence[:1]
    return tuple_b
