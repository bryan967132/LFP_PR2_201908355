# Tabla de Tokens

| Descripción                               | Patrón                                          | Expresión regular      | ejemplos                      |
| ----------------------------------------- | ----------------------------------------------- | ---------------------- | ----------------------------- |
| Reservada RESULTADO                       | Palabra RESULTADO                               | RESULTADO              | RESULTADO                     |
| Reservada TEMPORADA                       | Palabra TEMPORADA                               | TEMPORADA              | TEMPORADA                     |
| Reservada JORNADA                         | Palabra JORNADA                                 | JORNADA                | JORNADA                       |
| Reservada GOLES                           | Palabra GOLES                                   | GOLES                  | GOLES                         |
| Reservada TABLA                           | Palabra TABLA                                   | TABLA                  | TABLA                         |
| Reservada PARTIDOS                        | Palabra PARTIDOS                                | PARTIDOS               | PARTIDOS                      |
| Reservada TOP                             | Palabra TOP                                     | TOP                    | TOP                           |
| Reservada ADIOS                           | Palabra ADIOS                                   | ADIOS                  | ADIOS                         |
| Reservada VS                              | Palabra VS                                      | VS                     | VS                            |
| Reservada LOCAL                           | Palabra LOCAL                                   | LOCAL                  | LOCAL                         |
| Reservada VISITANTE                       | Palabra VISITANTE                               | VISITANTE              | VISITANTE                     |
| Reservada TOTAL                           | Palabra TOTAL                                   | TOTAL                  | TOTAL                         |
| Reservada SUPERIOR                        | Palabra SUPERIOR                                | SUPERIOR               | SUPERIOR                      |
| Reservada INFERIOR                        | Palabra INFERIOR                                | INFERIOR               | INFERIOR                      |
| Valores asignados                         | Secuencia de caracteres alfanuméricos           | "[A-Za-z][0-9a-za-z]\*"| "Real Madrid","Barcelona"     |
| Valores numéricos                         | Secuencia de caracteres numéricos               | [0-9]\*                | 5,13,18,35,22                 |
| Signo menor que                           | Un caracter '<'                                 | '<'                    | <                             |
| Signo mayor que                           | Un caracter '>'                                 | '>'                    | >                             |
| Guion                                     | Un caracter '-'                                 | '-'                    | -                             |

# Gramática Libre de Contexto
| Producciones                              |
| ----------------------------------------- |
S ::= INICIO
INICIO ::= COMANDO
COMANDO ::= RESULTADO \| JORNADA \| GOLES \| TABLA \| PARTIDOS \| TOP \| pr_ADIOS
RESULTADO ::= pr_RESULTADO nomEquipo pr_VS nomEquipo pr_TEMPORADA TEMPORADA
JORNADA ::= pr_JORNADA numeroEntero pr_TEMPORADA TEMPORADA BANDERAS
GOLES ::= pr_GOLES CONDICIONEQUIPO pr_TEMPORADA TEMPORADA
TABLA ::= pr_TABLA pr_TEMPORADA TEMPORADA BANDERAS
PARTIDOS ::= pr_PARTIDOS nomEquipo pr_TEMPORADA TEMPORADA BANDERAS
TOP ::= pr_TOP CONDICIONTOP pr_TEMPORADA TEMPORADA BANDERAS
TEMPORADA ::= menorQue año guion año mayorQue
BANDERAS ::= BANDERAS BANDERA valor
BANDERAS ::= BANDERA valor \| cadena_vacia
BANDERA ::= -f \| -ji \| -jf \| -n
CONDICIONEQUIPO ::= pr_LOCAL \| pr_VISITANTE | pr_TOTAL
CONDICIONTOP ::= pr_SUPERIOR \| pr_INFERIOR