import time
# csv 처리
import csv
# 랜덤
import random
# 사운드 처리
# import winsound

# 현재 경로로 작업경로 설정해주기
import os
currentPath = os.getcwd()
os.chdir(currentPath+"/Desktop/DEV/PY/python_basic/practice")

# 처음 인사
name = input('What is your name?  ')


print('Hi, ' + name , 'Time to play Hangman Game!')
print()

time.sleep(1)
    
print('Start Loading ... ')
print()
time.sleep(0.5)


# CSV단어 리스트
words = []

# 문제 csv 파일 로드
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # header는 없으므로 skip
    next(reader)
    for c in reader:
        words.append(c)

# list shuffle
random.shuffle(words)
q = random.choice(words)

# 정답 단어
word = q[0].strip() # 양쪽 공백 제거

# 추측 단어
guesses = ''

# chance
turns = 10

# 핵심 while Loop
# if chance count left
while turns > 0:
    # Fail count(단어 매치 수)
    failed = 0
    print(guesses)
    
    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함된 경우
        if char in guesses: # 처음에는 guesses 공백이므로 실행 안됨
            print(char, end = ' ')
        else:
            # 틀린 경우/아직 못맞춘 경우 _ 처리
            print('_', end = ' ')
            failed += 1
    # 처음 실행시 failed 가 6이 되어있어 실행되지 않는다.    
    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME) # sound를 재생할 때는
        print('Congratulations!')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input('Guess a character! ')

    # 입력한 단어들 더하기
    guesses += guess

    # 정단 단어에 추측한 문자가 포함 X경우
    if guess not in word:
        turns -= 1
        print('Oops! Wrong')
        print(f'You have {turns} more guesses!')
        print('**************************')

        # 실패 메세지
        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print('Your Hangman game failed!')