import re
from abc import ABCMeta, abstractproperty


class Path(object):
    def __init__(self):
        self.items = []

    def add(self, path_node):
        self.items.append(path_node)

    def __getitem__(self, key):
        return self.items[key]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        self.cache_index = 0

        return self

    def next(self):
        # print 'index', self.cache_index, self.items
        self.cache_index += 1
        if len(self.items) >= self.cache_index:
            return self.items[self.cache_index - 1]

        raise StopIteration


class PathNode(object):
    __metaclass__ = ABCMeta

    def __init__(self, value=None, data=None):
        self.data = data
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __iter__(self):
        self.cache_index = 0

        return self

    def next(self):
        # print 'index', self.cache_index, self.items
        self.cache_index += 1
        if len(self.children) >= self.cache_index:
            return self.children[self.cache_index - 1]

        raise StopIteration

    @abstractproperty
    def is_text(self):
        pass

    @abstractproperty
    def is_params(self):
        pass

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        # print self.children
        return '[Path: {0}, Data: {1}, Branches: {2}]'.format(
            self.value,
            self.data,
            ', '.join([str(_) for _ in self.children
                       ]))


class PathTextNode(PathNode):
    @property
    def is_params(self):
        return False

    @property
    def is_text(self):
        return True


class PathParamNode(PathNode):
    @property
    def is_params(self):
        return True

    @property
    def is_text(self):
        return False