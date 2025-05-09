def fifo_page_replacement(frame_len, sequence):
    page = [-1] * frame_len
    ptr = 0
    page_hit = 0
    page_fault = 0

    for num in sequence:
        if num in page:
            page_hit += 1
        else:
            page[ptr] = num
            page_fault += 1
            ptr = (ptr + 1) % frame_len

        print("\nCurrent page frames:", end=" ")
        for p in page:
            if p != -1:
                print(p, end=" ")
            else:
                print(" ", end=" ")

    print("\nPage Fault:", page_fault)
    print("Page Hit:", page_hit)


# Input section
print("Enter the length of page frames: ", end="")
frame_len = int(input())

print("Enter the total numbers in the sequence: ", end="")
n = int(input())

print("Enter the sequence of numbers:")
sequence = [int(input()) for _ in range(n)]

# Run FIFO algorithm
fifo_page_replacement(frame_len, sequence)