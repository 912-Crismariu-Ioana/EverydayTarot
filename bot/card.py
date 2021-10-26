class Card:
    def __init__(self, id, name, image, meaning):
        self._id = id
        self._name = name
        self._image = image
        self._meaning = meaning

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image

    @property
    def meaning(self):
        return self._meaning

    def __eq__(self, other):
        return self.id == other.id
