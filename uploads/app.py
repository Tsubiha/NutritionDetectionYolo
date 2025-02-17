from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from model import detect_fruits
from database import fetch_nutrition_info,store_visitor_ip, get_unique_visitor_count


app = Flask(__name__,template_folder='../templates')
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit


def allowed_file(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png'))


@app.route('/', methods=['GET', 'POST'])
def index():
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip_list = visitor_ip.split(',')  # Split into a list by commas
    origin_ip = ip_list[0].strip()  # Take the first IP and strip any whitespace
    # Store the IP address in the database
    store_visitor_ip(origin_ip)

    # Get the count of unique visitors
    origin_ip = get_unique_visitor_count()
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Debug print statements
            print(f"File saved to: {file_path}")

            # Detect fruits in the uploaded image
            fruit_names, image_path = detect_fruits(file_path)


            # Debug print statements
            print(f"Detected fruit names: {fruit_names}")

            # Fetch nutritional information for detected fruits
            nutrition_info = [fetch_nutrition_info(fruit_name) for fruit_name in fruit_names]

            # Debug print statements
            print(f"Nutrition info: {nutrition_info}")

            return render_template('result.html', nutrition_info=nutrition_info, image_path=filename)

    return render_template('index.html',visitor_count=origin_ip)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default port is 5000 if PORT env var is not found
    app.run(host='0.0.0.0', port=port)
   # app.run(debug=True)
