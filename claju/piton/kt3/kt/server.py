from flask import Flask, request, jsonify
import sqlite3
import string
import random
import os

app = Flask(__name__)
DATABASE = 'url_shortener.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                short_url TEXT UNIQUE,
                normal_url TEXT UNIQUE
            )
        ''')
        conn.commit()

def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/short-url/<short_url>', methods=['GET'])
def get_normal_url(short_url):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT normal_url FROM urls WHERE short_url = ?', (short_url,))
        result = cursor.fetchone()
    
    if result:
        return jsonify({'normal_url': result[0]}), 200
    return jsonify({'error': 'Not found'}), 404

@app.route('/normal-url', methods=['POST'])
def create_short_url():
    data = request.get_json()
    if not data or 'normal_url' not in data:
        return jsonify({'error': 'Bad request'}), 400
    
    normal_url = data['normal_url']
    short_url = generate_short_url()
    
    with sqlite3.connect(DATABASE) as conn:
        try:
            conn.execute('INSERT INTO urls (short_url, normal_url) VALUES (?, ?)', 
                        (short_url, normal_url))
            conn.commit()
            return jsonify({'short_url': short_url}), 201
        except sqlite3.IntegrityError:
            # Если URL уже существует, вернем существующий короткий URL
            cursor = conn.cursor()
            cursor.execute('SELECT short_url FROM urls WHERE normal_url = ?', (normal_url,))
            result = cursor.fetchone()
            return jsonify({'short_url': result[0]}), 200

@app.route('/short-url/<short_url>', methods=['PUT'])
def update_url(short_url):
    data = request.get_json()
    if not data or 'normal_url' not in data:
        return jsonify({'error': 'Bad request'}), 400
    
    new_normal_url = data['normal_url']
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE urls SET normal_url = ? WHERE short_url = ?', 
                      (new_normal_url, short_url))
        conn.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Not found'}), 404
        return jsonify({'message': 'Updated successfully'}), 200

@app.route('/short-url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM urls WHERE short_url = ?', (short_url,))
        conn.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Not found'}), 404
        return jsonify({'message': 'Deleted successfully'}), 200

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)