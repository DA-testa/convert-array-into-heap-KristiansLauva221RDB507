import sys


def build_heap(data):
   
    swaps = []
    for i in range(len(data) -1, -1, -1):
        while i!= 0:
            if data[i]<data[int((i-1)/2)]:
                data[i],data[int((i-1)/2)] = data[int((i-1)/2)],data[i]
                swaps.append((i,int((i-1)/2)))
            i = int((i-1)/2)
    return swaps
def main():
    input_type = input()
    if "F" in input_type:
        filename = input()
        if "a" not in filename:
           with open("./tests/"+filename, mode="r") as f:
                nav = int(f.readline())
                data = list(map(int, f.readline().split()))
        else:
            print("error")
    elif "I" in input_type:
        nav = int(input())
        data = list(map(int, input().split()))
    # checks if length of data is the same as the said length
    assert len(data) == nav

    
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
