from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def _main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r"/home/src/bin/chromedriver.exe",options=options)

    driver.get('https://www.google.co.jp/')
    search = driver.find_element_by_name('q')
    search.send_keys('Python')
    search.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.save_screenshot('search_results.png')

    driver.quit()

if __name__ == '__main__':
    _main()
