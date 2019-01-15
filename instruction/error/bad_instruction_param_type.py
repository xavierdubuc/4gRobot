class BadInstructionParamTypeError(Exception):
    """
    BadInstructionParamTypeError is fired when an instruction is called with
    a param of unsupported type. Ex: a string instead of a int.
    """
    pass
