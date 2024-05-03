a = input("Digite qualquer coisa: ")

print(a,',', type(a))

print("O valor informado é um número? ", a.isnumeric())

print("O valor informado é composto apenas por letras? ", a.isalpha())

print("O valor informado é alfanumérico ? ", a.isalnum())

print("O valor informado contém apenas letras maiúsculas? ", a.isupper())

print("O valor informado contém apenas letras minúsculas? ", a.islower())

print("O valor informado esta entre o valor 0 e 127 da tabela ASCII? ", a.isascii())

print("O valor informado contém apenas digitos decimais? ", a.isdecimal())

print("O valor informado contém apenas dígitos?(Números de 0 a 9) ", a.isdigit())

print("O valor informado é um identificador válido em python? ", a.isidentifier())

print("Todos os caracteres do valor informado são imprimíveis? ", a.isprintable())

print("Valor informado é um espaço em branco? ", a.isspace())

print("Valor informado tem formato de título?(primeira letra maiúscula e o restante minúscula) ", a.istitle())
