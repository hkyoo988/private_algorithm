from itertools import combinations

def wordTobit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))

    return bit

# 입력 받기
N, K = map(int, input().split())

words = [input().rstrip() for _ in range(N)]
bits = list(map(wordTobit, words))
base_bit = wordTobit('antic')

# K가 5보다 작으면 a, c, i, n, t를 배우지 못하므로 읽을 수 있는 단어가 없음
if K < 5:
    print(0)
else:

    unlearned = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    max_readable = 0
    # 조합 생성 및 최대 읽을 수 있는 단어 수 계산
    for combo in combinations(unlearned, K - 5):
        know_bit = sum(combo) | base_bit
        readable_count = 0
        for bit in bits:
            if bit & know_bit == bit:
                readable_count += 1
        max_readable = max(max_readable, readable_count)    
    print(max_readable)
