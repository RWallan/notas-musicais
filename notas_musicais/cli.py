from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.escalas import escala

console = Console()
app = Typer()


@app.command()
def escalas(
    nota: str = Argument('C', help='Tônica da escala.'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala.'),
):
    table = Table()

    notas, graus = escala(nota, tonalidade).values()

    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)

    console.print(table)
