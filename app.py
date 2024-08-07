from typing import Required
from flask import Flask, render_template, jsonify
from db_conn import query_runner
# from api_fetch import api_fetch
app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}]

# html routing
@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, company_name="WIPRO")
    

# json routing through api
@app.route("/api/jobs")
def list_jobs():
    responses = query_runner(query="select * from jobs")
    data = []
    for response in responses:
        id, title, location, salary, currency, responsibilities, requirements = response
        data.append({
            'id': id,
            'title': title,
            'location': location,
            'salary': salary,
            'currency': currency,
            'responsibilities': responsibilities,
            'requirements': requirements
        })

    return jsonify(data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
