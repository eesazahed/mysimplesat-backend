import json
import sqlite3

with open('sat_question_bank.json', 'r') as f:
    questions = json.load(f)

conn = sqlite3.connect('question_bank.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS questions')

cur.execute("""
CREATE TABLE questions (
    id TEXT PRIMARY KEY,
    subject TEXT,
    difficulty TEXT,
    question_text TEXT,
    choices TEXT,
    correct_choice TEXT,
    rationale TEXT
)
""")

for q in questions:
    cur.execute("""
    INSERT INTO questions (id, subject, difficulty, question_text, choices, correct_choice, rationale)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        q['id'],
        q['subject'],
        q['difficulty'],
        q['question_text'],
        json.dumps(q['choices']),
        q['correct_choice'],
        q['rationale']
    ))

conn.commit()
conn.close()
