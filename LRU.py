def lru_page_replacement():
    frame = int(input("Enter the number of page frames: "))
    n = int(input("Enter the total numbers in the sequence: "))

    seq = []
    print("Enter the sequence of numbers:")
    for _ in range(n):
        seq.append(int(input()))

    page = [-1] * frame
    last_used = [0] * frame
    page_fault = 0
    page_hit = 0

    for i in range(n):
        hit = False

        for j in range(frame):
            if page[j] == seq[i]:
                hit = True
                page_hit += 1
                last_used[j] = i
                break

        if not hit:
            page_fault += 1
            replace_index = -1
            oldest = float('inf')

            for j in range(frame):
                if page[j] == -1:
                    replace_index = j
                    break
                if last_used[j] < oldest:
                    oldest = last_used[j]
                    replace_index = j

            page[replace_index] = seq[i]
            last_used[replace_index] = i

        print("\nCurrent page frames: ", end="")
        for j in range(frame):
            if page[j] != -1:
                print(page[j], end=" ")
            else:
                print("  ", end="")

    print("\nPage Fault: ", page_fault)
    print("Page Hit: ", page_hit)


# Run the function
lru_page_replacement()