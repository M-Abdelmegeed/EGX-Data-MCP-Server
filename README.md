# EGX-Data-MCP-Server

MCP server for Egyptian Exchange (EGX) stock tools.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/M-Abdelmegeed/EGX-Data-MCP-Server.git
   cd EGX-Data-MCP-Server/egx-mcp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Ensure you have Python 3.11 or higher installed.
2. Run the MCP server using the following command:
   ```bash
   uv --directory . run main.py
   ```

## Adding the MCP Server

To add the EGX MCP server to your environment, use the following configuration in your `settings.json`:

```json
"egx-mcp": {
    "command": "uv",
    "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/egx-mcp",
        "run",
        "main.py"
    ]
}
```

Replace the directory path with the appropriate path to the `egx-mcp` folder on your system.

## Additional Installation Steps

### Installing `uv` Command

To install the `uv` command, run the following command in PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Make sure to restart your terminal afterwards to ensure that the `uv` command gets picked up.

### Setting Up the Project

#### Windows

1. Create a new directory for your project:
   ```bash
   uv init egx-mcp
   cd egx-mcp
   ```

2. Create a virtual environment and activate it:
   ```bash
   uv venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv add mcp[cli] httpx
   ```

4. Create your server file:
   ```bash
   new-item main.py
   ```