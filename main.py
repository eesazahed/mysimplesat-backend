from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = 'question_bank.db'


@app.route('/get-questions', methods=['GET'])
def get_questions():
    section = request.args.get('subject')
    difficulty = request.args.get('difficulty')
    limit = int(request.args.get('limit', 20))

    query = "SELECT * FROM questions WHERE 1=1"
    params = []

    if section:
        query += " AND subject = ?"
        params.append(section)
    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)

    query += " ORDER BY RANDOM() LIMIT ?"
    params.append(limit)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()

    result = [dict(row) for row in rows]
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
