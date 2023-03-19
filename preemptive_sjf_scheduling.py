# Implementation of Shortest Job First (Preemptive) Algorithm

def findWaitingTime(processes, n, wt):
	bt = [0] * n
	for i in range(n):
		bt[i] = processes[i][1]
	complete = 0
	MIN = 999999999
	t = 0
	short = 0
	check = False

	while (complete != n):
		# Find process with minimum remaining time among the processes that arrives till the current time`
		for j in range(n):
			if ((processes[j][2] <= t) and (bt[j] < MIN) and bt[j] > 0):
				MIN = bt[j]
				short = j
				check = True

		if (check == False):
			t += 1
			continue
			
		# Reduce remaining time by one
		bt[short] -= 1

		# Update minimum
		MIN = bt[short]
		if (MIN == 0):
			MIN = 999999999

		# If a process gets completely executed
		if (bt[short] == 0):
			complete += 1
			check = False
			fint = t + 1

			wt[short] = (fint - proc[short][1] - proc[short][2])

			if (wt[short] < 0):
				wt[short] = 0

		t += 1

def findTurnAroundTime(processes, n, wt, tat):
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]

def findavgTime(processes, n):
	wt = [0] * n
	tat = [0] * n

	findWaitingTime(processes, n, wt)
	findTurnAroundTime(processes, n, wt, tat)

	print("Processes     BurstTime	    WaitingTime	    Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",
				processes[i][1], "\t\t",
				wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = ", total_tat / n)

if __name__ =="__main__":
	proc = [[1, 6, 1], [2, 8, 1], [3, 7, 2], [4, 3, 3]]
	n = 4
	findavgTime(proc, n)