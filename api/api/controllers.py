from . import app


@app.route('/health')
def health():
    return 'OK', 200
