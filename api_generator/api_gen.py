import os
import inflection

import gen

current_dir_path = os.path.dirname(os.path.abspath(__file__))

api_name_plural = input('API name com acento e plural: ')
api_name_singular = input('API name com acento e singular: ')
masculino = input('A palavra eh masculina? ')

if masculino[0] == 'n' or masculino == 'f':
    masc = False
else:
    masc = True

api_name_plural = api_name_plural.replace(" ","_")
api_name_singular = api_name_singular.replace(" ","_")
print (api_name_plural, api_name_singular)
dir_name = inflection.dasherize(inflection.transliterate(api_name_plural)), #contas-cartao
abs_api_path = str(current_dir_path) + '/' + str(dir_name)

if masc is True:
    new = 'novo'
    one = 'um'
    the = 'o'
else:
    new = 'nova'
    one = 'uma'
    the = 'a'

api_dict = dict(

    new = new,
    one = one,
    the = the,

    url_name_singular = inflection.dasherize(inflection.transliterate(api_name_singular)), #contas-cartao
    url_name = inflection.dasherize(inflection.transliterate(api_name_plural)), #contas-cartao
    route_name = inflection.dasherize(inflection.transliterate(api_name_singular)), #conta-cartao
    db_name = 'db' + inflection.camelize(inflection.transliterate(api_name_plural)).replace(" ",""), #dbContasCartao
    collection_name = inflection.camelize(inflection.transliterate(api_name_plural),False).replace(" ",""), #contasCartao
    return_name = inflection.camelize(inflection.transliterate(api_name_singular),False).replace(" ",""), #contaCartao
    singular_uppercase = inflection.camelize(inflection.transliterate(api_name_singular)).replace(" ",""), #ContaCartao #novaContaCartao
    description_plural = api_name_plural.replace("_", " "), #contas cartão
    description_singular = api_name_singular.replace("_", " "), #conta cartão

)

print("Creating api directory...")

if not os.path.exists(abs_api_path):
  os.makedirs(abs_api_path)

print("Creating api's files...")

funcs = ['atualizar', 'cadastrar', 'consultar', 'recuperar', 'remover', 'index']

for i in funcs:
  eval("gen.escreve_codigo_{}(api_dict, abs_api_path)".format(i))

print("Files created at {}".format(abs_api_path))
