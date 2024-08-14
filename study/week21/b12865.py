# 평범한 배낭
# 하나씩 넣어가면서 가치를 업데이트

import sys

n, totalWeight = map(int, sys.stdin.readline().split())

bag = [0] * (totalWeight + 1)

for _ in range(n):  # 모든 보석을 한번씩 검사
    w, v = map(int, sys.stdin.readline().split())  # weight, value
    if w > totalWeight:
        continue

    # 전체 무게의 뒷쪽부터 하니씩 검사, 0이면 아무것도 담을 수 없기 때문에 고려x
    for j in range(totalWeight, 0, -1):
        if w + j <= totalWeight and bag[j] != 0:
            # 원래 있던거 vs 새로 합쳐서 만든 가치 중에 더 큰걸로 업데이트
            bag[w + j] = max(bag[w + j], bag[j] + v)
    # bag[j] == 0인 경우 딱 들어맞는 물건을 넣을 수 있으므로 그떄 물건의 가치와 원래 있던 가치를 비교해서 넣어줌(무게는 같고 가치는 다른 애들 고려)
    bag[w] = max(v, bag[w])

print(max(bag))
