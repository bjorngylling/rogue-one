from ecs import Entity


class World(object):
    def __init__(self, seed):
        self.seed = seed
        self._entities = []
        self._systems = []
        self._next_entity_guid = 0
        self.map = None

    @property
    def entities(self):
        return self._entities

    def create_entity(self, components):
        entity = Entity(self._next_entity_guid)
        entity.components.add(components)
        self._entities.add(entity)
        self._next_entity_guid += 1

    def add_system(self, system):
        self._systems.add(system)
        self._systems.sort(key=lambda s: s.priority)

    def step(self):
        for system in self.systems:
            system.update(self)
