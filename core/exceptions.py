from re import S


class AddressIsDoubleAssigned(Exception):
    def __init__(self):
        self.message = "Address can't be associated with both customer and contact"


class AddressWithoutParentKey(Exception):
    def __init__(self):
        self.message = "You can't retrive address without parent key"
