import os
import json
import mysql.connector as sql
from jinja2 import Template

# Constants
ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT_PATH = os.path.join(ROOT_DIR, "search.html")
NAV_PATH = os.path.join(ROOT_DIR, "templates", "nav.html")
TEMPLATE_PATH = os.path.join(ROOT_DIR, "templates", "search.html")

# Database connection
conn = sql.connect(
    host=input("What is the database host? "),
    user=input("What is the database user? "),
    password=input("What is the database password? "),
    database=input("What is the database name? "),
)
cursor = conn.cursor(dictionary=True)

# All words fetcher
cursor.execute("SELECT word from words")
all_words = {row["word"].lower() for row in cursor.fetchall()}
template = Template(open(TEMPLATE_PATH).read())

# Output setup
if os.path.exists(OUT_PATH):
    os.remove(OUT_PATH)

html = template.render(
    nav=open(NAV_PATH, "r", encoding="utf-8").read(),
    results=json.dumps(sorted(all_words)),
)

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(html)
