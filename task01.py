#2013년 9월 부터
#2016년 9월 까지
#각 월별 30개 영화의 주소를 긁어와서 txt 파일로 저장함
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

# Setup
service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def scrape_and_save():
    time.sleep(0.3)
    months = [f'{year}{month:02d}' for year in range(2013, 2017) for month in range(1, 13)
              if not (year == 2013 and month < 9) and not (year == 2016 and month > 9)]

    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

    with open('addresses.txt', 'w') as file:
        for month in months:
            url = f'https://movie.daum.net/ranking/boxoffice/monthly?date={month}'
            driver.get(url)

            for i in range(1, 31):  # Assuming there are always 30 items in the list
                xpath = f'//*[@id="mainContent"]/div/div[2]/ol/li[{i}]/div/div[2]/strong/a'
                element = driver.find_element(By.XPATH, xpath)
                address = element.get_attribute('href')
                file.write(f'{address}\n')
                print(f'Scraped address from item {i} for {month}: {address}')

    driver.quit()


# Call the function to execute the task
scrape_and_save()