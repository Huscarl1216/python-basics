# 레슨 2: 조건문 (if)
# 레슨 1에서는 for로 리스트의 값을 하나씩 꺼냈다.
# 이번에는 꺼낸 값 중에서 "조건에 맞는 것만" 골라 본다.

fruits = ['사과', '바나나', '포도', '딸기', '파인애플']

# ── 1단계: if / else ──
# if 조건:   → 조건이 참(True)이면 들여쓴 줄을 실행
# else:      → 조건이 거짓(False)이면 들여쓴 줄을 실행
# (== 는 "같다"는 뜻. 3단계에서 자세히 본다)
print('--- 1단계 ---')
for fruit in fruits:
    if fruit == '포도':
        print(f"{fruit}: 찾았다!")
    else:
        print(f"{fruit}: 아님")

# ── 2단계: elif ──
# elif 조건: → 앞의 조건이 거짓일 때, 다음 조건을 검사 (else if 의 줄임)
# 위에서부터 차례로 검사하고, 처음 참인 것 하나만 실행한다
print('--- 2단계 ---')
for fruit in fruits:
    if len(fruit) == 2:
        print(f"{fruit}: 2글자")
    elif len(fruit) == 3:
        print(f"{fruit}: 3글자")
    else:
        print(f"{fruit}: 4글자 이상")

# ── 3단계: 비교 연산자 (comparison operator) ──
# ==  같다        !=  다르다        >=  크거나 같다
# 비교 결과는 항상 True 또는 False (불리언, boolean)
print('--- 3단계 ---')
print('사과' == '사과')     # True
print('사과' != '포도')     # True
print(len('바나나') >= 4)   # False

# ── 4단계: and / or ──
# A and B → 둘 다 참이어야 참
# A or B  → 하나만 참이어도 참
print('--- 4단계 ---')
for fruit in fruits:
    if fruit == '사과' or fruit == '딸기':
        print(f"{fruit}: 빨간 과일")
    if len(fruit) >= 3 and fruit != '바나나':
        print(f"{fruit}: 3글자 이상인데 바나나는 아님")

# ── 연습 문제 1 ──
# korean_words 에서 3글자 이상인 단어만 출력하기
# 힌트: for 로 하나씩 꺼내고 → if 와 len(), >= 로 검사
korean_words = ['꿈', '우리말', '하늘', '대한민국', '무지개', '별']
for korean_word in korean_words:
    if len(korean_word) >= 3:
        print(korean_word)

# ── 연습 문제 2 ──
# korean_words 에서 2글자 이상 3글자 이하인 단어만 출력하기
# 힌트: 조건 두 개를 and 로 묶는다. "이하"는 <= 를 쓴다
for korean_word in korean_words:
    if len(korean_word) <= 3 and len(korean_word) >= 2:
        print(korean_word)