# Notas musicais

![logo do projeto](assets/logo.png){width="300" .center}

## Como usar?

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ D │ E  │ F#  │ G  │ A │ B  │ C#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`:

```bash
poetry run escalas F#
```

Retornando:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Alteração da tonalidade da escala

Você pode alterar a tonalidade da escala também. Esse é o segundo parâmetro da linha de comando. Por exemplo, a escala de `C# maior`:

```bash
poetry run escalas C# maior
```
Retornando:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ C# │ D# │ F   │ F# │ G# │ A# │ C   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode executar a flag `--help`:

```bash
poetry run escalas --help

 Usage: escalas [OPTIONS] [NOTA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   nota            [NOTA]        Tônica da escala. [default: C]                                                       │
│   tonalidade      [TONALIDADE]  Tonalidade da escala. [default: maior]                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell.             │
│                                                              [default: None]                                         │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or  │
│                                                              customize the installation.                             │
│                                                              [default: None]                                         │
│ --help                                                       Show this message and exit.                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
