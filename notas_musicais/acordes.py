from notas_musicais.escalas import NOTAS, escala


def _menor(cifra: str) -> tuple[str]:
    nota, _ = cifra.split('m')

    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=1)]
        graus = ['I', 'III-', 'V+']
    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']

    return notas, graus


def semitom(nota: str, *, intervalo):
    posicao = NOTAS.index(nota) + intervalo

    return NOTAS[posicao % 12]


def triade(nota: str, tonalidade: str) -> list[str]:
    GRAUS = (0, 2, 4)
    notas_da_escala = escala(nota, tonalidade)['notas']

    return [notas_da_escala[grau] for grau in GRAUS]


def acorde(cifra: str) -> dict[str, list[str]]:
    """
    Gera as notas de um acorde partindo de uma cifra.

    Parameters:
        cifra (str): Um acorde em forma de cifra.

    Returns:
        dict[str, list[str]]: Um dicionário com as notas e os graus correspondentes.

    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('F#')
        {'notas': ['F#', 'A#', 'C#'], 'graus': ['I', 'III', 'V']}
    """

    if 'm' in cifra:
        notas, graus = _menor(cifra)
    elif '°' in cifra:
        nota, _ = cifra.split('°')
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=-1)]
        graus = ['I', 'III-', 'V-']
    elif '+' in cifra:
        nota, _ = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semitom(quinta, intervalo=1)]
        graus = ['I', 'III', 'V+']
    else:
        graus = ['I', 'III', 'V']
        notas = triade(cifra, 'maior')

    return {'notas': notas, 'graus': graus}
