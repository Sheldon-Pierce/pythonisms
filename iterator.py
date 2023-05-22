class CustomCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        yield from self.data


my_collection = CustomCollection([1, 2, 3, 4, 5])


for item in my_collection:
    print(item)


squared_numbers = [x ** 2 for x in my_collection]


list_collection = list(my_collection)
