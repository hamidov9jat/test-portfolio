from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():  # put application's code here
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def grab_form_data():
    if request.method == 'POST':
        try:
            # data = request.form['email']
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            raise Exception('Did not save to database!')
    else:
        raise Exception('Something Went Wrong. Please try again!')


def write_to_file(data):
    with open('database.txt', 'a') as file:
        name = data.get('name')
        email = data.get('email')
        message = repr(data.get('message'))
        file.write(f'\n{name}, {email}, {message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as file:
        name = data.get('name')
        email = data.get('email')
        message = repr(data.get('message'))
        csv_writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


if __name__ == '__main__':
    app.run()
