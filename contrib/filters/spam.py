from .abstract import AbstractSpamFilter


class SimpleFilter(AbstractSpamFilter):
    def filter(self) -> bool:
        return self._some_filter_logic()

    def _some_filter_logic(self) -> bool:
        if self.string.__contains__('текст который не пройдет проверку'):
            return False
        return True
