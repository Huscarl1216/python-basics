# 레슨 3: 리스트에 모으기 append()
# 레슨 2에서는 조건에 맞는 단어를 "출력"만 했다.
# 이번에는 새 리스트에 "모아서" 나중에 다시 쓸 수 있게 한다.

words = ['봄', '여름', '가을', '겨울', '무지개', '바다', '산']

# ── 1단계: 빈 리스트 [] 만들고 append() 로 넣기 ──
# 리스트.append(값) → 리스트 맨 끝에 값 하나를 추가한다
print('--- 1단계 ---')
basket = []
print(basket)
basket.append('사과')
basket.append('포도')
print(basket)

# ── 2단계: for + append() ──
# 반복하면서 하나씩 넣으면 리스트가 점점 커진다
print('--- 2단계 ---')
copied = []
for word in words:
    copied.append(word)
print(copied)

# ── 3단계: for + if + append() ──
# 레슨 2의 if 를 붙이면 "조건에 맞는 것만" 모인다
print('--- 3단계 ---')
two_letter_words = []
for word in words:
    if len(word) == 2:
        two_letter_words.append(word)
print(two_letter_words)

# ── 4단계: 모은 결과의 len() 확인 ──
print('--- 4단계 ---')
print(f"2글자 단어는 {len(two_letter_words)}개")

# ── 연습 문제 1 ──
# korean_words 에서 3글자 이상인 단어를 새 리스트에 모으고, 몇 개인지 출력하기
# 힌트: 빈 리스트 → for → if len() >= 3 → append() → 반복이 끝난 뒤 len()
korean_words = ['꿈', '우리말', '하늘', '대한민국', '무지개', '별', '도서관']
at_least3 = []
for korean_word in korean_words:
    if len(korean_word) >= 3:
        at_least3.append(korean_word)
print(len(at_least3))

# ── 연습 문제 2 ──
# korean_words 를 두 리스트로 나누기
#   2글자 이하 → short_words,  3글자 이상 → long_words
# 두 리스트와 각각의 개수를 출력하기
# 힌트: 빈 리스트를 두 개 만들고, if / else 로 어느 쪽에 append() 할지 고른다
short_words = []
long_words = []
for korean_word in korean_words:
    if len(korean_word) >= 3:
        long_words.append(korean_word)
    else:
        short_words.append(korean_word)
print(short_words, long_words, len(short_words), len(long_words), sep='\n')