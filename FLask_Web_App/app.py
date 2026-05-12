from flask import Flask, render_template, request
import os
from utils.inference import process_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        files = request.files.getlist("files")

        results = []
        breed_results = []

        for file in files:

            if file.filename == "":
                continue

            filename = os.path.basename(file.filename)

            filepath = os.path.join(UPLOAD_FOLDER, filename)

            file.save(filepath)

            output_path = os.path.join(
                RESULT_FOLDER,
                "output_" + filename
            )

            if filename.lower().endswith(
                (".jpg", ".jpeg", ".png")
            ):

                breeds = process_image(filepath, output_path)

                results.append(output_path)
                breed_results.append(breeds)

        return render_template(
            "index.html",
            results=results,
            breed_results=breed_results
        )

    return render_template(
        "index.html",
        results=None,
        breed_results=None
    )


if __name__ == "__main__":
    app.run(debug=True)