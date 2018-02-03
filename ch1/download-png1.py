
#-*- coding: utf-8 -*-
# 라이브러리 읽어 들이기
import urllib.request

# URL과 저장 경로 지정하기
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR60NGrI683oZRe3O_dpew-b_OYdxNv3WTHNsU2Kk34TExC_AwI"
savename = "test.png"

# 다운로드
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")

