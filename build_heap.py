def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, data, swaps)

def main():
    input_type = input()
    if "I" in input_type:
        nav = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_type:
        filename = input()
        if "a" not in filename:
            with open("./tests/"+filename, mode='r') as f:
                nav = int(f.readline())
                data = list(map(int, f.readline().split()))
    else:
        print("error")
        return
    
    assert len(data) == nav
    
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
