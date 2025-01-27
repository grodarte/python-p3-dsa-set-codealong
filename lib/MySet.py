import ipdb

class MySet:
# __init__: Initializes a new MySet and adds any values from a list.
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

# has(value): Checks if the value is already included in the MySet. Must have a O(1) runtime.
    def has(self, value):
        return value in self.dictionary

# add(value): Adds the value to the MySet if it isn't already present. Must have a O(1) runtime.
    def add(self, value):
        self.dictionary[value] = True
        return self
# delete(value): Removes the value from the MySet. Must have a O(1) runtime.
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
# size(): Returns the number of elements in the MySet.
    def size(self):
        return len(self.dictionary)

# MySet.clear(): Removes all the items from the set, and returns the updated set.
    def clear(self):
        self.dictionary = {}
        return self
# Print the set in a readable format using the __str__ method.
    def __str__(self):
        keys = ','.join([f"{key}" for key in self.dictionary.keys()])
        return f"MySet: {{{keys}}}"
