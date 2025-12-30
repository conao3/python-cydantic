# cydantic

A lightweight CLI tool for working with Pydantic models. Generate JSON schemas and validate data directly from the command line.

## Features

- **Schema Generation**: Export JSON schemas from Pydantic models
- **Data Validation**: Validate JSON/YAML input against Pydantic models
- **Multiple Formats**: Output in JSON or YAML format

## Installation

### From PyPI (Recommended)

Install using [pipx](https://pipx.pypa.io/stable/) for isolated CLI tool management:

```bash
pipx install cydantic
```

### From Source

```bash
poetry install
```

## Quick Start

### Define a Pydantic Model

Create a Python file with your Pydantic model (e.g., `schema.py`):

```python
import pydantic

class Model(pydantic.BaseModel):
    name: str = "John Doe"
    age: int = 20
```

### Generate JSON Schema

```bash
cydantic generate -s schema.py
```

Output:

```json
{
  "properties": {
    "name": {
      "default": "John Doe",
      "title": "Name",
      "type": "string"
    },
    "age": {
      "default": 20,
      "title": "Age",
      "type": "integer"
    }
  },
  "title": "Model",
  "type": "object"
}
```

Use `--format yaml` for YAML output:

```bash
cydantic generate -s schema.py --format yaml
```

### Validate Input Data

Validate a JSON or YAML file against your schema:

```bash
cydantic validate -s schema.py -i input.json
```

With YAML output format:

```bash
cydantic validate -s schema.py -i input.json --format yaml
```

## Command Reference

### generate

Generate a JSON schema from a Pydantic model.

| Option | Description |
|--------|-------------|
| `-s, --schema` | Path to Python file containing the model (required) |
| `-m, --model` | Model class name (default: `Model`) |
| `-f, --format` | Output format: `json` or `yaml` (default: `json`) |

### validate

Validate input data against a Pydantic model.

| Option | Description |
|--------|-------------|
| `-s, --schema` | Path to Python file containing the model (required) |
| `-m, --model` | Model class name (default: `Model`) |
| `-i, --input` | Path to input file in JSON or YAML format (required) |
| `-f, --format` | Output format: `json` or `yaml` (default: `json`) |

## Requirements

- Python 3.12+
- Pydantic 2.x

## License

Apache-2.0
