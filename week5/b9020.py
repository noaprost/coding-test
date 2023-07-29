# 소수 구하는 함수
def isPrime(n):
    i = 2
    while i <= (n / 2):
        if n % i == 0:
            return False
        i = i + 1
    return True


n = input()  # 입력 받을 개수
num = [int(input()) for i in range(int(n))]  # 입력 받은 수의 배열

for n in num:
    # 차이를 가장 작게 하기위해 n의 절반부터 탐색
    p = int(n / 2)

    # 1씩 빼가면서 합이 되는 두 수가 모두 소수이면 출력하고 종료
    while p > 0:
        if isPrime(p) and isPrime(n - p):
            print(p, n - p)
            break
        p = p - 1
