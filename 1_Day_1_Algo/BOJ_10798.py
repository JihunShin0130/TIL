#영석이의 세로 읽기

words = [input() for _ in range(5)]
max_len = max(len(word) for word in words) # 가장 긴 문자열을 기준으로 설정

for i in range(max_len):
    for word in words:
        if i < len(word): # 길이가 짧은 문자열에 대해 에러 방지
            print(word[i], end="")
            
            
"""
Zipg함수를 활용해서 풀어도 될 것 같기는 한데..
list(zip(a)) = [([1, 2, 3, 4],), (['a', 'b', 'c', 'd'],), ([5, 6, 7, 8],) 
list(zip(*a)) = [(1, 'a', 5), (2, 'b', 6), (3, 'c', 7),(4, 'd', 8)]    

이걸 활용해도 풀 수 있을 것 같다.
"""