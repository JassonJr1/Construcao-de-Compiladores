#Jasson Júnior
#Importação da biblioteca
import ply.lex as lex

# Definição dos tokens
tokens = (
    'NUMERO',
    'SOMA',
    'MENOS',
    'MULTIPLICACAO',
    'DIVICAO',
    'ABRE_PARENTESE',
    'FECHA_PARENTESE',
)

# Definição sas expressões regulares para cada token
t_SOMA = r'\+'
t_MENOS = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVICAO = r'/'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_NUMERO = r'\d+'

# Ignora espaços e tabulações
t_ignore = ' \t'

# Trata erros de lexema
def t_error(t):
    print("Caractere inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Cria o analisador léxico
lexer = lex.lex()

# Teste do analisador léxico com uma expressão
lexer.input('3 + 4 * 2 - 1 / 5')

# Imprime os tokens encontrados
for tok in lexer:
    print(tok)
