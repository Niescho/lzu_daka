import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class User:
    def __init__(self, uid, pwd):
        self.uid = uid
        self.pwd = pwd


def sign_in(uid, pwd):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://my.lzu.edu.cn/main")
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(uid)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pwd)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]/button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="my-stores"]/li[2]/a').click()
        driver.find_element(By.XPATH, '//*[@id="my-stores"]/li[2]/a/div[2]/p[2]/span').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="my-apps"]/li[1]/a/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="my-apps"]/li[1]/a/div[2]/p[2]/span[1]').click()
        time.sleep(5)
        driver.switch_to.frame('iframe')
        driver.find_element(By.XPATH,
                            '/html/body/uni-app/uni-page/uni-page-wrapper/'
                            'uni-page-body/uni-view/uni-view[3]/uni-view/'
                            'uni-form/span/uni-view[13]/uni-button').click()

        time.sleep(1)
        print("Successful")
    except Exception:
        print("Unsuccessful")
    finally:
        driver.quit()


users = [User('请更改为你的邮箱号或你的校园卡号', '请更改为你的密码'),
        #如果是多用户请如上范式增加User

         ]

for user in users:
    sign_in(user.uid, user.pwd)
