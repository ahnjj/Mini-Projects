# Salary_prediction
## No
1

## Case
Kaggle에 있는 dataset으로 salary prediction
2개 데이터, 총 34개 데이터셋으로 간단한 머신러닝 학습용 실습을 진행했다.

## Issue
처음 visualize했는데 직선에 가까운 line이 나왔다 ;

## Solve
iloc함수 인자를 잘못 넘겨줘서 y - y 그래프를 그렸던 것이었다.
iloc[:,:] / iloc[::] Column 값을 구할 때와 Row 값을 구할 때 꼼꼼하게 살피자.
