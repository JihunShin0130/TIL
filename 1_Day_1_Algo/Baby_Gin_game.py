"""
cards = [8, 3, 2, 8, 1, 8]

card_counts = [0] * 10  # 10 개짜리 틀을 만들어 주고

for num in cards:  # 뽑아져 나올 때마다 
    card_counts[num] += 1

# print(card_counts) => [0, 1, 1, 1, 0, 0, 0, 0, 3, 0]

answer = False

for card_num in card_counts:
    if card_num >= 3:
        answer = True
        break

print(answer)

"""

cards = [4, 8, 7, 3, 1, 5, 5, 6]

card_counts = [0] * 10  # 10개짜리 카운트용 리스트 만들고

for num in cards:  # 발견하면 우물정자 표시하고
    card_counts[num] += 1

is_run = False  # 일단 없다고 생각하되, 아래서 인덱스 에러 조심해주자!

for i in range(len(cards)-2): # 3개씩 동시에 검증해야하니까 index 5 까지만! 
    if card_counts[i] >= 1 and card_counts[i+1] >= 1 and card_counts[i+2] >= 1:
        #if card_counts[i] and card_counts[i+1]  and card_counts[i+2] :        
			#card_counts[i] -= 1        
			#card_counts[i+1] -= 1        
			#card_counts[i+2] -= 1
        is_run = True  # 3개 동시에 봤을때 조건을 만족하면 run 이니까?
        
print(is_run)