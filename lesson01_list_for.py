words = ['낭만', '사랑', '경험', '변화']
print(words)
print(words[0], words[-1])
print(len(words))

for word in words:
    print(f"{word}은/는 좋은 단어")
print('끝')

# 연습 문제 1
days = ['월요일',
        '화요일',
        '수요일',
        '목요일',
        '금요일',
        '토요일',
        '일요일']
print(f"일주일은 {len(days)}일")
for day in days:
    print(f"{day}에는 Python 공부")

# 연습 문제 2
korean_words = ['꿈',
                '우롱차',
                '취미',
                '중앙대학교',
                '호쇼마린']
for korean_word in korean_words:
    print(f"{korean_word}: {len(korean_word)}글자")
