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

    def get_entity(self, component_mask):
        for entity in self._entities:
            if component_mask <= entity.component_mask():
                return entity

    def create_entity(self, components):
        entity = Entity(self._next_entity_guid)
        for component in components:
            entity.components[type(component)] = component
        self._entities.append(entity)
        self._next_entity_guid += 1

    def add_system(self, system):
        self._systems.append(system)
        self._systems.sort(key=lambda s: s.priority)

    def step(self):
        for system in self._systems:
            system.update(self)
