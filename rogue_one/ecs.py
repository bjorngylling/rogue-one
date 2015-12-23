import abc


class Entity(object):
    __slots__ = ("_guid", "_components")

    def __init__(self, guid):
        self._guid = guid

    def __repr__(self):
        return "<Entity name:%s, guid:%s, components:%s>" \
            % (self.__name__, self._guid, self)

    def __hash__(self):
        return self._guid

    def __eq__(self, other):
        return self._guid == hash(other)

    def __ne__(self, other):
        return self._guid != hash(other)

    def __lt__(self, other):
        return self._guid < hash(other)

    def __le__(self, other):
        return self._guid <= hash(other)

    def __gt__(self, other):
        return self._guid > hash(other)

    def __ge__(self, other):
        return self._guid <= hash(other)


class Component(object):
    """All components inherit from this class.
    """
    pass


class System(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.entity_manager = None
        self.system_manager = None

    @abc.abstractmethod
    def update(self):
        pass
