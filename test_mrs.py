def test_reverse_relation(bubble_sort):
    """Test MR1: Reversing the input array."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_original = bubble_sort(arr.copy())
    arr_reversed = arr[::-1]
    sorted_reversed = bubble_sort(arr_reversed)
    assert sorted_original == sorted_reversed, "Sorting should yield the same result for reversed input"

def test_constant_addition_relation(bubble_sort, constant=10):
    """Test MR2: Adding a constant to all elements."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_original = bubble_sort(arr.copy())
    arr_added = [x + constant for x in arr]
    sorted_added = bubble_sort(arr_added)
    sorted_added = [x - constant for x in sorted_added]
    assert sorted_original == sorted_added, "Sorting should maintain relative order when a constant is added to all elements"
