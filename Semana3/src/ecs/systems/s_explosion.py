import esper
from src.ecs.components.c_explosion import CExplosion

def system_explosion(world: esper.World, delta_time: float):
    # Track entities to remove
    entities_to_remove = []
    
    # Process all explosions - get_components returns (entity_id, (component1, component2, ...))
    for entity, (explosion_component,) in world.get_components(CExplosion):
        # Update explosion time
        explosion_component.time_remaining -= delta_time
        
        # Check if explosion should be removed
        if explosion_component.time_remaining <= 0:
            entities_to_remove.append(entity)
    
    # Remove completed explosions
    for entity in entities_to_remove:
        world.delete_entity(entity, True)
