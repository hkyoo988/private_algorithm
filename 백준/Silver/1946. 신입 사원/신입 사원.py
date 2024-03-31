import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    arr = [
        tuple(map(int, sys.stdin.readline().split()))
        for _ in range(n)
    ]

    arr.sort(key=lambda end: (end[0], end[1]))

    prev_resume = 0
    prev_interview = 0
    cnt = 0
    for i in arr:
        resume, interview = i
        if prev_interview < interview and prev_resume < resume and prev_interview != 0 and prev_resume != 0:
            continue
        if prev_interview <= interview or prev_resume <= resume:
            prev_interview = min(prev_interview, interview) if prev_interview != 0 else interview
            prev_resume = min(prev_resume, resume) if prev_resume != 0 else resume
            cnt += 1
    print(cnt)