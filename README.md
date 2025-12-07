# 🤖 DeepSeek Sidekick API

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.123+-green.svg)](https://fastapi.tiangolo.com)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://astral.sh)
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)](https://sqlite.org)

> A modern API for interacting with the DeepSeek model, with chat history saved to an SQLite database and a sleek web interface.

## 🚀 Quick Start

### Installation
```bash
git clone <repository-url>
cd deepseek_sidekick_api
uv sync
cp .env.example .env  # Set up your DEEPSEEK_API_KEY
```

### Running the Backend API
```bash
uv run uvicorn main:app --reload
```

### Running the Frontend
Open `index.html` in your browser or serve it with any static file server:
```bash
# Using Python's built-in server
python -m http.server 5500

# Or using Node.js http-server (install with: npm install -g http-server)
http-server -p 5500
```

Then visit http://localhost:5500 in your browser.

## 📋 Requirements

- **Python 3.13+**
- **UV** (package manager)
- **DeepSeek API Key** (get one at https://platform.deepseek.com/)

## 🏗️ Project Structure

```
deepseek_sidekick_api/
├── 📦 pyproject.toml          # Project configuration and dependencies
├── 📦 uv.lock                 # Dependency lock file
├── 🔧 main.py                 # Main FastAPI application
├── 🔧 db.py                   # Database models and functions
├── 🔧 config.py               # Application configuration
├── 🔧 deepseek_client.py      # DeepSeek API client
├── 🖥️ index.html             # Modern web frontend interface
├── 📝 .env.example            # Environment variables example
├── 🗃️ data.db                # SQLite database (created automatically)
```

## 🛠️ API Endpoints

### POST `/requests` - Send a prompt to DeepSeek
Sends your prompt to the DeepSeek model and returns the response.

```bash
curl -X POST "http://localhost:8000/requests" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Hello, how are you?"}'
```

### GET `/requests` - Get chat history
Returns the history of all requests from the current user (by IP address).

```bash
curl -X GET "http://localhost:8000/requests"
```

## 🌐 Web Interface

The project includes a modern web interface (`index.html`) featuring:
- Real-time chat interface with AI
- Message history loading
- Responsive design with Tailwind CSS
- Smooth animations and loading indicators
- Support for both localhost and 127.0.0.1 origins

To use the web interface:
1. Start the backend API server
2. Serve the `index.html` file on port 5500
3. Visit http://localhost:5500 in your browser

## 📦 UV Package Management

### Installing UV
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### UV Commands
```bash
uv sync               # Sync dependencies
uv add package        # Add a package
uv remove package     # Remove a package
uv run command        # Run a command in the environment
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file based on `.env.example`:
```bash
DEEPSEEK_API_KEY=your-api-key-here
```

## 🗃️ Database

The project uses SQLite to store chat history:

**`chat_requests` table structure:**
- `id` - Unique record identifier
- `ip_address` - User's IP address
- `prompt` - User's prompt text
- `response` - Response from the DeepSeek model

The database is created automatically when the application starts.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Create a Pull Request

## 🔗 Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [DeepSeek Platform](https://platform.deepseek.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.