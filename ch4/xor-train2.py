import pandas as pd
# 사이킷런
from sklearn import svm, metrics

# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
xor_df = pd.DataFrame(xor_input)
#print(xor_df) # 전체 테이블 형태
xor_data = xor_df.ix[:,0:1] # 데이터
#print(xor_data) # 테이블의 데이터
xor_label = xor_df.ix[:,2] # 값
#print(xor_label) # 테이블의 값

# 데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
print(pre) # 예측 값

# 정답률 구하기
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률=", ac_score)

