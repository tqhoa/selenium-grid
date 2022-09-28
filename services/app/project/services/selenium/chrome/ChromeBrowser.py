from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from project.config import Config
import undetected_chromedriver.v2 as uc
import time

config = Config()


class ChromeBrowser:

    def __init__(self) -> None:
        pass

    def test(self):
        print("TEST")

    def searchGoogle(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        # options.add_argument('--start-fullscreen')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--incognito")
        options.add_argument("--disable-web-security")
        options.add_argument(
            '--disable-blink-features=AutomationControlled')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_argument("disable-infobars")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-site-isolation-trials")

        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            options=options
        )

        browser.get('https://youtube.com')
        # element = browser.find_element(By.NAME, "q")
        # element.send_keys('test' + Keys.RETURN)

        """
        print(1)
        time.sleep(120)
        browser.quit()
        print(2)
        """
