# Implementation of non-preemptive Shortest Job First algorithm

def sjf(processes):
    n = len(processes)
    total, avg_wt, avg_tat = 0, 0, 0

    processes.sort(key= lambda i:i[1]) # sorting the processes according to burst time

    processes[0][2] = 0 # calculation of waiting time

    for i in range(1, n):
        processes[i][2] = 0
        for j in range(i):
            processes[i][2] += processes[j][1]
        total += processes[i][2]

    avg_wt = total / n
    total = 0

    print("P" + "\t" + "BT" + "\t" + "WT" + "\t" + "TAT")
    for i in range(n): # calculation of turnaround time
        processes[i][3] = processes[i][1] + processes[i][2]
        total += processes[i][3]
        print(f"P{processes[i][0]}	 {processes[i][1]}	 {processes[i][2]}	 {processes[i][3]}")

    avg_tat = total / n

    print(f"Average Waiting Time= {avg_wt}")
    print(f"Average Turnaround Time= {avg_tat}")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = [[0 for i in range(4)] for j in range(n)]

    print("Enter Burst Time:")
    for i in range(n):  # User Input Burst Time and alloting Process Id.
        processes[i][1] = int(input(f"P{i+1}: "))
        processes[i][0] = i + 1

    sjf(processes)