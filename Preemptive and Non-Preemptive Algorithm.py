class Process:
    def __init__(self, pid, priority, arrival_time, burst_time):
        self.pid = pid
        self.priority = priority
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1
        self.completed = False


def print_results(processes, title):
    print(f"\n{title}")
    print(f"{'Process':<10}{'Priority':<10}{'Arrival Time':<15}{'Burst Time':<15}"
          f"{'Completion Time':<17}{'Waiting Time':<15}{'Turnaround Time':<17}{'Response Time'}")

    total_wt = total_tat = 0
    processes.sort(key=lambda p: p.pid)

    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
        print(f"{p.pid:<10}{p.priority:<10}{p.arrival_time:<15}{p.burst_time:<15}"
              f"{p.completion_time:<17}{p.waiting_time:<15}{p.turnaround_time:<17}{p.response_time}")

    print(f"Average Waiting Time: {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_tat / len(processes):.2f}")


def non_preemptive(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n

    while completed != n:
        idx = -1
        min_burst = float('inf')

        for i in range(n):
            p = processes[i]
            if p.arrival_time <= current_time and not is_completed[i]:
                if p.burst_time < min_burst:
                    min_burst = p.burst_time
                    idx = i
                elif p.burst_time == min_burst:
                    if p.priority < processes[idx].priority:
                        idx = i

        if idx != -1:
            p = processes[idx]
            p.waiting_time = current_time - p.arrival_time
            current_time += p.burst_time
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.response_time = p.waiting_time
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1

    print_results(processes, "Non-Preemptive SJF (Shortest Job First) Scheduling")


def preemptive(processes):
    n = len(processes)
    current_time = 0
    completed = 0
    remaining_time = [p.burst_time for p in processes]
    response_time = [-1] * n
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    while completed != n:
        idx = -1
        min_remaining = float('inf')

        for i in range(n):
            if (processes[i].arrival_time <= current_time and
                    remaining_time[i] < min_remaining and remaining_time[i] > 0):
                min_remaining = remaining_time[i]
                idx = i

        if idx == -1:
            current_time += 1
            continue

        if response_time[idx] == -1:
            response_time[idx] = current_time - processes[idx].arrival_time

        remaining_time[idx] -= 1
        current_time += 1

        if remaining_time[idx] == 0:
            completed += 1
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - processes[idx].arrival_time
            waiting_time[idx] = turnaround_time[idx] - processes[idx].burst_time
            if waiting_time[idx] < 0:
                waiting_time[idx] = 0

    for i in range(n):
        p = processes[i]
        p.completion_time = completion_time[i]
        p.turnaround_time = turnaround_time[i]
        p.waiting_time = waiting_time[i]
        p.response_time = response_time[i]

    print_results(processes, "Preemptive SRTF (Shortest Remaining Time First) Scheduling")


# ==== Main ====
def main():
    print("Enter number of processes: ", end="")
    n = int(input())

    processes = []
    for i in range(n):
        print(f"Process {i + 1}")
        at = int(input("Enter arrival time: "))
        bt = int(input("Enter burst time: "))
        pr = int(input("Enter priority (integer): "))
        processes.append(Process(i + 1, pr, at, bt))

    print("Choose the scheduling algorithm:")
    print("1. Non-Preemptive")
    print("2. Preemptive")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        non_preemptive(processes)
    elif choice == 2:
        preemptive(processes)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()