words = input("단어를 입력하세요 : ")

palindrome_check = True

for word in range(len(words) // 2):
    if words[word] != words[-1-word]:
        palindrome_check = False
        break

print(palindrome_check)