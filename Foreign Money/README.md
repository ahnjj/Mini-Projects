# Foreign Money

##  기능
1. 현찰 구매시 실시간 환율 적용 금액 ( API 사용 불가 )
2. 나라 환율 정보 전체 조회
3. 송금 받을 때 환율 적용 금액
4. 송금 할 때 환율 적용 금액
5. NLP : 그 나라의 은행명들 및 화폐 단위 정보 제공

## 기능별 세부 사항 및 issue

### 1. 현찰 구매시 실시간 환율 적용 금액
현찰 살때 / 팔때 = 매매기준율 + (매매기준율 * 통화별 스프레드) 

ctr_cur 
type : dict {country : currency}
1. input pattern1  : country name ~ X원 환전 
2. input pattern2 : won -> 그나라 돈으로
단위 X달러 만큼 환전하고 싶다 -> 나라 인식 -> 환율 찾기

#### Issue 
하나은행 환율 : 기업만 접근 가능한 api

#### Solve
1. 다른 api찾기
2. 이 기능 삭제
-> 일단 기능 제외하고 송금 받고 보내는 환율 기능적용

--------------------------------------------

### 2. 나라 환율 정보 전체 조회 summary
나라 - 환율 테이블 보여주기
#### Approach
pandas DataFrame 사용

#### Issue
테이블명이 'tts'같은 용어로 써있어서 변경해야한다.
나라 이름을 테이블의 가장 처음에 배치하고 싶다.

--------------------------------------------

### 3. 송금 받을때  TTB mode 1
input __ 단위 __ -> ttb * 돈 = 원으로 바꿔서 return '__원을 받습니다'

### 4. 송금 보낼때 TTS mode 2
input __ 단위 __ -> tts * 돈 = 원으로 바꿔서 '__ 원을 보냅니다'

#### Approach
json형태의 환율 정보 API에서 사용자의 input mode(보내기,받기)에 따라 환율 적용해서 원화 / 해당 currency로 변경해서 사용자에게 알려준다.

#### Issue
1. 중국과 유럽지역은 나라 이름 대신 '위안화', '유로'로 데이터가 저장되어 있다. 
2. 덴마크는 덴마아크로 검색

#### Solve
1. [나라 : 통화] 구조의 dictionary를 만들었다. -> 나라 / 통화 둘다 검색 가능하게 한다.
2. 

#### 추가 기능 / 추가 해결점
1. 나라 / 통화가 데이터에 없을 경우 오류 메세지를 출력한다.
2. 덴마아크.....
3. 최근 환율 그래프로 시각화 하고싶다.
4. 맨처음에 검색 가능한 나라/ 통화 띄워주기 (country info)

--------------------------------------------

### 5. 기타정보 제공
input : country name
return : 그 나라 은행 정보 및 화폐 단위 제공....

#### Approach 
NLP regular expression이용

1. url에 나라 이름 부분을 변수로 두고 input 을 받아 url post한다.

2. wikipedia api 사용

3. 통화 : Banknotes 부분을 nlp한다.
 Freq. used	¥1 RMB, ¥5 RMB, ¥10 RMB, ¥20 RMB, ¥50 RMB, ¥100 RMB
Coins	
 Freq. used	¥0.1 RMB, ¥0.5 RMB, ¥1 RMB
 Rarely used	¥0.01 RMB, ¥0.02 RMB, ¥0.05 RMB

4. list of banks in __ 나라이름 Page
