from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import logging
from resume_analyzer import analyze_resume

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    review = None
    try:
        if request.method == 'POST':
            file = request.files.get('resume')
            if not file or file.filename == '':
                review = {"Error": ["No file selected."]}
            elif allowed_file(file.filename):
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                logging.info(f"✅ File saved to: {filepath}")
                review = analyze_resume(filepath)
                os.remove(filepath)  # Optional cleanup
            else:
                review = {"Error": ["Invalid file format. Please upload a PDF."]}
    except Exception as e:
        logging.error("❌ Exception during resume upload", exc_info=True)
        review = {"Error": [str(e)]}

    return render_template('index.html', review=review)

if __name__ == '__main__':
    app.run(debug=True)
