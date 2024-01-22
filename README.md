# python-cydantic

conao3's pydantic CLI wrapper.

## Install

### Install from PyPI

release soon.

### Install from Source

```bash
poetry install
```

## Usage

### generate

Prepare pydantic model named `Model`.

```python
import pydantic


class Model(pydantic.BaseModel):
    name: str = 'John Doe'
    age: int = 20
```

Generate `Model`'s schema.

```bash
$ cydantic generate -s sample/schema01.py
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

Output using yaml format.

```bash
$ cydantic generate -s sample/schema01.py --format yaml
properties:
  age:
    default: 20
    title: Age
    type: integer
  name:
    default: John Doe
    title: Name
    type: string
title: Model
type: object
```

### validate

```bash
$ cydantic validate -s sample/schema01.py -f yaml -i sample/inpt01.json
age: 20
name: conao3

$ cydantic validate -s sample/schema01.py -f yaml -i sample/inpt02.json
age: 18
name: conao3

$ cydantic validate -s sample/schema01.py -f yaml -i sample/inpt03.json
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/conao/dev/repos/python-cydantic/src/cydantic/main.py", line 86, in main
    args.handler(args)
  File "/Users/conao/dev/repos/python-cydantic/src/cydantic/main.py", line 48, in command_validate
    obj = model.model_validate(inpt)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/conao/dev/repos/python-cydantic/.venv/lib/python3.12/site-packages/pydantic/main.py", line 503, in model_validate
    return cls.__pydantic_validator__.validate_python(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for Model
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Unknown', input_type=str]
    For further information visit https://errors.pydantic.dev/2.5/v/int_parsing
```
