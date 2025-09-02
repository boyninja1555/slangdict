@echo off

echo "[.] Building home page..."
python home.py
echo "[/] Built home page!"

echo "[.] Building about page..."
python about.py
echo "[/] Built about page!"

echo "[.] Building word pages..."
python words.py
echo "[/] Built word pages!"

echo "[.] Building word not found page..."
python word-not-found.py
echo "[/] Built word not found page!"

echo "[.] Building search page..."
python search.py
echo "[/] Built search page!"