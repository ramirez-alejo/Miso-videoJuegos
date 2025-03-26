import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def system_movement(world: esper.World, delta: float):
    components = world.get_components(CTransform, CVelocity)
    for _, (transform, velocity) in components:
        transform.position.x += velocity.speed.x * delta
        transform.position.y += velocity.speed.y * delta