class Stack:
    last_reference = None

    def __init__(self, object, reference):
        self.data = object
        self.next_data = reference
        if Stack.last_reference is not None:
            Stack.last_reference = self

