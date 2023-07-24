import sys
import time
sys.path.append('../')
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_page_content(driver:webdriver.Chrome,URL:str) -> list:
    results = []
    driver.get(URL)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    for n_game in range(1,31):
        if not driver.find_elements(By.XPATH,f"/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div[1]/div[{n_game}]/div/div/div[2]/div/div/p"):
            break
        odds = [0.]*3
        result = -1
        for n_team in range(2,5):
            component = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div[1]/div[{n_game}]/div/div/div[{n_team}]/div/div/p")
            component_attribute = component.get_attribute(name="class")
            odds[n_team-2] = float(component.text)
            if component_attribute.find("gradient-green ") != -1:
                result = n_team-2
        assert result > -1 
        results.append((tuple(odds),result))
    driver.close()
    driver.quit()
    return results
    
if __name__ == "__main__":
    options= webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    r = get_page_content(driver=driver,URL="https://www.oddsportal.com/football/france/ligue-1-2022-2023/results/")
    print(r)