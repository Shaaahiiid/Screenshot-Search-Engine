from flask import Flask, render_template, request
from search import search_screenshots

app = Flask(__name__)
    
@app.route('/', methods=["GET","POST"])
def index():
    results = None
    
    if request.method == "POST":
        query = request.form.get("query")
        results = search_screenshots(query)
        
    return render_template("index.html", results = results)

if __name__ == "__main__":
    app.run(debug=True)