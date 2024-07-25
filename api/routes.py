from flask import request, jsonify
from src.core import read_file_records
from api import app

records = []


@app.route('/records', methods=['POST'])
def add_record():
    record = request.json  # Assuming JSON input
    records.append(record)
    return jsonify({"message": "Record added successfully"})


