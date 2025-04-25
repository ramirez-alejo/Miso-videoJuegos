from src.engine.services.images_service import ImagesService
from src.engine.services.sounds_servive import SoundsService


class ServiceLocator:
    
    images_service = ImagesService()
    sounds_service = SoundsService()