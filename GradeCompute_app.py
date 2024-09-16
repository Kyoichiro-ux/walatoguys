from flask import Flask, request, render_template_string

app = Flask(__name__)

def GradeCompute_app(prelim, midterm, final):
    try:
        prelim, midterm, final = float(prelim), float(midterm), float(final)
        avg = prelim * 0.3 + midterm * 0.3 + final * 0.4
        return (f"Congratulations! You Passed The Exam and got an Average of {avg:.2f}."
                if avg >= 75
                else f"Sorry Bro! Bawi ka nalang next life you got {avg:.2f}. You need 75 to pass.")
    except ValueError:
        return "Invalid input. Please enter numeric values."

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Grade Calculator</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Cinzel', serif;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #f0f0f0; 
        }
        .card {
            background: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
            width: 360px;
            text-align: center;
        }
        h2 {
            color: #4CAF50; 
            margin-bottom: 20px;
            font-size: 28px;
            font-weight: 700;
        }
        .input-group {
            margin-bottom: 15px;
            text-align: left;
        }
        label {
            color: #ddd;
            display: block;
            margin-bottom: 5px;
            font-size: 14px;
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #666;
            background-color: #333;
            color: #f0f0f0;
            font-size: 16px;
        }
        input[type="text"] {
            margin-bottom: 10px;
        }
        input[type="submit"] {
            border: none;
            background: linear-gradient(to right, #4CAF50, #81C784);
            color: #fff;
            cursor: pointer;
            margin-top: 20px;
            font-weight: bold;
        }
        input[type="submit"]:hover {
            background: linear-gradient(to right, #388E3C, #66BB6A);
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background: rgba(0, 0, 0, 0.8);
            border-radius: 6px;
            color: #4CAF50;
            font-weight: bold;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Grade Calculator</h2>
        <form method="post">
            <div class="input-group">
                <label for="prelim">Prelim Grade</label>
                <input type="text" id="prelim" name="prelim" required>
            </div>
            <div class="input-group">
                <label for="midterm">Midterm Grade</label>
                <input type="text" id="midterm" name="midterm" required>
            </div>
            <div class="input-group">
                <label for="final">Final Grade</label>
                <input type="text" id="final" name="final" required>
            </div>
            <input type="submit" value="Calculate">
        </form>
        <div class="result">{{ result }}</div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        result = GradeCompute_app(request.form['prelim'], request.form['midterm'], request.form['final'])
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
