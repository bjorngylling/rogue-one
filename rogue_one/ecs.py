import abc


class Entity(object):

    def __init__(self, guid):
        self._components = dict()
        self._guid = guid

    def __repr__(self):
        return "<Entity name:%s, guid:%s, components:%s>" \
            % (self.__name__, self._guid, self._components)

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

    def component_mask(self):
        return set(self._components)

    @property
    def components(self):
        return self._components

    def add_component(self, component):
        self._components[type(component)] = component


class Component(object):
    """All components inherit from this class."""
    pass


class System(object):
    """Priority is 0 by default. That is the highest priority, i.e.
    that system will be updated first. No priority is guaranteed among
    many systems with equal priority."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, priority=0):
        self.priority = priority

    @abc.abstractmethod
    def component_mask(self):
        """Should return a set of Component types
        (ex: {VelocityComponent, PositionComponent})"""
        pass

    @abc.abstractmethod
    def process_components(self, components):
        pass

    def update(self, world):
        for entity in world.entities:
            if self.component_mask() <= entity.component_mask():
                self.process_components({k: entity.components[k]
                                         for k in self.component_mask()})
