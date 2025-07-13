from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify_image", methods=["POST"])
def classify_image():
    image_file = request.files["image_file"]

    if image_file:
        image_data = image_file.read()
        import base64
        encoded_image_data = "data:image/jpeg;base64," + base64.b64encode(image_data).decode('utf-8')

        result = util.classify_image(encoded_image_data)

        if "error" in result[0]:
            return render_template("index.html", result=None, error=result[0]["error"])
        else:
            return render_template("index.html", result=result, error=None)
    else:
        return render_template("index.html", result=None, error="No image uploaded.")

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run()
