# to use greedy,must should sort.
meetings=[(1,4),(3,5),(0,6),(5,7),(8,9),(5,9)]
meetings.sort(key=lambda x: x[1])
selected_meetings = []
last_end_time = 0
for meeting in meetings:
    if meeting[0] >= last_end_time:
        selected_meetings.append(meeting)
        last_end_time = meeting[1]
print("Selected meetings:")
for meeting in selected_meetings:
    print(meeting)