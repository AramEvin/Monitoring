from jinja2 import Environment, FileSystemLoader
from dotenv import dotenv_values

env = Environment(loader=FileSystemLoader('prometheus'))
template = env.get_template('prometheus.yml.j2')

config = dotenv_values('.env')
rendered = template.render(**config)

with open('prometheus/prometheus.yml', 'w') as f:
    f.write(rendered)
