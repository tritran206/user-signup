from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('user-signup.html')


@app.route('/validate', methods=['POST'])
def validate_user():
    username = request.form['username']
    pwd = request.form['pwd']
    verifypw = request.form['verifypw']
    email = request.form['useremail']

    username_error = ''
    pwd_error = ''
    vpwd_error = ''
    useremail_error = ''

################## Validating password
    if pwd == '':
        pwd_error = 'Please enter a valid password'

    elif ' ' in pwd:
        pwd_error = 'Password can not contain spaces'

    elif len(pwd) <= 3:
        pwd_error = 'Your password is not long enough'
        pwd = ''
        verifypw = ''

    elif len(pwd) > 20:
        pwd_error = 'Your password is too long'
        pwd = ''
        verifypw = ''

    elif pwd != verifypw:
        vpwd_error = 'Passwords did not match.'
        pwd = ''
        verifypw = ''

################## Validating username
    if username == '':
        username_error = 'Please enter a vaild username'
    elif len(username) <= 3:
        username_error = 'Your username is not long enough'
        username = ''

    elif len(username) > 20:
        username_error = 'Your username is too long'
        username = ''

    elif ' ' in username:
        username_error = 'Your username can not contain any spaces'
        username = ''

################## Validating email
    if email:
        if "@" not in email:
            useremail_error = 'Your email is invalid'
        if "." not in email:
            useremail_error = 'Your email is invalid'
        if " " in email:
            useremail_error = 'Your email is invalid'

    if not username_error and not pwd_error and not vpwd_error and not useremail_error:
        return render_template('confirmation.html', username = username)
    else:
        return render_template('user-signup.html', username_error=username_error, pwd_error=pwd_error, vpwd_error=vpwd_error, useremail_error=useremail_error, username=username, useremail= email )


if __name__ == '__main__':
    app.run()
