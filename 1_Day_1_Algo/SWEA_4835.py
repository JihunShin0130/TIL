#구간 합
"""
# 풀이 1
T = int(input())
m = 0

for tc in range(T):
    integer_info = list(map(int, (input().split())))
    received_nums = list(map(int, (input().split())))
    integer_num = integer_info[0]
    interval = integer_info[1]

    all_sums_list = [] # 구간합들을 받아줄 빈 리스트 생성.

    # 예를들면 숫자들이 5개인데 3개짜리 구간을 설정했다고 하면 (5-3)  2 + 1 번만큼 연속한 다른구간이 나온다.
    for i in range(integer_num - interval + 1):
        interval_list = received_nums[i:i+interval] # 슬라이싱 할때 이렇게.
        count = 0
        for j in interval_list:
            count += j

        all_sums_list.append(count)

    # 여기까지 하면 all_sums_list 에는 구간합들이 요소로서 들어가 있을 것이므로 이걸 버블정렬 하고
    # -1 인덱스인 최댓값 - 0인덱스인 최솟값을 빼주면 완성!

    for x in range(len(all_sums_list)-1, 0, -1):
        for y in range(x):
            if all_sums_list[y] > all_sums_list[y+1]:
                all_sums_list[y], all_sums_list[y+1] = all_sums_list[y+1], all_sums_list[y]

    answer = all_sums_list[-1] - all_sums_list[0]

    m += 1

    print('#{} {}'.format(m, answer))
"""

# 풀이 2
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N개 정수, M개 구간
    numbers = list(map(int, input().split()))  # 숫자들 리스트

    pendency = 0  # 일단 첫 구간에 대한 합을 임시로 저장해두는 변수입니다.
    for _ in range(M):  # 첫 구간의 합을 저장
        numbers[_] += pendency
    
    max_result = pendency  # 일단 최솟값과 최댓값 모두 첫번째 구간의 합으로 초기화
    min_result = pendency

    # 슬라이딩 윈도우라면 ->
    for i in range(M, N):  # 위의 range 에서 M은 오른쪽이라 미만을 나타낸 것이고 그다음부터 봐야할땐 지금은 range 왼쪽에 M이 맞습니다.
        pendency = pendency - numbers[i-M] + numbers[i]  # 이 pendency 변수는 포문이 돌면서 재할당됩니다.

        if max_result < pendency:  # 그 임시 변수가 현재 있는 최대값보다 크다면?
            max_result = pendency   # 최대값을 임시변수로 재할당
        if min_result > pendency:  # 마찬가지로 최솟값도 처리해 줍니다.
            min_result = pendency

    answer = max_result - min_result  # 차를 구하는 것이므로

    print('#{} {}'.format(tc, answer))