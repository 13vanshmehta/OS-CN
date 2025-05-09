def optimal_page_replacement():
    frame = int(input("Enter the length of page frames: "))
    n = int(input("Enter the total numbers in the sequence: "))

    seq = []
    print("Enter the sequence of numbers:")
    for _ in range(n):
        seq.append(int(input()))

    page = [-1] * frame
    page_fault = 0
    page_hit = 0

    for i in range(n):
        hit = False

        for j in range(frame):
            if page[j] == seq[i]:
                hit = True
                page_hit += 1
                break

        if not hit:
            page_fault += 1

            # Check if there's any empty space
            empty_index = -1
            for j in range(frame):
                if page[j] == -1:
                    empty_index = j
                    break

            if empty_index != -1:
                page[empty_index] = seq[i]
            else:
                farthest_index = -1
                page_to_replace = -1

                for j in range(frame):
                    found = False
                    for k in range(i + 1, n):
                        if page[j] == seq[k]:
                            if k > farthest_index:
                                farthest_index = k
                                page_to_replace = j
                            found = True
                            break
                    if not found:
                        page_to_replace = j
                        break

                page[page_to_replace] = seq[i]

        print("\nCurrent page frames: ", end="")
        for j in range(frame):
            if page[j] != -1:
                print(page[j], end=" ")
            else:
                print("  ", end="")

    print("\nPage Fault: ", page_fault)
    print("Page Hit: ", page_hit)


# Run the function
optimal_page_replacement()