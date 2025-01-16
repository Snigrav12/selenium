from flask import Flask, jsonify, render_template
import scraper

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["GET"])
def scrape():
    result = scraper.scrape_twitter()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
