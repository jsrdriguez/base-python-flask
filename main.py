import os
from app import create_app
from config import config

env = config['local']

app = create_app(env)

@app.route('/')
def main():
    return 'API'

port = int(os.getenv('PORT', 5000))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port, debug=True)