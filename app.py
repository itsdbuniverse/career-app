from typing import Required
from flask import Flask,request, render_template, jsonify
from db_conn import add_data_to_db, query_runner
from db_conn import bring_data
from api_fetch import api_fetch
import requests
app = Flask(__name__)

# JOBS = [{
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 10,00,000'
# }, {
#     'id': 2,
#     'title': 'Data Scientist',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 15,00,000'
# }, {
#     'id': 3,
#     'title': 'Frontend Engineer',
#     'location': 'Remote'
# }, {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$120,000'
# }]

# html routing

app = Flask(__name__)

@app.route("/")
def hello():
    responses = query_runner(query="select * from jobs")
    data = []
    for response in responses:
        id, title, location, salary, currency, responsibilites, requirements = response
        data.append({
            'id': id,
            'title': title,
            'location': location,
            'salary': salary,
            'currency': currency,
            'responsibilites': responsibilites,
            'requirements': requirements,
            'url':f"https://3dce0f53-d44b-4a00-9e9f-1bf445d50f11-00-qs9f2kiivs06.sisko.replit.dev/api/jobs?id={id}"
        })
    return render_template("home.html", jobs=data, company_name="WIPRO")



    

# json routing through api
# @app.route("/api/jobs")
# def list_jobs():
#     responses = query_runner(query="select * from jobs")
#     data = []
#     for response in responses:
#         id, title, location, salary, currency, responsibilities, requirements = response
#         data.append({
#             'id': id,
#             'title': title,
#             'location': location,
#             'salary': salary,
#             'currency': currency,
#             'responsibilities': responsibilities,
#             'requirements': requirements
#         })
    
#     return jsonify(data)
    
# dynamic data for apply
@app.route("/api/jobs")
def show_job():
    
    id=str(request.args.get('id')).strip()
    if id is not None or id!='' or id != ' ':
        query = f"SELECT * FROM jobs WHERE id = {id}"
    else:
        query = "SELECT * FROM jobs"
    responses = bring_data(query)
    if responses is None:
        return jsonify({"error": "Data retrieval failed"}), 500

    data = []
    for response in responses:
        id, title, location, salary, currency, responsibilites, requirements = response
        data.append({
            'id': id,
            'title': title,
            'location': location,
            'salary': salary,
            'currency': currency,
            'responsibilites': responsibilites,
            'requirements': requirements
        })
    if not data:
        return "Not Found", 404
    # return jsonify(data)
    return render_template("jobpage.html", job=data[0])

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    id=str(request.args.get('id')).strip()
    data = request.form
    add_data_to_db(job_id=data.get('job_id'), full_name=data.get('full_name'), email=data.get('email'), linkedin_url=data.get('linkedin_url'), education=data.get('education'), work_experience=data.get('work_experience'), resume_url=
                  data.get('resume_url'))
    
    return render_template('application_submit.html',
                          application=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
