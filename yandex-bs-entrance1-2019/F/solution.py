def highload_start(sessions):
    times = set([row[0] for row in sessions]) | set([row[1] for row in sessions])
    load = {}
    for time in times:
        load[time] = len([ses for ses in sessions if ses[0] <= time and ses[1] >= time])

    max_load = max(load.values())
    highload_times = [time for time, load in load.items() if load == max_load]
    highload_start = min(highload_times)
    return highload_start


# input
session_cnt = int(input())
sessions = []
for i in range(session_cnt):
    sessions.append([int(val) for val in input().split()])

# output
print(highload_start(sessions))
