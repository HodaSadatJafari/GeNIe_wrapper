# GeNIe Wrapper

A FastAPI-based wrapper around **BayesFusion SMILE / GeNIe** that exposes Bayesian network functionality through a REST API.

The project uses **PySMILE** to interact with GeNIe/SMILE models and **FastAPI** to provide a web-accessible API.

## ✨ Features

* FastAPI REST API
* Integration with BayesFusion PySMILE
* Load and work with Bayesian network models
* Expose GeNIe/SMILE functionality through HTTP endpoints
* Interactive API documentation with Swagger UI
* Modern Python dependency management with `uv`

## 🛠️ Tech Stack

* **Python 3.13**
* **FastAPI**
* **Uvicorn**
* **PySMILE 2.4.7**
* **GeNIe / SMILE**
* **uv**

## 📁 Project Structure

```text
GeNIe_wrapper/
├── main.py
├── frontend
├── pyproject.toml
├── uv.lock
├── README.md
└── .venv/
```

## 🚀 Getting Started

### Prerequisites

Make sure you have:

* Python 3.13
* GeNIe / SMILE
* PySMILE 2.4.7
* `uv`

Install `uv` if necessary:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone the repository

```bash
git clone <repository-url>
cd GeNIe_wrapper
```

### Install dependencies

```bash
uv sync
```

If PySMILE is provided through the BayesFusion package index:

```bash
uv pip install \
  --index-url https://support.bayesfusion.com/pysmile-A/ \
  "pysmile==2.4.7"
```

> **Note:** PySMILE is distributed by BayesFusion and may not be available through the standard PyPI index.

## ▶️ Running the API

Start the FastAPI development server with:

```bash
uv run python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### API Documentation

FastAPI automatically provides interactive documentation.

**Swagger UI:**

```text
http://127.0.0.1:8000/docs
```

**ReDoc:**

```text
http://127.0.0.1:8000/redoc
```

## 🔍 Verify PySMILE

You can verify that PySMILE is installed correctly:

```bash
uv run python -c "import pysmile; print(pysmile)"
```

You should see something similar to:

```text
<module 'pysmile' from '.../.venv/lib/python3.13/site-packages/pysmile.so'>
```

Check the Python version:

```bash
uv run python --version
```

## 🧪 Development

Run the application with automatic reload:

```bash
uv run python -m uvicorn main:app --reload
```

After modifying the source code, Uvicorn will automatically reload the application.

## 📦 Dependency Management

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency and environment management.

Add a dependency:

```bash
uv add package-name
```

Add a specific version:

```bash
uv add "package-name==1.2.3"
```

Install/synchronize dependencies:

```bash
uv sync
```

Show installed dependencies:

```bash
uv tree
```

## ⚠️ PySMILE / Python Version

PySMILE contains a compiled native extension (`pysmile.so`), so the Python version matters.

This project uses:

```text
Python 3.13
PySMILE 2.4.7
```

Make sure PySMILE and Python are compatible with each other.

You can check the environment with:

```bash
uv run python --version
uv run python -c "import pysmile; print(pysmile.__file__)"
```

## 🔧 Troubleshooting

### `ModuleNotFoundError: No module named 'pysmile'`

Check whether PySMILE is installed in the project's environment:

```bash
uv run python -c "import pysmile; print(pysmile)"
```

If it is not installed, install it from the BayesFusion package index:

```bash
uv pip install \
  --index-url https://support.bayesfusion.com/pysmile-A/ \
  "pysmile==2.4.7"
```

### Uvicorn uses the wrong Python version

Check:

```bash
uv run which python
uv run which uvicorn
uv run uvicorn --version
```

If Uvicorn is being loaded from a global installation such as:

```text
/home/<user>/.local/bin/uvicorn
```

run Uvicorn through the project's Python:

```bash
uv run python -m uvicorn main:app --reload
```

This ensures Uvicorn uses the same Python environment where PySMILE is installed.

## 📄 License

Add your project's license information here.

## 👤 Author

**Hoda**

---

Built with Python, FastAPI, PySMILE, and GeNIe/SMILE.
