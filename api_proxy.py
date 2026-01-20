#!/usr/bin/env python3
"""
ThousandEyes API Proxy Server
This proxy server handles API requests server-side to avoid CORS issues.
Run with: python3 api_proxy.py
Then update the frontend to use http://localhost:5000/api/ instead of direct API calls.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_BASE = 'https://api.thousandeyes.com/v7'

@app.route('/api/account-groups', methods=['GET'])
def get_account_groups():
    """Proxy request to ThousandEyes account groups endpoint"""
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Missing Authorization header'}), 401
    
    try:
        url = f'{API_BASE}/account-groups'
        headers = {
            'Authorization': token,
            'Accept': 'application/hal+json'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), getattr(e.response, 'status_code', 500)

@app.route('/api/endpoint/labels', methods=['GET'])
def get_labels():
    """Proxy request to ThousandEyes endpoint labels endpoint"""
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Missing Authorization header'}), 401
    
    account_group_id = request.args.get('aid')
    if not account_group_id:
        return jsonify({'error': 'Missing aid parameter'}), 400
    
    try:
        url = f'{API_BASE}/endpoint/labels'
        headers = {
            'Authorization': token,
            'Accept': 'application/hal+json'
        }
        params = {
            'aid': account_group_id
        }
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), getattr(e.response, 'status_code', 500)

@app.route('/api/endpoint/agents', methods=['GET'])
def get_endpoint_agents():
    """Proxy request to ThousandEyes endpoint agents endpoint"""
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Missing Authorization header'}), 401
    
    try:
        url = f'{API_BASE}/endpoint/agents'
        headers = {
            'Authorization': token,
            'Accept': 'application/hal+json'
        }
        
        # Forward all query parameters
        params = dict(request.args)
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), getattr(e.response, 'status_code', 500)

@app.route('/api/v6/endpoint-agents/state', methods=['POST'])
def update_endpoint_state():
    """Proxy request to ThousandEyes endpoint agents state endpoint"""
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Missing Authorization header'}), 401
    
    try:
        url = f'{API_BASE.replace("/v7", "")}/v6/endpoint-agents/state'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'Accept': 'application/hal+json'
        }
        
        data = request.json
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), getattr(e.response, 'status_code', 500)

@app.route('/api/account-groups/<account_id>', methods=['GET'])
def get_account_group(account_id):
    """Proxy request to get specific account group details"""
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Missing Authorization header'}), 401
    
    try:
        url = f'{API_BASE}/account-groups/{account_id}'
        headers = {
            'Authorization': token,
            'Accept': 'application/hal+json'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), getattr(e.response, 'status_code', 500)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f'Starting API proxy server on http://localhost:{port}')
    print(f'API proxy will forward requests to {API_BASE}')
    app.run(host='0.0.0.0', port=port, debug=True)
