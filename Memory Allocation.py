def first_fit(memory, process):
    allocation = [-1] * len(process)
    block_used = [False] * len(memory)

    for i in range(len(process)):
        for j in range(len(memory)):
            if not block_used[j] and memory[j] >= process[i]:
                allocation[i] = j
                block_used[j] = True
                break
    return allocation


def best_fit(memory, process):
    allocation = [-1] * len(process)
    block_used = [False] * len(memory)

    for i in range(len(process)):
        best_index = -1
        min_diff = float('inf')

        for j in range(len(memory)):
            if not block_used[j] and memory[j] >= process[i]:
                diff = memory[j] - process[i]
                if diff < min_diff:
                    min_diff = diff
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            block_used[best_index] = True
    return allocation


def worst_fit(memory, process):
    allocation = [-1] * len(process)
    block_used = [False] * len(memory)

    for i in range(len(process)):
        worst_index = -1
        max_diff = -1

        for j in range(len(memory)):
            if not block_used[j] and memory[j] >= process[i]:
                diff = memory[j] - process[i]
                if diff > max_diff:
                    max_diff = diff
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            block_used[worst_index] = True
    return allocation


def print_allocation(strategy_name, process, allocation):
    print(f"\n{strategy_name} Allocation:")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process)):
        block = allocation[i]
        if block != -1:
            print(f"{i + 1}\t\t{process[i]}\t\t{block + 1}")
        else:
            print(f"{i + 1}\t\t{process[i]}\t\tNot Allocated")


# ----------------- Main Program -----------------
if __name__ == "__main__":
    # Input memory blocks
    n_blocks = int(input("Enter number of memory blocks: "))
    memory = list(map(int, input("Enter sizes of memory blocks: ").split()))

    # Input processes
    n_processes = int(input("Enter number of processes: "))
    processes = list(map(int, input("Enter sizes of processes: ").split()))

    # First Fit
    ff_allocation = first_fit(memory.copy(), processes)
    print_allocation("First Fit", processes, ff_allocation)

    # Best Fit
    bf_allocation = best_fit(memory.copy(), processes)
    print_allocation("Best Fit", processes, bf_allocation)

    # Worst Fit
    wf_allocation = worst_fit(memory.copy(), processes)
    print_allocation("Worst Fit", processes, wf_allocation)
