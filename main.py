from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_profile_name(access_token):
    url = "https://graph.facebook.com/me"
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    profile_name = None
    error_message = None

    if request.method == 'POST':
        access_token = request.form['access_token']
        profile_name = get_profile_name(access_token)
        if profile_name is None:
            error_message = "Invalid access token. Please try again."

    return render_template('index.html', profile_name=profile_name, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
