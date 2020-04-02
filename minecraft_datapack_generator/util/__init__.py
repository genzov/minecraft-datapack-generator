class Util:

    def __init__(self, name: str, namespace: str = 'minecraft'):
        self.name = name
        self.namespace = namespace

    def __str__(self):
        return f'{self.namespace}:{self.name}'
