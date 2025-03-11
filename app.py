from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get top output (only the first 10 lines)
    try:
        top_output = subprocess.check_output("top -bn1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = str(e)

    return f"""
    <h1>HTOP Endpoint</h1>
    <p><strong>Name:</strong> Your Full Name</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)