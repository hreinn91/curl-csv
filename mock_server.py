from flask import Flask, jsonify, request, make_response
import flask_excel as excel
app = Flask(__name__)
data = [
    ["REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"],
    ["1985/01/21","Douglas Adams",'0345391802',5.95],
    ["1990/01/12","Douglas Hofstadter",'0465026567',9.95],
    ["1998/07/15","Timothy \"The Parser\" Campbell",'0968411304',18.99],
    ["1999/12/03","Richard Friedman",'0060630353',5.95],
    ["2004/10/04","Randel Helms",'0879755725',4.50]
]

@app.route('/generate2', methods=['GET'])
def generate2():
    output = excel.make_response_from_array(data, 'csv')
    output.headers["Content-type"] = "text/csv"
    return output


@app.route('/generate')
def generate():
    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
"1985/01/21","Douglas Adams",0345391802,5.95
"1990/01/12","Douglas Hofstadter",0465026567,9.95
"1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
"1999/12/03","Richard Friedman",0060630353,5.95
"2004/10/04","Randel Helms",0879755725,4.50"""
    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response


@app.route('/greet')
def greet():
    return 'Hello',200

if __name__ == "__main__":
    app.debug=True
    app.run()
