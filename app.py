from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Sarah McGloin. This is my first code change!'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():  # put application's code here
    return render_template('about-css.html')

@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')

    print('Subject entered: ' + request.args.get('subject'))
    print('Course number entered' + request.args.get('course_number'))
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():  # put application's code here
    if request.method == 'POST':
        return render_template('contact.html', form_submitted = True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
