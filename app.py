from flask import Flask, render_template_string
app = Flask(__name__)
patients = [
    {"id": 1, "name": "John Dose", "age": 45, "disease": "Flu", "admission_date": "2024-11-01"},
    {"id": 2, "name": "Jane Smith", "age": 30, "disease": "Covid", "admission_date": "2024-11-05"},
    {"id": 3, "name": "Emma Brown", "age": 60, "disease": "dengue", "admission_date": "2024-11-10"}
]

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hospital Management System</title>
        <style>
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
                background-color: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Hospital Management System</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Disease</th>
                    <th>Admission Date</th>
                </tr>
            </thead>
            <tbody>
                {% for patient in patients %}
                <tr>
                    <td>{{ patient.id }}</td>
                    <td>{{ patient.name }}</td>
                    <td>{{ patient.age }}</td>
                    <td>{{ patient.disease }}</td>
                    <td>{{ patient.admission_date }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    return render_template_string(html_content, patients=patients)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug= True)
