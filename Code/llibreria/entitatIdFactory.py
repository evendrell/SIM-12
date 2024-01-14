

class entitatIdFactory(object):
    _id = 0
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(entitatIdFactory, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._id = 0

    @classmethod
    def get_big_id(cls):
        return cls._id
    @classmethod
    def update_id(cls, value):
        cls._id += value

    def get_id(self):
        returning_id = self.get_big_id()
        self.update_id(1)
        return returning_id

