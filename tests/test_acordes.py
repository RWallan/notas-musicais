from pytest import mark

from notas_musicais.acordes import acorde


@mark.parametrize(
    'nota, esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('F#', ['F#', 'A#', 'C#']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
    ],
)
def test_acorde_deve_retornar_as_notas_correspondentes(
    nota: str, esperado: list[str]
):
    resultado = acorde(nota)

    assert resultado['notas'] == esperado


@mark.parametrize(
    'cifra, esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def test_acorde_deve_retornar_os_graus_correspondentes(
    cifra: str, esperado: list[str]
):
    resultado = acorde(cifra)

    assert resultado['graus'] == esperado
