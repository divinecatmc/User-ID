import csv
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def readfunction():

    if request.method == "POST":

        id = request.form['user_id']
        name = ""
        yes = 0
        with open("employee.csv","r") as csv_file:
            
            csv_reader = csv.reader(csv_file,delimiter=",")

            for line in csv_reader:

                if line[0] == id:

                    print(line[1])
                    name = line[1]
                    yes += 1
            
            if yes == 0:
                name = "This Prolific ID is not in our records. Please check and enter again. If you continue to encounter the same problem, you can email Dr. Selin Kudret at s.kudret@henley.ac.uk"
                csv_file.close()
                return render_template("index.html", name=name)
            
            else:

                csv_file.close()
                return render_template("index.html", name=name)

    
    else:

        return render_template("index.html")
