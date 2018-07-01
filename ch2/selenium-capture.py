# -*- coding: utf-8 -*-
from selenium import webdriver

url = "http://www.naver.com/"

# PhantomJS 드라이버 추출하기
# browser = webdriver.PhantomJS()
browser = webdriver.PhantomJS(executable_path='/phantomjs/bin/phantomjs')

# 3초 대기
browser.implicitly_wait(3)
# URL 읽어 들이기
browser.get(url)
# 화면을 캡처해서 지정하기
browser.save_screenshot("Website.png")
# 브라우저 종료하기
browser.quit()