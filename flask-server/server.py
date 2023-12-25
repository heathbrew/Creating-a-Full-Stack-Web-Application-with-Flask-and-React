from flask import Flask , redirect

app = Flask(__name__)

# Members API Route

@app.route("/")
def home():
    return redirect("/members")

@app.route("/members")
def members():
    return {"members" : ["Members1", "Members2","Members3"]}

if __name__ == "__main__":
    app.run(debug=True , host = "0.0.0.0" , port = 5000)