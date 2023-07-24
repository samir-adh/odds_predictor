import sys
sys.path.insert(0,'./')
from src.aggregator import get_page_content
from selenium import webdriver

class TestAggregator:
    def test_get_page_content(self):
            options= webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            r = get_page_content(driver=driver,URL="https://www.oddsportal.com/football/france/ligue-1-2022-2023/results/")
            assert len(r) == 30
