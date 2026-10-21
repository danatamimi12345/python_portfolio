
# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# bool("") prints False because an empty string is false.
print(bool(""))

# bool("0") prints True because "0" is a non-empty string.
print(bool("0"))

# bool(0) prints False because zero is a false numeric value.
print(bool(0))

# bool(0.0) prints False because 0.0 is numeric zero.
print(bool(0.0))

# bool("False") prints True because "False" is a non-empty string.
print(bool("False"))
