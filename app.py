from flask import Flask, request
app = Flask(__name__)
#SECURITY MISCONFIGURATION DEMO
#Debug Mode Enabled in Production
#Fake Database Password

DB_PASSWORD = "SuperSecretPassword123"

@app.route("/")
def home():
    return f"""
    <h1>Bank Application</h1>
    <p>Try opening:</p>
    <a href ='/transfer>/transfer</a>
    """
@app.route("/transfer")
def transfer():
    #DELIVERABLE ERROR
    amount = int(request.args.get("amount"))
    return f"Transferred $(amount)"

#VULNERABILITY: DEBUG MODE ENABLED

app.run(debug=True)
