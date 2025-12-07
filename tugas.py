from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Tugas Paas Komputasi Awan!"

if __name__ == '__main__':
    app.run()
