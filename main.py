
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def route1():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        # Perform data processing here
        processed_data = input1 + ' ' + input2
        response = jsonify({'result': processed_data})
        return response
    return '''
        <form method="POST">
            <input type="text" name="input1" placeholder="Input 1">
            <input type="text" name="input2" placeholder="Input 2">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run()
