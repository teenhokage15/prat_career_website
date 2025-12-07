from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangalore, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Hyderabad, India',
        'salary': 'Rs. 9,00,000'
    }
]
@app.route("/")
def hello_jovian():
    return render_template("home.html", 
                           jobs = JOBS,
                           company_name="Prat Careers")    

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host = '0.0.0.0', debug = True)

