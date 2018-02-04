import urllib.request

# URL과 저장 경로 지정하기
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqHWuEM_m5SDUJTNNQscjlLD2iYuEPfz6LRRQJ98sfUgHiBrk4fw"
savename = "test.jpg"

# 다운로드

# request.urlopen()을 이용하면 곧바로 파일로 저장하는 것이 아니라 데이터를 파이썬 메모리 위에 올릴 수 있음
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다...!")