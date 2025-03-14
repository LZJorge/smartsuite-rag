from uuid import uuid4

def generate_uuids(length):
    if type(length) is not int:
        raise TypeError("Length must be an integer")

    if length <= 0:
        raise ValueError("Length must be greater than 0")

    uuids = [str(uuid4()) for _ in range(length)]
    return uuids