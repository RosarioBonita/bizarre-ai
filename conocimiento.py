HISTORIA = """
JoJo's Bizarre Adventure es una serie de manga y anime creada por
Hirohiko Araki.

La historia sigue a diferentes miembros de la familia Joestar a través
de distintas generaciones. Cada parte presenta un protagonista diferente,
conocido generalmente como un JoJo.

Phantom Blood es la primera parte y tiene como protagonista a Jonathan
Joestar. La historia presenta su conflicto con Dio Brando.

Battle Tendency tiene como protagonista a Joseph Joestar, nieto de
Jonathan Joestar. Joseph se enfrenta a los llamados Hombres del Pilar.

Stardust Crusaders tiene como protagonista a Jotaro Kujo, nieto de
Joseph Joestar. Jotaro viaja junto con sus aliados para enfrentarse a Dio.

Diamond is Unbreakable tiene como protagonista a Josuke Higashikata.
La historia se desarrolla principalmente en Morioh.

Golden Wind tiene como protagonista a Giorno Giovanna.
Giorno está relacionado con Dio y busca convertirse en una figura
importante dentro de Passione.

Stone Ocean tiene como protagonista a Jolyne Cujoh, hija de Jotaro Kujo.
Gran parte de la historia ocurre en una prisión de Florida.
"""


PERSONAJES = {

    "Jonathan Joestar": {
        "parte": "Phantom Blood",
        "descripcion": """
Jonathan Joestar es el protagonista de Phantom Blood.
Es conocido por su nobleza, honor y determinación.
Su principal enemigo es Dio Brando.
"""
    },

    "Dio Brando": {
        "parte": "Phantom Blood / Stardust Crusaders",
        "descripcion": """
Dio Brando es uno de los principales antagonistas de
JoJo's Bizarre Adventure.

Comienza como rival de Jonathan Joestar y posteriormente
se convierte en una amenaza para generaciones posteriores
de la familia Joestar.
"""
    },

    "Joseph Joestar": {
        "parte": "Battle Tendency / Stardust Crusaders",
        "descripcion": """
Joseph Joestar es el protagonista de Battle Tendency y
posteriormente participa en Stardust Crusaders.

Se caracteriza por su inteligencia, creatividad y capacidad
para engañar a sus enemigos.
"""
    },

    "Jotaro Kujo": {
        "parte": "Stardust Crusaders",
        "descripcion": """
Jotaro Kujo es el protagonista de Stardust Crusaders.

Es nieto de Joseph Joestar y viaja hasta Egipto para
enfrentarse a Dio.
"""
    },

    "Josuke Higashikata": {
        "parte": "Diamond is Unbreakable",
        "descripcion": """
Josuke Higashikata es el protagonista de
Diamond is Unbreakable.

La historia ocurre principalmente en Morioh.
"""
    },

    "Giorno Giovanna": {
        "parte": "Golden Wind",
        "descripcion": """
Giorno Giovanna es el protagonista de Golden Wind.

Está relacionado con Dio y busca convertirse en una
figura importante dentro de Passione.
"""
    },

    "Jolyne Cujoh": {
        "parte": "Stone Ocean",
        "descripcion": """
Jolyne Cujoh es la protagonista de Stone Ocean.

Es hija de Jotaro Kujo y gran parte de su historia
ocurre en una prisión de Florida.
"""
    }
}


def obtener_conocimiento():

    texto = HISTORIA

    texto += "\n\nPERSONAJES:\n"

    for nombre, datos in PERSONAJES.items():

        texto += f"""
Nombre: {nombre}
Parte: {datos["parte"]}
Descripción: {datos["descripcion"]}
"""

    return texto