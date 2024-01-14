import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_login():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get("http://test.erviko.rs")
    message = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/div/span").text
    print(message)
    assert "v" in message
    driver.fullscreen_window()
    driver.find_element(By.ID, "mat-input-0").send_keys("stefancacak32@gmail.com")
    driver.find_element(By.ID, "mat-input-1").send_keys("Sifra123.")
    driver.find_element(By.CSS_SELECTOR, "body > app-root > div > app-login > div > mat-card > form > button").click()
    driver.implicitly_wait(5)
    time.sleep(5)


def test_changelanguage():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get("http://test.erviko.rs")
    driver.fullscreen_window()
    driver.find_element(By.ID, "mat-input-0").send_keys("stefancacak32@gmail.com")
    driver.find_element(By.ID, "mat-input-1").send_keys("Sifra123.")
    driver.find_element(By.CSS_SELECTOR, "body > app-root > div > app-login > div > mat-card > form > button").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[@id='toolbar']/span[3]/button").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-3']/div/button[1]").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-4']/div/button[2]").click()
    driver.implicitly_wait(5)
    naziv_menija = driver.find_element(By.XPATH, "//*[@id='app-navbar-left']/li[5]/a/span").text
    assert naziv_menija == "ADMINISTRACIJA"
    print(naziv_menija)
    time.sleep(2)
