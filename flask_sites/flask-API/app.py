from flask import Flask, request

app = Flask(__name__)


# for example: localhost/API?arg1=10&arg2=3&action=mul
@app.route('/API')
def calc():
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    action = request.args.get('action')

    if action == 'add':
        result = arg1 + arg2
    elif action == 'sub':
        result = arg1 - arg2
    elif action == 'mul':
        result = arg1 * arg2
    elif action == 'dev':
        if arg2 == 0:
            return 'None'
        result = arg1 / arg2
    else:
        return 'None'
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)
