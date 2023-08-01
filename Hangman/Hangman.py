import time

# 처음 인사
name = input('What is your name?  ')


print('Hi, ' + name , 'Time to play Hangman Game!')
print()

time.sleep(1)
    
print('Start Loading ... ')
print()
time.sleep(0.5)

# 정답 단어
word = 'butterfly'

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
        print('Congratulations!')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
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
            print('Your Hangman game failed!')