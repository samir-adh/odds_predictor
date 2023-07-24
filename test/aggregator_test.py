import sys

sys.path.insert(0, "./")
from src.aggregator import *
from selenium import webdriver


class TestAggregator:
    def test_get_page_content(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        url = "https://www.oddsportal.com/football/france/ligue-1-2022-2023/results/"
        r = get_page_content(driver=driver, URL=url)
        assert len(r) == 30
        driver.close()
        driver.quit()

    def test_get_all_content(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        url = "https://www.oddsportal.com/football/france/ligue-1-2022-2023/results/"
        r = get_all_content(driver=driver, base_url=url, n_pages=8)
        assert len(r) > 30
        driver.close()
        driver.quit()
