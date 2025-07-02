from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'soso25'

# Página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == 'soso25':
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return "Senha incorreta. <a href='/login'>Tente novamente</a>"
    return render_template('login.html')

# Página de perfil
@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', user=session['username'])
    return redirect(url_for('home'))

# Página de logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')

# Página de produtos
@app.route('/produtos')
def produtos():
    produtos = ["Maçã", "Banana", "Laranja"]
    logado = 'username' in session
    return render_template("produtos.html", produtos=produtos, logado=logado)

if __name__ == '__main__':
    app.run(debug=True)
