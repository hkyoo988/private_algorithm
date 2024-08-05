from itertools import combinations

# 입력 받기
N, K = map(int, input().split())

texts = []
for _ in range(N):
    # 문자열에서 'anta', 'tica'를 제거한 후 중복 제거
    text = set(input().strip()[4:-4])
    texts.append(text)

# 기본적으로 배우고 있어야 하는 알파벳 (a, c, i, n, t)
base_learned = {0, 2, 8, 13, 19}
unlearned = [i for i in range(26) if i not in base_learned]

# K가 5보다 작으면 a, c, i, n, t를 배우지 못하므로 읽을 수 있는 단어가 없음
if K < 5:
    print(0)
else:
    max_readable = 0
    # 조합 생성 및 최대 읽을 수 있는 단어 수 계산
    for combo in combinations(unlearned, K - 5):
        learned = set(combo) | base_learned
        readable_count = 0
        for text in texts:
            if all((ord(char) - ord('a')) in learned for char in text):
                readable_count += 1
        max_readable = max(max_readable, readable_count)
    
    print(max_readable)
