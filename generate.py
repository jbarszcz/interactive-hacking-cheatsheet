import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.html')

with open('data.json') as json_file:
    data = json.load(json_file)

rendered_template = template.render(data=data)

with open("index.html", "w") as file:
    file.write(rendered_template)
