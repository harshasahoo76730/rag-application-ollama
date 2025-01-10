export UV_LINK_MODE=copy

uv venv
uv pip install --no-cache-dir --upgrade pip setuptools wheel
uv pip install --no-cache-dir --upgrade -r requirements.txt
