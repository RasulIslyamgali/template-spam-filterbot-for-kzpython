"""
Add your filter classes here
"""
from utils import use_filter_class
from .abstract import AbstractSpamFilter


@use_filter_class()
class SimpleFilter(AbstractSpamFilter):
    def filter(self) -> bool:
        return self._some_filter_logic()

    def _some_filter_logic(self) -> bool:
        return self.string.__contains__('текст который не пройдет проверку')
