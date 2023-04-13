from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    tonica = 'c'
    tonalidade = 'maior'

    resultado = escala(tonica, tonalidade)

    assert resultado


def test_deve_retornar_uma_mensagem_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe , tente uma desssas {NOTAS}'

    with raises(ValueError) as erro:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == erro.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'C'
    tonalidade = 'tonalidade'

    mensagem_de_erro = (
        f'Essa escala não existe ou não foi implementada,'
        f'tente uma dessas {list(ESCALAS.keys())}'
    )

    with raises(KeyError) as erro:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == erro.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica: str, esperado: list):
    resultado = escala(tonica, 'maior')

    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = 'C'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
