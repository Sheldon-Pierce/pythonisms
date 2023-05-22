class CustomDataStructure:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __bool__(self):
        return len(self.data) > 0


data_structure_1 = CustomDataStructure([1, 2, 3])
data_structure_2 = CustomDataStructure([1, 2, 3])


if data_structure_1 == data_structure_2:
    print("Data structures are equal")


if data_structure_1:
    print("Data structure is not empty")
