def solution(t):
    midIdx = 12
    moveCount = 0
    idx = 0

    aNum = t.count("A")
    t = t.replace("A", "")

    #커서의 이동 횟수
    if(len(t) > 0):
        curCount = len(t) - 1 + (aNum // 2)
    else:
        return 0
    moveCount = moveCount + curCount

    for i in range(len(t)):

        idx = alphabet.index(t[i])

        # 알파벳 이동 횟수를 더해주는 부분
        if(idx <= 12):
            moveCount = moveCount + idx
        else:
            moveCount = moveCount + (26 - idx) 

    return moveCount

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# 0~12 앞부터 찾는게 빠름
# 13~25 뒤부터 찾는게 빠름

t = input()
print(solution(t))




