# API Proxy Server Setup

Due to CORS (Cross-Origin Resource Sharing) restrictions, direct browser calls to the ThousandEyes API may fail. This Python proxy server acts as a backend to handle API requests and avoid CORS issues.

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Proxy Server**:
   ```bash
   python3 api_proxy.py
   ```

   The server will start on `http://localhost:5000` by default.

3. **Update Frontend Settings**:
   - Open `index.html`
   - The proxy is already configured with `USE_PROXY = true`
   - If you run the proxy on a different port, update `API_PROXY_BASE` in the JavaScript code

## How It Works

The proxy server:
- Receives requests from the frontend (browser)
- Forwards them to the ThousandEyes API with proper authentication
- Returns the response to the frontend
- Handles CORS automatically using Flask-CORS

## Available Endpoints

The proxy provides these endpoints that mirror the ThousandEyes API:

- `GET /api/account-groups` - List account groups
- `GET /api/endpoint/labels?aid={accountGroupId}` - List endpoint labels
- `GET /api/endpoint/agents?aid={accountGroupId}&tag={label}` - List endpoint agents
- `POST /api/v6/endpoint-agents/state` - Update endpoint agent state
- `GET /api/account-groups/{id}` - Get specific account group details
- `GET /health` - Health check

## Configuration

- Default port: 5000
- Change port: Set `PORT` environment variable or modify `port` in `api_proxy.py`
- API base: Hardcoded to `https://api.thousandeyes.com/v7`

## Troubleshooting

- **Connection refused**: Make sure the proxy server is running
- **CORS errors**: The proxy should handle this automatically, but check Flask-CORS is installed
- **API errors**: Check the proxy server console for detailed error messages
- **Port conflicts**: Change the port in `api_proxy.py` or use `PORT=8080 python3 api_proxy.py`
