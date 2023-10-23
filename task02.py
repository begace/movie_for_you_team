# addresses.txt의 주소를 하나씩 읽어옴
# 클릭 : //*[@id="mainContent"]/div/div[2]/div[1]/ul/li[4]/a/span
# 클릭 x5 : //*[@id="alex-area"]/div/div/div/div[3]/div[1]/button
# 시작 xpath : /html/body/div[2]/main/article/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/ul[2]/li[1]/div/p
# 끝 xpath : /html/body/div[2]/main/article/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/ul[2]/li[160]/div/p
# 시작부터 끝까지 xpath의 텍스트 (영화 리뷰)를 가져와서 csv로 저장
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrape_reviews():
    driver = webdriver.Chrome()  # chromedriver가 PATH에 있는지 확인하세요
    data = []

    with open('addresses.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        driver.get(url.strip())  # 페이지로 이동

        # 페이지가 로드될 때까지 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]'))
        )

        # 제목 가져오기
        title_xpath = '//*[@id="mainContent"]/div/div[1]/div[2]/div[1]/h3/span[1]'
        title = driver.find_element(By.XPATH, title_xpath).text

        # 4번째 탭에서 URL을 가져와서 이동
        tab_xpath = '//*[@id="mainContent"]/div/div[2]/div[1]/ul/li[4]/a'
        tab_url = driver.find_element(By.XPATH, tab_xpath).get_attribute('href')
        driver.get(tab_url)

        # "더 보기" 버튼이 표시될 때까지 대기
        show_more_xpath = '//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button'
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, show_more_xpath))
        )

        # "더 보기" 버튼을 5번 클릭하여 더 많은 리뷰를 로드
        for _ in range(5):
            driver.find_element(By.XPATH, show_more_xpath).click()
            time.sleep(2)  # 콘텐츠가 로드되는데 시간을 주기 위해 지연 추가

        # start_xpath에서 end_xpath까지 리뷰 스크랩
        for i in range(1, 161):  # 160개의 리뷰가 로드되었다고 가정
            review_xpath = f'/html/body/div[2]/main/article/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/ul[2]/li[{i}]/div/p'
            elements = driver.find_elements(By.XPATH, review_xpath)
            if elements:  # 요소가 존재하면
                review_text = elements[0].text.replace('\n', ' ')  # 줄바꿈 제거
                data.append({'Title': title, 'Review': review_text})

    # 데이터를 CSV 파일에 저장
    df = pd.DataFrame(data)
    df.to_csv('reviews.csv', index=False)

    driver.quit()  # 드라이버 종료

# 작업을 실행하기 위해 함수 호출
scrape_reviews()
