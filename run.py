from flask import Flask,render_template,request,redirect,url_for
from datetime import datetime, date

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save_data', methods=['GET'])
def save_data():
    employee_id = int(request.args.get("employee id", 0))
    employee_name = request.args.get("employee name", "")
    department = request.args.get("department", "")
    position = request.args.get("position", "")
    email = request.args.get("email", "")
    salary = int(request.args.get("salary", 0))
    joining_date = request.args.get("joining date", "")
    
    print(employee_id, employee_name, department, position, email, salary, joining_date)

    return redirect(url_for('home'))

app.run()