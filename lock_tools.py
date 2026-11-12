
def is_locked(failed, max_tries=3):
    """Return True if failed attempts reach or exceed the maximum tries."""
    return failed >= max_tries


def tries_left(failed, max_tries=3):
    """Return the number of remaining tries, or 0 if the account is locked."""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed


def status(failed, max_tries=3):
    """Return the account status as locked or active with remaining tries."""
    if is_locked(failed, max_tries):
        return "locked"
    return f"active ({tries_left(failed, max_tries)} tries left)"


print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))
