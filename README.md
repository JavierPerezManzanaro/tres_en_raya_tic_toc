# **Juego del tic-toc o 3 en raya**

## Descripción
El tres en línea, también conocido como ceros y cruces, tres en raya (España, México, Ecuador y Bolivia), cerito cruz (en Cuba), michi (en Perú), triqui (en Colombia), cuadritos, juego del gato, gato (en Chile, Costa Rica y México), tatetí (en Argentina, Paraguay y Uruguay), totito (en Guatemala), triqui traka, equis cero, o la vieja (en Venezuela) es un juego de lápiz y papel entre dos jugadores: O y X, que marcan los espacios de un tablero de 3×3 alternadamente.
Fuente: https://es.wikipedia.org/wiki/Tres_en_línea

![<a href="https://commons.wikimedia.org/wiki/File:Tic_tac_toe.svg">Symode09</a>, Dominio público, a través de Wikimedia Commons](https://raw.githubusercontent.com/JavierPerezManzanaro/https---github.com-JavierPerezManzanaro-tres_en_raya_tic_toc/6091cf38f2bf0373c6bb96f65851169d71e6bc3d/Tic_tac_toe.svg?token=AOLDIXJVOJXTTCG2P2VDCFTELQLEO)




## Puntos de interés
Los puntos más destacados de la aplicación son estos:

### Motor gráfico
El juego no tiene motor gráfico, la intención es incluir el algoritmo de Minamax por lo que he omitido un interfaz gráfico. Más adelante se implantara para dejarlo completo

### Librerías
- El archivo requirements.txt esta creado para facilitar la instalación de las librerías
- Pese a que no hay motor gráfico se necesitan dos librerías para hacer un poco mas atractivo el juego. Estas son:
  - tabulate:
    - https://pypi.org/project/tabulate/
    - Se usa para mostrar el tablero de juego
  - colorama
    - https://pypi.org/project/colorama/
    - Se usa para dar color, dentro del tablero, a los dos tipos de fichas, las de cada jugador
- Otras librerías usadas:
  - itertools
    - Integrada en Python
    - itertools.cycle(iterable): Crea un iterador que retorna elementos del iterable y hace una copia de cada uno. Cuando el iterable es consumido, retornar los elementos de la copia almacenada. Se repite indefinidamente.
    - https://docs.python.org/es/3/library/itertools.html#itertools.cycle
  - logging
    - Integrada en Python
    - Logging proporciona un conjunto de funciones convenientes para un uso sencillo de registro
    - Aunque esta implementado desde el principio su uso principal va a ser para el desarrollo del Algoritmo MaxMin

### Creaciones de excepciones propias: try / except
No es que sean errores de programación, son errores lógicos que se pueden dar a la hora de solicitar la casilla. Estos son:
- Número de casilla mayor que 9
- Número de casilla menor que 0
- No se introduce un número, y, por último
- La casilla esta ocupada


## Próximas versiones
Las implementaciones previstas son:
- Incluir una Inteligencia artificial, concretamente el Algoritmo MaxMin para que juegue un humano contra la máquina
- Implementar que se empiece a jugar entre los dos jugadores de forma aleatoria
- Usar una interfaz gráfica


## Historial de versiones
### 1.1
- Mejoras menores
### 1.0
- Versión base


## Manifiesto de los archivos del repositorio
- README.md
  - El archivo que estas leyendo
- requirements.txt
    - Archivo con las librerías utilizadas


## Motivación
El mundo de la IA es muy interesante. Y esta es una buena forma de empezar a aprender.


## Créditos y agradecimientos
- A toda la comunidad web que me ha permitido ir ampliando mi formación
- A mi familia por su infinita paciencia

## Licencias y derechos de autor
CC (Creative Commons) de Reconocimiento – NoComercial – SinObraDerivada
![CC (Creative Commons) de Reconocimiento – NoComercial – SinObraDerivada](https://raw.githubusercontent.com/JavierPerezManzanaro/Maquetacion-de-masivos-responsive-html-con-noticias/main/Reconocimiento-no-comercial-sin-obra-derivada.png)

## Información de contacto del autor
Javier Pérez
javierperez@perasalvino.es

