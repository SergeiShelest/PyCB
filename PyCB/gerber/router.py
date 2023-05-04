def merge_dicts(d1, d2):
    for k, v in d1.items():
        if k in d2:
            d2[k] = merge_dicts(v, d2[k])

    d1.update(d2)
    return d1


def build_brunch(nodes):
    tmp = nodes.pop(-1)
    for node in reversed(nodes):
        d = {}
        d.update({node: tmp})
        tmp = d

    return tmp


class ActionNotFound(Exception):
    def __init__(self, parent):
        self.parent = parent

    def __str__(self):
        return "No action found for pattern '{}'".format(self.parent)


class Router:
    SPLITTER = "/"

    def __init__(self):
        self.actions_tree = {}

    def call(self, pattern, *args):
        self.get_action(pattern)(*args)

    def get_action(self, pattern):
        nodes = pattern.split(self.SPLITTER)
        tmp = self.actions_tree

        for node in nodes:
            tmp = tmp.get(node)
            if not tmp:
                raise ActionNotFound(pattern)

        return tmp

    def action(self, pattern):
        def inner(func):
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)

            self.add_action(pattern, wrapper)
            return wrapper
        return inner

    def add_action(self, pattern, func):
        nodes = pattern.split(self.SPLITTER)
        nodes.append(func)
        new_brunch = build_brunch(nodes)

        self.actions_tree = merge_dicts(self.actions_tree, new_brunch)
