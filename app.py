from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello RAJ from AWS EKS DevOps Learning. Thanks for building this Docker Image!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)