"""
Add your filter classes here
"""

from .abstract import AbstractSpamFilter


class SimpleFilter(AbstractSpamFilter):
    def filter(self) -> bool:
        return self._some_filter_logic()

    def _some_filter_logic(self) -> bool:
        return self.string.__contains__('текст который не пройдет проверку')
