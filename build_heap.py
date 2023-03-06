# import sys

# def sift_down(data, i, swaps):
#     """
#     Performs sift-down operation on the element at index i in the array.
#     Modifies the array in place and records the swaps made in the swaps list.
#     """
#     min_index = i
#     left_child = 2 * i + 1
#     if left_child < len(data) and data[left_child] < data[min_index]:
#         min_index = left_child
#     right_child = 2 * i + 2
#     if right_child < len(data) and data[right_child] < data[min_index]:
#         min_index = right_child
#     if i != min_index:
#         data[i], data[min_index] = data[min_index], data[i]
#         swaps.append((i, min_index))
#         sift_down(data, min_index, swaps)


# def build_heap(data):
#     """
#     Builds a min-heap from the given array using the sift-down method.
#     Returns a list of swaps made during the heap construction.
#     """
#     swaps = []
#     for i in range(len(data) // 2, -1, -1):
#         sift_down(data, i, swaps)
#     return swaps


# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     data = map(int, sys.stdin.readline().split())
#     swaps = build_heap(list(data))
#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)
import sys

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


def build_heap(data, n):
    """
    Builds a min-heap from the given array using the sift-down method.
    Returns a list of swaps made during the heap construction.
    """
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


if __name__ == "__main__":
    input_type = input()
    if "F" in input_type:
        filename = input()
        if "a" not in filename:
            with open(str("test/"+filename), mode="r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline()))
        else:
            print("error")
    elif "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
