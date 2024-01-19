import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_untill(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window()  # 브라우저 창 최대화

url = 'https://flight.naver.com/'
browser.get(url)

# time.sleep(1)  # 1초 대기
wait_untill('//button[text() = "가는 날"]')  # 나올 때까지 30초 대기
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

# 가는 날
wait_untill('//b[text() = "22"]')
day22 = browser.find_elements(By.XPATH, '//b[text() = "22"]')
day22[0].click()

# 오는 날
wait_untill('//b[text() = "26"]')
day26 = browser.find_elements(By.XPATH, '//b[text() = "26"]')
day26[0].click()

# 도착 클릭
wait_untill('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

# 국내 클릭
# time.sleep(1)  # 1초 대기
wait_untill('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]') 
domestic.click()

# 제주 클릭
wait_untill('//i[contains(text(), "제주국제공항")]')
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

# 항공권 검색 클릭
wait_untill('//span[contains(text(), "항공권 검색")]')
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]') 
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA"]')))
print(elem.text)

input('종료하려면 Enter 키를 입력하세요')
# browser.quit()  # 브라우저 종료