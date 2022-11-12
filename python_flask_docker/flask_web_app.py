import os
import subprocess

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# connect the environment variable from the dockerfile
SECRET_KEY = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)


@app.route('/', methods=['POST', 'GET'])
def home():
    if SECRET_KEY:
        return "I am running from a Docker container"
    command = 'docker ps --format "table {{.ID}}\t\t{{.Image}}\t\t{{.CreatedAt}}"'
    running_containers = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return render_template('index.html', value=running_containers)


if __name__ == "__main__":
    print("Go to -> http://localhost:5000")
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)