# Implementation of first come first serve algorithm

def find_waiting_time(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def find_turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_average_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    find_waiting_time(processes, n, bt, wt)
    find_turnaround_time(processes, n, bt, wt, tat)

    print("Process  BurstTime  WaitingTime  TurnaroundTime")

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" + str(bt[i]) + "\t " + str(wt[i]) + "\t\t" + str(tat[i]))

    print("Average Waiting Time: ", total_wt/n)
    print("Average Turnaround Time: ", total_tat/n)

if __name__ == "__main__":
    
    burst_time = []
    n = int(input("Enter number of processes: "))
    processes = [i for i in range(1, n + 1)]

    for i in range(n):
        burst_time.append(int(input(f"P{i + 1}: ")))

    find_average_time(processes, len(processes), burst_time)