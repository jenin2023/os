class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.finish_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def read_processes(filename):
    processes = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split()
            if parts[0] == "CS":
                context_switch_time = int(parts[1])
            elif parts[0] == "Q":
                quantum = int(parts[1])
            else:
                pid = int(parts[0])
                arrival_time = int(parts[1])
                burst_time = int(parts[2])
                processes.append(Process(pid, arrival_time, burst_time))
    return processes, context_switch_time, quantum

def fcfs(processes, context_switch_time):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    gantt_chart = []
    
    for process in processes:
        if current_time &lt; process.arrival_time:  # تم تصحيح هنا
            current_time = process.arrival_time
        gantt_chart.append((process.pid, current_time, current_time + process.burst_time))
        current_time += process.burst_time + context_switch_time
        process.finish_time = current_time
        process.turnaround_time = process.finish_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        
    return gantt_chart

def print_results(processes, gantt_chart):
    print("Gantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: start at {entry[1]}, finish at {entry[2]}")
    
    print("\nProcess details:")
    for process in processes:
        print(f"Process {process.pid}: Finish Time = {process.finish_time}, Waiting Time = {process.waiting_time}, Turnaround Time = {process.turnaround_time}")
    
    total_burst_time = sum(p.burst_time for p in processes)
    total_time = max(p.finish_time for p in processes)
    cpu_utilization = (total_burst_time / total_time) * 100
    print(f"\nCPU Utilization: {cpu_utilization:.2f}%")

def main():
    processes, context_switch_time, quantum = read_processes('processes.txt')
    
    # FCFS
    print("FCFS Scheduling:")
    gantt_chart = fcfs(processes, context_switch_time)
    print_results(processes, gantt_chart)

if __name__ == "__main__":
    main()
  
