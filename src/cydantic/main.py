import argparse
import importlib
import importlib.util
import json
from types import ModuleType

import pydantic
import yaml


def load_module_from_path(path: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location('__load_module__', path)
    if not spec:
        raise Exception(f'Failed to load module from path: {path}')

    if not spec.loader:
        raise Exception(f'spec.loader is None: {path}')

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def output_object(obj: object, format: str) -> str:
    if format == 'json':
        return json.dumps(obj, indent=2, ensure_ascii=False)

    if format == 'yaml':
        return yaml.safe_dump(obj, allow_unicode=True).strip()

    raise Exception(f'Unknown format: {format}')


def command_validate(args: argparse.Namespace) -> None:
    module = load_module_from_path(args.schema)


def command_generate(args: argparse.Namespace) -> None:
    module = load_module_from_path(args.schema)
    model: pydantic.BaseModel = getattr(module, args.model)

    model_schema = model.model_json_schema(by_alias=True)
    result = output_object(model_schema, args.format)
    print(result)


def parse_args() -> tuple[argparse.ArgumentParser, argparse.Namespace]:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_validate = subparsers.add_parser('validate')
    parser_validate.set_defaults(handler=command_validate)
    parser_validate.add_argument('-s', '--schema', required=True)
    parser_validate.add_argument('-i', '--input')

    parser_generate = subparsers.add_parser('generate')
    parser_generate.set_defaults(handler=command_generate)
    parser_generate.add_argument('-s', '--schema', required=True)
    parser_generate.add_argument('-m', '--model', default='Model')
    parser_generate.add_argument('-t', '--type', choices=['jsonschema'], default='jsonschema')
    parser_generate.add_argument('-f', '--format', choices=['json', 'yaml'], default='json')

    return parser, parser.parse_args()


def main() -> None:
    parser, args = parse_args()
    print(args)
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
