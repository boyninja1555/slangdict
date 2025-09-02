import os
import mysql.connector as sql
from jinja2 import Template

# Constants
ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT_DIR = os.path.join(ROOT_DIR, "words")
NAV_PATH = os.path.join(ROOT_DIR, "templates", "nav.html")
TEMPLATE_PATH = os.path.join(ROOT_DIR, "templates", "word.html")

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

# All word details fetcher
cursor.execute("SELECT word, description, synonyms, antonyms FROM words")
template = Template(open(TEMPLATE_PATH).read())

# Output setup
if os.path.exists(OUT_DIR):
    for f in os.listdir(OUT_DIR):
        os.remove(os.path.join(OUT_DIR, f))

    os.removedirs(OUT_DIR)

os.makedirs(OUT_DIR, exist_ok=True)


# Page creation
def prefix_word(word: str) -> str:
    word_clean = word.strip()
    return (
        f'<a href="/words/{word_clean}.html">{word_clean}</a>'
        if word_clean.lower() in all_words
        else f'<a href="https://www.merriam-webster.com/dictionary/{word_clean}">{word_clean}</a>'
    )


for row in cursor.fetchall():
    synonyms = (
        [prefix_word(s) for s in row["synonyms"].split("\n")] if row["synonyms"] else []
    )
    antonyms = (
        [prefix_word(a) for a in row["antonyms"].split("\n")] if row["antonyms"] else []
    )

    html = template.render(
        nav=open(NAV_PATH, "r", encoding="utf-8").read(),
        word=row["word"].capitalize(),
        description=row["description"],
        synonyms=", ".join(synonyms),
        antonyms=", ".join(antonyms),
    )

    with open(os.path.join(OUT_DIR, f"{row['word']}.html"), "w", encoding="utf-8") as f:
        f.write(html)
