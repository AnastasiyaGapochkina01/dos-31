from flask import Flask
import time
import threading

app = Flask(__name__)

# Глобальные флаги для симуляции состояний
ready = False
alive = True
startup_complete = False

@app.route('/readyz')
def readyz():
    global ready
    if not startup_complete:
        return 'Not ready: startup', 503
    return 'OK' if ready else 'Not ready', 503

@app.route('/livez')
def livez():
    global alive
    return 'OK' if alive else 'Dead', 503

@app.route('/')
def hello():
    return f'Hello from Pod! Ready: {ready}, Alive: {alive}'

@app.route('/toggle-ready')
def toggle_ready():
    global ready
    ready = not ready
    return f'Ready toggled to {ready}'

@app.route('/kill-alive')
def kill_alive():
    global alive
    alive = False
    return 'Alive killed - liveness probe should fail'

if __name__ == '__main__':
    # Симуляция startup: 20 секунд
    time.sleep(20)
    startup_complete = True

    # Симуляция readiness: становится ready через 30с
    threading.Timer(30.0, lambda: globals().update(ready=True)).start()

    app.run(host='0.0.0.0', port=8080, debug=False)
