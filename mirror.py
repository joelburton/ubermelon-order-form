"""Trivial Flask server to respond to an order form.

Used for teaching students to make HTML forms.
"""

import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/process', methods=['GET', 'POST'])
def mirror():
    """Respond to form with letter & debug info on request."""

    # request.values is a combination of both the form-data and url-data,
    # so it works for both GET and POST requests
    r = request.values

    return render_template(
        'mirror.html',
        firstname=r.get('firstname'),
        lastname=r.get('lastname'),
        quantity=r.get('quantity'),
        melontype=r.get('melontype'),
        time=r.get('time'),
        returning=r.get('returning'),
        stats=r.get('stats'),
        method=request.method,
        data=r,
    )

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)),
            host='0.0.0.0')
