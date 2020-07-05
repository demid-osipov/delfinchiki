from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return gcd(y, x%y)

@app.route('/send', methods = ['POST'])
def send():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        return render_template('app.html',gcd = gcd(num1, num2))
    else:
        return render_template('app.html')


if __name__ == '__main__':
    app.run()
