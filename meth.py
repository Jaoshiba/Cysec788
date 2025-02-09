from flask import Blueprint, request, jsonify
import subprocess

# Correct Blueprint initialization
meth = Blueprint('meth', __name__)

@meth.route('/')
def home():
    return 'home'

@meth.route('/test/', methods=['POST'])
def boolean_base():
    data = request.get_json()
    
    # Extract input data
    url = data.get('url')
    technique = data.get('technique', '').upper() # BEUSTQ

    # Validate input
    if not url or technique not in ['B', 'E', 'T', 'U']:
        return jsonify({"error": "Valid URL and technique (B, E, T, U) are required"}), 400
    
    # Build SQLMap command
    mapcommand = ['python','sqlmap', '-u', url, f'--technique={technique}', '--batch']

    try:
        result = subprocess.run(mapcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify({"output": result.stdout})
    except FileNotFoundError:
        return jsonify({"error": "SQLMap not found. Ensure it is installed"}), 500
