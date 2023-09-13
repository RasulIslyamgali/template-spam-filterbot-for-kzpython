import inspect
import sys

from contrib.filters import spam
from contrib.filters.abstract import AbstractSpamFilter


def get_spam_filter_classes() -> list[AbstractSpamFilter]:
    classes = []

    for name, obj in inspect.getmembers(sys.modules[spam.__name__]):
        if inspect.isclass(obj) and not inspect.isabstract(obj):
            classes.append(obj)

    return classes
