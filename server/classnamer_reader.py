import re
from typing import List

from page_reader import PageReader


class ClassNamerReader(PageReader):

    def extract(self) -> List[str]:
        class_name = self.get_class_name()
        class_name_words = re.findall('[A-Z][^A-Z]*', class_name)
        return class_name_words

    def get_class_name(self) -> str:
        return self._read_attr("p", {"id": "classname"})
