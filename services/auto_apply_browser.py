from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def launch_browser():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    return driver


def open_job_page(url):
    driver = launch_browser()

    driver.get(url)

    return driver