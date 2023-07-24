import sys
sys.path.insert(0,'./')
from src.aggregator import get_page_content

class TestAggregator:
    def test_get_page_content(self):
        url:str = "https://www.oddsportal.com/football/france/ligue-1-2022-2023/results/"
        content = get_page_content(url)
        assert (content > 0)
