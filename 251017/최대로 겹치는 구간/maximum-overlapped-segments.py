n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
events = []
for start, end in segments:
    events.append((start,1))
    events.append((end,-1))

events.sort(key=lambda x:(x[0],x[1]))

current = 0
maxe = 0

for  _,event_type in events:
    current += event_type
    if current>maxe:
        maxe = current

print(maxe)
    
