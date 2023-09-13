import inspect
import sys

from contrib.filters.abstract import AbstractSpamFilter


def get_spam_filter_classes() -> list[AbstractSpamFilter]:
    from contrib.filters import spam

    classes = []

    for name, obj in inspect.getmembers(sys.modules[spam.__name__]):
        if inspect.isclass(obj) and not inspect.isabstract(obj):
            classes.append(obj)

    return classes


def use_filter_class(use: bool = True):
    def wrapper(cls: AbstractSpamFilter):
        if not use:
            cls.filter = lambda string: False

        return cls

    return wrapper
