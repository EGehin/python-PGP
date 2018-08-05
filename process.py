#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import os, gnupg

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

def encrypt(key, src):
    home = os.path.join(os.getcwd(), "gnupg")
    gpg = gnupg.GPG(gnupghome=home,)
    keys = gpg.import_keys(key)
    print keys.fingerprints
    result = gpg.encrypt(src, keys.fingerprints[0], always_trust=True)
    return str(result)
    if not result:
         raise RuntimeError(result.status)  


@app.route('/process', methods=['POST'])
def process():


    message = request.form['message']

    print len(message)
    
    pgp = request.form['pgp']

    print pgp

    if message and pgp:
        encrypt(pgp, message)

        newMessage = encrypt(pgp, message)


        print newMessage

        return jsonify({'message1' : newMessage})

    return jsonify({'error' : 'Missing data!'})


if __name__ == '__main__':
    app.run(debug=True)

