# Section06-01
# Selenium
# Selenium 사용 실습(1) - 설정 및 기본 테스트

# https://sites.google.com/a/chromium.org/chromedriver/downloads

# selenium 임포트
from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
browser = webdriver.Chrome('./webdriver/chromedriver')

# 크롬 브라우져 대기 - 속도가 조금씩 달라서, 웹드라이버 쓸때는 조금씩 타이밍을 주는게 좋음.
browser.implicitly_wait(5)

# print(dir(browser))

# 브라우져 사이즈
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://daum.net')

# 페이지 내용
print('Page Content : {}'.format(browser.page_source))

print()
print()

# 세션 값 출력. 브라우저 엔진을 가지고 움직이기 때문에, 세션과 쿠키를 다 가지고 있음. 진짜 브라우져를 가지고 접근하는 것.
print('Session ID : {}'.format(browser.session_id))

# 페이지 타이틀
print('Title : {}'.format(browser.title))

# 현재 URL
print('URL : {}'.format(browser.current_url))

# 현재 쿠키 정보 출력
print('Cookies : {}'.format(browser.get_cookie))

# 검색창 input 선택
element = browser.find_element_by_css_selector("div.inner_search > input.tf_keyword")

# 검색어 입력
element.send_keys('고려화학매트')

# 검색
element.submit()


#스크린샷 저장 1
browser.save_screenshot("./resources/website_ch1.jpg")

#스크린샷 저장 2
browser.get_screenshot_as_file("./resources/website_ch2.jpg")

#  브라우져 종료
browser.quit()



