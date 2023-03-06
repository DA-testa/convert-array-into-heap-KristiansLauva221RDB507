def sift_down(data, i, swaps):
    """
    Performs sift-down operation on the element at index i in the array.
    Modifies the array in place and records the swaps made in the swaps list.
    """
    min_index = i
    left_child = 2 * i + 1
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)


def build_heap(data):
    """
    Builds a min-heap from the given array using the sift-down method.
    Returns a list of swaps made during the heap construction.
    """
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
