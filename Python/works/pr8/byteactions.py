def get_and(a:int, b:int) -> int:
    return a & b

def get_or(a:int, b:int) -> int:
    return a | b

def get_xor(a:int, b:int) -> int:
    return a ^ b

def get_not(a:int) -> int:
    return ~a

def get_left_shift(a:int, bits:int) -> int:
    return a << bits

def get_right_shift(a:int, bits:int) -> int:
    return a >> bits
