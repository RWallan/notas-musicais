# Notas musicais

![logo do projeto](assets/logo.png){width="300" .center}

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.

Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcomando relacionado a cada ação que a aplicação pode relaizar. Como: `escala`, `acorde` e `campo-harmonico`.

{% include "templates/cards.html" %}

{% include "templates/instalacao.md" %}

## Como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
{{ commands.run }} escala
```

Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ D │ E  │ F#  │ G  │ A │ B  │ C#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`:

```bash
{{ commands.run }} escala F#
```

Retornando:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Alteração da tonalidade da escala

Você pode alterar a tonalidade da escala também. Esse é o segundo parâmetro da linha de comando. Por exemplo, a escala de `C# maior`:

```bash
{{ commands.run }} escala C# menor
```

Retornando:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Acordes

Uso básico:

```bash
{{ commands.run }} acorde

┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Variações na cifra

```bash
{{ commands.run }} acorde C+

┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento você pode usar acordes:

* maiores
* menores
* diminuto e
* aumentado

### Campo Harmonônico

Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
{{ commands.run }} campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica de `C` e o campo harmônico `maior`.

#### Alterações no campo harmônico

Você pode alterar os parâmetros da tônica e da tonalidade.

```bash
{{ commands.run }} campo-harmonico [OPTIONS] [NOTA] [TONALIDADE]
```

##### Alterações na tônica do campo

Um exemplo com o campo harmônico de `E`:

```bash
{{ commands.run }} campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

##### Alterações na tonalidade do campo

Um exemplo utilizando o campo harmônico de `E` na tonalidade `menor`:

```bash
{{ commands.run }} campo-harmonico E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode executar a flag `--help`:

```bash
{{ commands.run }} --help

 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ acorde                                                                                                               │
│ campo-harmonico                                                                                                      │
│ escala                                                                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Mais informações sobre os subcomandos

As informações sobre as informações sobre os subcomandos podem ser acessadas usando a flag `--help` após o nome do parâmetro. Um exemplo do uso do `help` nos campos harmônicos:

```bash
{{ commands.run }} campo-harmonico --help

 Usage: notas-musicais campo-harmonico [OPTIONS] [NOTA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   nota            [NOTA]        Tônica do campo harmônico. [default: C]                                              │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico. [default: maior]                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
