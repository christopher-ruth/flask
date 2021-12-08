from flask import Flask, render_template, request, redirect
from database import mydb, mycursor
# from wtforms.validators import input 

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    msg=''
    if request.method=='POST':
        _hidden= request.form['boy']
        if _hidden == 'reg':
            _hospital_name = request.form['hospital']
            _email = request.form['email']
            _password = request.form['password1']
            _confirm_password = request.form['password2']
            if _password==_confirm_password:
                sql = 'INSERT INTO register (hospital_name, email, password, confirm_password) VALUES (%s, %s, %s,  %s)'
                val = (_hospital_name, _email, _password, _confirm_password)
                mycursor.execute(sql, val)
                mydb.commit()
                return redirect('/registeration')
            else:
                msg= 'Please confirm your password'
        if _hidden =='login':
            _emaillog= request.form['emaillog']
            _passwordlog = request.form['passwordlog']

            mycursor.execute(f'SELECT * FROM register WHERE email="{_emaillog}" AND password="{_passwordlog}"')
            ver= mycursor.fetchone()
            if ver: 
                return redirect('/registeration')
            else:
                msg='incorrect'

    return render_template('index.html',message=msg)

 

@app.route('/registeration', methods=['GET', 'POST'])
def registeration():
    msg=''
    if request.method == 'POST':
        _first_name = request.form['firstname']
        _last_name = request.form['lastname']
        _phone_number = request.form['phonenumber']
        _email = request.form['email']
        _blood_type = request.form['bloodtype']
        _genotype = request.form['genotype']

        mycursor.execute(f'SELECT * FROM registed_patient WHERE first_name="{_first_name}" AND last_name="{_last_name}" AND phone_number="{ _phone_number}" AND email="{_email}" AND Blood_type="{_blood_type}" AND genotype="{_genotype}"')
        find =mycursor.fetchone()
        if find:
            msg='already registered'
        else:
            sql = f'INSERT INTO registed_patient (first_name, last_name, phone_number, email, Blood_type, genotype) VALUES (%s, %s, %s, %s,  %s, %s)'
            val = (_first_name, _last_name, _phone_number, _email, _blood_type, _genotype)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect('/registeration')

    mycursor.execute('SELECT * FROM registed_patient')
    check= mycursor.fetchall()
    return render_template('registeration.html', check=check, msg=msg)





if __name__ == '__main__':
    app.run(debug=True)