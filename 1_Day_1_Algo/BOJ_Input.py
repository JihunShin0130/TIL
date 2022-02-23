# 공백으로 구분된 두 정수 입력받기 - 1000번

a, b = map(int, input().split())
print(a + b)

# 개행으로 구분된 두 정수 입력받기 - 2558번 

a, b = int(input()), int(input())
print(a + b)

# 테스트 케이스 갯수에 따라 유동적으로 입력 받기 - 10950번

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b)
    
# 특정 종료 조건에서 탈출하기 - 10952번

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)
    
# 특정 형식으로 출력하기 - 11021번 (f-string 활용)

for t in range(int(input())):
    a, b = map(int, input().split())
    print(f"Case #{t + 1}: {a + b}")
    

# 특정 형식으로 출력하기2 - 11022번

for t in range(int(input())):
    a, b = map(int, input().split())
    print(f"Case #{t + 1}: {a} + {b} = {a + b}")

