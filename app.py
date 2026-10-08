from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    result_class = ""

    if request.method == "POST":
        age = int(request.form["age"])

        if age < 18:
            result = "WALA KANG BITAW"
            result_class = "underage"
        else:
            result = "PWEDENG-PWEDE KA"
            result_class = "adult"

    return render_template(
        "index.html",
        result=result,
        result_class=result_class
    )

if __name__ == "__main__":
    app.run(debug=True)