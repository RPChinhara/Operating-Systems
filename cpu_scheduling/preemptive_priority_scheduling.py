class Process:
    def __init__(self, pid, priority, burst_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
    
    def __repr__(self):
        return f"Process {self.pid}: Priority={self.priority}, Burst Time={self.burst_time}"


def preemtive_priority_scheduling(processes):
    """
    Implement pre-emptive priority scheduling algorithm.
    :param processes: list of Process objects
    :return: list of Process objects in the order of their execution
    """
    # sort processes by priority
    processes.sort(key=lambda p: p.priority)

    # create a queue to hold the ready processes
    ready_queue = []

    # create a list to hold the completed processes
    completed_processes = []

    # initialize time and current process
    time = 0
    current_process = None

    while processes or ready_queue:
        # move any processes that have arrived to the ready queue
        while processes and processes[0].burst_time <= time:
            ready_queue.append(processes.pop(0))

        # if there is a higher priority process in the ready queue, pre-empt the current process
        if ready_queue and (not current_process or ready_queue[0].priority < current_process.priority):
            if current_process:
                # add the current process back to the ready queue
                ready_queue.append(current_process)
            # get the next process from the ready queue
            current_process = ready_queue.pop(0)

        if current_process:
            # execute the current process for one time unit
            current_process.burst_time -= 1
            # if the process has finished, add it to the completed list and set current process to None
            if current_process.burst_time == 0:
                completed_processes.append(current_process)
                current_process = None

        time += 1

    return completed_processes

if __name__=="__main__":
    # create some sample processes
    processes = [
        Process(1, 3, 6),
        Process(2, 1, 3),
        Process(3, 4, 4),
        Process(4, 2, 5)
    ]

    # run pre-emptive priority scheduling
    result = preemtive_priority_scheduling(processes)

    # print the order of execution
    print([p.pid for p in result])
