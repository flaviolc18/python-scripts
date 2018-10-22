from string import Template

def write_template(crud_name, api_dict, path_to_save):
  array_of_lines = []
  template = open('./templates/'+crud_name, 'r')
  for line in template:
    t = Template(line)
    array_of_lines.append(t.substitute(api_dict))
  f = open("{}/{}-{}.js".format(path_to_save, crud_name, api_dict['route_name']), 'w')
  f.write("".join(array_of_lines))

def write_template(api_dict, path_to_save):
  crud_operation('atualizar', api_dict, path_to_save)

def write_template(api_dict, path_to_save):
  crud_operation('cadastrar', api_dict, path_to_save)

def write_template(api_dict, path_to_save):
  crud_operation('consultar', api_dict, path_to_save)

def write_template(api_dict, path_to_save):
  crud_operation('recuperar', api_dict, path_to_save)

def write_template(api_dict, path_to_save):
  crud_operation('remover', api_dict, path_to_save)

def write_template(api_dict, path_to_save):
  crud_operation('index', api_dict, path_to_save)
