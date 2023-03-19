# Implementation of Round Robin scheduling algorithm

def find_waiting_time(processes, n, bt, wt, quantum):
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 # Current time

    while(True):
        done = True
        # Traverse all processes one by one repeatedly
        for i in range(n):
            if (rem_bt[i] > 0) :
                done = False
                if (rem_bt[i] > quantum) :
                    t += quantum
                    rem_bt[i] -= quantum

                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0

        # If all processes are done
        if (done == True):
            break

def find_turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    find_waiting_time(processes, n, bt, wt, quantum)
    find_turnaround_time(processes, n, bt, wt, tat)

    # Display processes along with all details
    print("Processes    Burst Time     Waiting Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])

    print("\nAverage waiting time = ", total_wt /n)
    print("Average turn around time =", total_tat / n)

if __name__ =="__main__":
    proc = [1, 2, 3]
    n = len(proc)
    burst_time = [10, 5, 8]
    quantum = 2

    find_avg_time(proc, n, burst_time, quantum)