import os
import inflection

import gen

current_dir_path = os.path.dirname(os.path.abspath(__file__))
api_dir_path = input('Path to the new api: ')
api_name = input('Name to the new api (use space to separate the words): ')
abs_api_path = "{}/{}/{}".format(current_dir_path, api_dir_path, api_name)
api_name_words = api_name.split(" ")
api_name_underscore = api_name.replace(" ", "_")
api_name_underscore_plural = "_".join([inflection.pluralize(api_name_words[0])]+api_name_words[1:])
api_dict = dict(
api_name = api_name,
api_name_underscore = api_name_underscore,
api_singular_camelcase = inflection.camelize(api_name_underscore, False),
api_singular_camelcase_true = inflection.camelize(api_name_underscore),
api_plural_camelcase_true = inflection.camelize(api_name_underscore_plural),
api_plural_camelcase = inflection.camelize(api_name_underscore_plural, False),
api_singular_kebabcase = inflection.dasherize(api_name_underscore),
api_plural_kebabcase = inflection.dasherize(api_name_underscore_plural)
)

print("Creating api directory...")

if not os.path.exists(abs_api_path):
  os.makedirs(abs_api_path)

print("Creating api's files...")

funcs = ['atualizar', 'cadastrar', 'consultar', 'recuperar', 'remover', 'index']

for i in funcs:
  eval("gen.escreve_codigo_{}(api_dict, abs_api_path)".format(i))

print("Files created at {}".format(abs_api_path))