# Space Shooter - Videojuego MISO

## Link al juego publicado
https://ramirez-alejo.itch.io/asteroidsshooter

## Descripción del Juego
Space Shooter es un juego de disparos espaciales donde el jugador controla una nave que debe enfrentarse a asteroides y naves enemigas. El objetivo es destruir todos los asteroides y enemigos mientras se evita ser golpeado por ellos.

## Características Principales
- Control intuitivo de la nave del jugador
- Diferentes tipos de asteroides
- Naves enemigas con patrones de movimiento
- Sistema de disparo básico y especial (con recarga)
- Efectos visuales de explosiones
- Efectos de sonido inmersivos


## Personalizaciones
- Los enemigos de tipo "Hunter" patrullan un area (Se mueven en un rango y direccion definidos en la configuración)
- Poder Especial: Disparo en todas direcciones (12 disparos a la vez separados por 30 grados), este tiene una nueva animacion y un nuevo sonido
- Recarga de poder especial: 15 segundos, Se muestra el progreso de la recarga en la parte inferior izquierda de la pantalla a manera de porcentaje
- Se Agregan asteroides a la configuracion del juego

## Requisitos del Sistema
- Navegador web moderno 

## Instalación
1. Clone el repositorio:
```
git clone [URL del repositorio]
```

2. Navegue hasta el directorio del proyecto:
```
cd Miso-VideoJuegos/Semana4
```

3. Instale las dependencias:
```
pip install -r requirements.txt
```

## Cómo Jugar
1. Ejecute el juego:
```
python main.py
```

2. Controles:
   - Flechas direccionales: Mover la nave
   - Click Izquierdo: Disparo normal
   - Click Derecho: Disparo especial
   - Tecla `P`: Pausar o reanudar el juego

## Estructura del Proyecto
- `assets/`: Contiene recursos del juego
  - `cfg/`: Archivos de configuración en JSON
  - `fnt/`: Fuentes tipográficas
  - `img/`: Imágenes
  - `snd/`: Sonidos
- `src/`: Código fuente del juego
  - `ecs/`: Sistema de Entidad-Componente
  - `engine/`: Motor del juego

## Versiones Disponibles
- PC: Ejecute `main.py`
- Web: Disponible en la ruta [AsteroidsShooter](https://ramirez-alejo.itch.io/asteroidsshooter)

## Arquitectura del Juego
El juego está construido utilizando una arquitectura basada en Entidad-Componente-Sistema (ECS), lo que permite una organización modular y extensible del código.

## Créditos
Desarrollado como parte del curso MISO-VideoJuegos de la Universidad de los Andes.
- Alejandro Ramírez