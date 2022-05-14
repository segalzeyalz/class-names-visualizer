from abc import ABC

import requests
from bs4 import BeautifulSoup


class PageReader(ABC):
    def __init__(self, url: str):
        page_with_class_names = requests.get(url)
        self.site_soup = BeautifulSoup(page_with_class_names.text, 'html.parser')

    def extract(self):
        raise NotImplemented

    def _read_attr(self, tag: str, attr: dict) -> str:
        return self.site_soup.find(tag, attr).text
