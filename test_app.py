from app import process_lists

def test_process_lists():
    numbers = [1, 2, 3, 4, 11, 7, 24]

    list2, list3 = process_lists(numbers)

    assert list2 == [2, 4, 6, 8, 22, 14, 48]
    assert list3 == [4, 10, 29]