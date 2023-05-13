# Implementation of Priority Scheduling Algorithm

def find_waiting_time(processes, n, wt):
    wt[0] = 0

    for i in range(1, n):
        wt[i] = processes[i - 1][i] + wt[i - 1]

def find_turnaround_time(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]

def find_avg_time(processes, n):
    wt = [0] * n
    tat = [0] * n

    find_waiting_time(processes, n, wt)
    find_turnaround_time(processes, n, wt, tat)

    print("\n\nProcesses    BurstTime      WaitingTime      TurnaroundTime")

    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]

        print(" ", processes[i][0], "\t\t", processes[i][1], "\t\t", wt[i], "\t\t", tat[i])
    
    print(f"\nAverage Waiting Time = {(total_wt / n)}")
    print(f"Average Turnaround Time = {(total_tat / n)}")

def priority_scheduling(proc, n):
    proc.sort(key = lambda proc:proc[2], reverse = True)
    
    print("Order of Processes being executed: ")

    for i in proc:
        print(i[0], end = " ")
    
    find_avg_time(proc, n)

if __name__ == "__main__":
    processes = [[1, 10, 1], [2, 5, 0], [3, 8, 1]]
    n = len(processes)

    priority_scheduling(processes, n)