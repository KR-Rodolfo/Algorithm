# 강의 배정 문제 (Activity Seclection Problem)
'''
    - 강의실이 하나 뿐인데, 이 강의실을 쓰고 싶은 강의는 많다.
    강의가 서로 겹치지 않고 최대한 많은 강의를 배정하라
'''

# greedy 기준: 가장 빨리 끝나는 강의를 우선적으로 배정한다.

S = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12] # i번째 강의의 시작시간
F = [4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14] # i번째 강의의 종료시간

L = [0] # 배정할 강의 리스트
k = 0 # 배정된 강의 리스트 중 마지막 강의의 번호
for lecture_num in range(1, len(F)):
    if F[k] <= S[lecture_num]:
        L.append(lecture_num)
        k = lecture_num
        
print(L)