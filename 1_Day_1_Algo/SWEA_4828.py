T = int(input())
for test_case in range(1, T + 1):
    
    a=int(input())
    b=list(map(int,input().split()))
    #print("#{} {}".format(test_case,max(b)-min(b)))
    #f-string 활용
    print(f"#{test_case} {max(b)-min(b)}") 