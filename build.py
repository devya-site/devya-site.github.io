import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

SRC_DIR = Path('src')
PUBLISH_DIR = Path('docs')
TEMPLATES_DIR = SRC_DIR / '_includes'


shutil.copytree(SRC_DIR / 'assets', PUBLISH_DIR / 'assets', dirs_exist_ok=True)

env = Environment(loader=FileSystemLoader([str(SRC_DIR), str(TEMPLATES_DIR)]), autoescape=select_autoescape(['html']))
for filename in SRC_DIR.glob('*.html'):
    template = env.get_template(filename.name)
    output_file = PUBLISH_DIR / filename.name
    with open(output_file, 'w') as f:
        f.write(template.render())
        print("Generated file: ", output_file)

