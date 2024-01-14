import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_erviko():
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