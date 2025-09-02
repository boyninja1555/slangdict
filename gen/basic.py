import os
from jinja2 import Template

# Constants
ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT_PATH = os.path.join(ROOT_DIR, "{%}.html")
NAV_PATH = os.path.join(ROOT_DIR, "templates", "nav.html")
TEMPLATE_PATH = os.path.join(ROOT_DIR, "templates", "{%}.html")


# Output setup
def build(template_name: str):
    out_path = OUT_PATH.replace("{%}", template_name if template_name != "home" else "index")
    basic_template_path = TEMPLATE_PATH.replace("{%}", "basic")
    template_path = TEMPLATE_PATH.replace("{%}", template_name)

    if os.path.exists(out_path):
        os.remove(out_path)

    basic_template = Template(open(basic_template_path).read())
    template = Template(open(template_path).read())

    # Page creation
    html = basic_template.render(
        title="Unknown",
        nav=open(NAV_PATH, "r", encoding="utf-8").read(),
        content=template.render(),
    )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
