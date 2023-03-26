n = 5  # number of processes
m = 3  # number of resources

allocation = [[0, 1, 0],  # Allocation Matrix
            [2, 0, 0],
            [3, 0, 2],
            [2, 1, 1],
            [0, 0, 2]]

max_resources = [[7, 5, 3],  # MAX Matrix
                [3, 2, 2],
                [9, 0, 2],
                [2, 2, 2],
                [4, 3, 3]]

available_resources = [3, 3, 2]  # Available resources at start

finish = [0] * n
ans = [0] * n
idx = 0

# Calculate Need matrix
need = [[max_resources[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

for k in range(n):
    for i in range(n):
        if not finish[i]:
            flag = True
            for j in range(m):
                if need[i][j] > available_resources[j]:
                    flag = False  # If needed resources are more in number than the available ones, move to the next process
                    break

            if flag:
                # If available resources fulfill the need
                ans[idx] = i  # the index of process, that has been allocated the resources
                idx += 1
                for y in range(m):
                    available_resources[y] += allocation[i][y]
                finish[i] = 1

flag = True
for i in range(n):
    if not finish[i]:
        flag = False
        print("System is in deadlock!!")
        break

if flag:
    print("System is in safe state and following is the safe sequence: ", end="")
    for i in range(n - 1):
        print("P", ans[i], " -> ", end="")
    print("P", ans[n - 1])
