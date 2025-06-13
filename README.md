# DPM Prototype

## Setup
1. Copy `.env.example` to `.env` and customise values.
2. Create a Python virtual environment:
   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Initialise the database:
   sqlite3 dpm.db < dpm_schema.sql