import pytest

from dunderMethods import CustomDataStructure
from iterator import CustomCollection


def test_custom_collection_iteration():
    my_collection = CustomCollection([1, 2, 3, 4, 5])
    result = []
    for item in my_collection:
        result.append(item)
    assert result == [1, 2, 3, 4, 5]


def test_custom_collection_list_comprehension():
    my_collection = CustomCollection([1, 2, 3, 4, 5])
    result = [x ** 2 for x in my_collection]
    assert result == [1, 4, 9, 16, 25]


def test_custom_collection_conversion():
    my_collection = CustomCollection([1, 2, 3, 4, 5])
    result = list(my_collection)
    assert result == [1, 2, 3, 4, 5]

# def test_calculate_time_decorator():
#     @calculate_time
#     def my_function():
#         time.sleep(1)
#
#     # Capture standard output to check the printed message
#     with io.StringIO() as buffer, redirect_stdout(buffer):
#         my_function()
#         output = buffer.getvalue().strip()
#
#     # Check if the output contains the expected message format
#     assert output.startswith("Function my_function took")
#     assert output.endswith("seconds.")


def test_custom_data_structure_equality():
    data_structure_1 = CustomDataStructure([1, 2, 3])
    data_structure_2 = CustomDataStructure([1, 2, 3])
    assert data_structure_1 == data_structure_2


def test_custom_data_structure_truthiness():
    empty_data_structure = CustomDataStructure([])
    non_empty_data_structure = CustomDataStructure([1, 2, 3])
    assert bool(empty_data_structure) is False
    assert bool(non_empty_data_structure) is True



