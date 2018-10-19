from string import Template

def escreve_codigo_atualizar(api_dict, path_to_save):
  array_of_lines = []
  template = open('./templates/atualizar', 'r')
  for line in template:
    t = Template(line)
    array_of_lines.append(t.substitute(api_dict))
  f = open("{}/atualizar-{}.js".format(path_to_save, api_dict['api_singular_kebabcase']), 'w')
  f.write("".join(array_of_lines))

def escreve_codigo_cadastrar(api_dict, path_to_save):
  array_of_lines = []
  template = open('./templates/cadastrar', 'r')
  for line in template:
    t = Template(line)
    array_of_lines.append(t.substitute(api_dict))
  f = open("{}/cadastrar-{}.js".format(path_to_save, api_dict['api_singular_kebabcase']), 'w')
  f.write("".join(array_of_lines))

def escreve_codigo_consultar(api_dict, path_to_save):
  array_of_lines = []
  template = open('./templates/consultar', 'r')
  for line in template:
    t = Template(line)
    array_of_lines.append(t.substitute(api_dict))
  f = open("{}/consultar-{}.js".format(path_to_save, api_dict['api_singular_kebabcase']), 'w')
  f.write("".join(array_of_lines))

def escreve_codigo_recuperar(api_dict, path_to_save):
  array_of_lines = []
  template = open('./templates/recuperar', 'r')
  for line in template:
    t = Template(line)
    array_of_lines.append(t.substitute(api_dict))
  f = open("{}/recuperar-{}.js".format(path_to_save, api_dict['api_singular_kebabcase']), 'w')
  f.write("".join(array_of_lines))

def escreve_codigo_remover(api_dict, path_to_save):
  array_of_lines = []
  template = open('./templates/remover', 'r')
  for line in template:
    t = Template(line)
    array_of_lines.append(t.substitute(api_dict))
  f = open("{}/remover-{}.js".format(path_to_save, api_dict['api_singular_kebabcase']), 'w')
  f.write("".join(array_of_lines))