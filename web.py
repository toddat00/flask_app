from flask import Flask, render_template, request
app = Flask(__name__)
import os
import yelpapi

@app.route("/")
def index():
#allows the opportunity to enter information in the url link that will report,
#back into the output from the site.
    # name = request.values.get('name')
    # return render_template('index.html', name=name)
    location = request.values.get('location')
    terms = request.values.get('terms')
    if location and terms:
        businesses = yelpapi.get_businesses(location, terms)
    else:
        businesses = yelpapi.get_businesses("Boston, MA","Pizza")
    return render_template('index.html', businesses=businesses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
