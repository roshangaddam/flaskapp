
from FlaskWebProject1.app import app
from datetime import datetime 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080

    app.run(host=HOST, port=PORT)
