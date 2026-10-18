from flask import Flask, render_template, request

myserver = Flask(__name__, template_folder="webpages")


#website routes

@myserver.route("/")
def home():
    return render_template("home.html")


@myserver.route("/about")
def about():
    return render_template("about.html")


@myserver.route("/projects")
def projects():
    return render_template("projects.html")


@myserver.route("/contact")
def contact():
    return render_template("contact.html")



# api/about
@myserver.route("/api/about", methods=["GET"])
def api_about():
    return {
        "name": "Eghogho",
        "headline": "Solutions Engineer | Early-Career Tech Professional | Exploring Technology & Software | Building Practical Skills & Projects",
        "project": "HTML & JSON Server"
    }


# api/projects
@myserver.route("/api/projects", methods=["GET"])
def api_projects():
    return {
        "projects": [
            "Smart Home System simulation",
            "Local Host Lens",
            "Domain Check Tool",
            "HTML & JSON Server"
        ]
    }


# api/contact
@myserver.route("/api/contact", methods=["GET", "POST"])
def api_contact():

    if request.method == "GET":
        return {
            "Email": "binitieeghogho@gmal.com",
            "LinkedIn": "www.linkedin.com/in/eghogho-binitie-647888260"
        }

    if not request.is_json:
        return {
            "error": "Please send data as JSON."
        }, 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {
            "error": "Please send a valid JSON object."
        }, 400

    return {
        "message": "Your data was received successfully!!!!.",
        "received": data
    }, 200


# 404 page
@myserver.errorhandler(404)
def page_not_found(error):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>404 - Page Not Found</title>
    </head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The route you requested does not exist.</p>
        <a href="/">Return to homepage</a>
    </body>
    </html>
    """, 404


# to run locally for development
if __name__ == "__main__":
    myserver.run(debug=True)
