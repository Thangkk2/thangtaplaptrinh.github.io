from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Tạo một đối tượng dictionary để lưu trữ thông tin người dùng (chỉ để mô phỏng, không nên lưu trữ mật khẩu người dùng theo cách này trong môi trường thực tế)
users = {'user1': 'password1', 'user2': 'password2'}

# Route cho trang chủ
@app.route('/')
def index():
    if 'username' in session:
        return 'Bạn đã đăng nhập với tên đăng nhập {}'.format(session['username'])

    return 'Bạn chưa đăng nhập'

# Route cho trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại.'
    return render_template('login.html')

# Route cho trang đăng xuất
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
