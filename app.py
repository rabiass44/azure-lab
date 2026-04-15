from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    
    return "<h1>Rabia Yaşa - 221002064</h1><p>Azure ve GitHub Actions ile Otomatik Dağıtım Başarılı!</p>"

if __name__ == '__main__':
    app.run()

