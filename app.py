from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reports = [
    {"id": 1, "name": "Sanjana Shetty", "age": 10 ,"diagnosis": "Autism Spectrum Disorder", "notes": "Needs speech therapy."},
    {"id": 2, "name": "Kashish Tiwari", "age": 8, "diagnosis": "Autism Spectrum Disorder", "notes": "Improving social skills."}
]

@app.route('/')
def index():
    return render_template('index.html', reports=reports, page="home")

@app.route('/manage_reports')
def manage_reports():
    return render_template('index.html', reports=reports, page="manage_reports")

@app.route('/add', methods=['GET', 'POST'])
def add_report():
    if request.method == 'POST':
        data = request.form
        new_report = {
            "id": reports[-1]["id"] + 1 if reports else 1,
            "name": data.get("name"),
            "age": int(data.get("age")),
            "diagnosis": data.get("diagnosis"),
            "notes": data.get("notes")
        }
        reports.append(new_report)
        return redirect(url_for('manage_reports'))

    return render_template('add_report.html')

@app.route('/update/<int:report_id>', methods=['GET', 'POST'])
def update_report(report_id):
    report = next((r for r in reports if r["id"] == report_id), None)
    if not report:
        return "Report not found", 404

    if request.method == 'POST':
        data = request.form
        report.update({
            "name": data.get("name", report["name"]),
            "age": int(data.get("age", report["age"])),
            "diagnosis": data.get("diagnosis", report["diagnosis"]),
            "notes": data.get("notes", report["notes"])
        })
        return redirect(url_for('manage_reports'))

    return render_template('update_report.html', report=report)

@app.route('/delete/<int:report_id>', methods=['GET', 'POST'])
def delete_report(report_id):
    global reports
    reports = [report for report in reports if report["id"] != report_id]
    return redirect(url_for('manage_reports'))

if __name__ == "__main__":
    app.run()

