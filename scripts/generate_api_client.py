#!/usr/bin/env python3
"""Generate API clients from an OpenAPI specification using openapi-generator-cli (Docker)."""

import argparse
import subprocess
import sys
from pathlib import Path

DOCKER_IMAGE = "openapitools/openapi-generator-cli:latest"

GENERATORS = {
    "typescript": "typescript-fetch",
    "python": "python",
}


def generate(openapi_url: str, generator: str, package_name: str, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)

    cmd = [
        "docker", "run", "--rm",
        "--network", "host",
        "-v", f"{output.resolve()}:/out",
        DOCKER_IMAGE,
        "generate",
        "-i", openapi_url,
        "-g", generator,
        "-o", "/out",
        "--package-name", package_name,
        "--additional-properties", f"npmName={package_name},projectName={package_name}",
    ]

    print(f"\n{'='*60}")
    print(f"Generator : {generator}")
    print(f"Package   : {package_name}")
    print(f"Output    : {output.resolve()}")
    print(f"{'='*60}\n")

    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        print(f"[ERROR] Generator '{generator}' failed (exit {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)

    print(f"[OK] Client generated at {output.resolve()}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate API clients from an OpenAPI spec.")
    parser.add_argument("-u", "--url", required=True, help="URL to the openapi.json spec")
    parser.add_argument("-g", "--generators", nargs="+", choices=GENERATORS.keys(), required=True, help="Generators to run")
    parser.add_argument("-n", "--name", required=True, help="Base package name")
    parser.add_argument("-o", "--output", required=True, type=Path, help="Base output directory")
    args = parser.parse_args()

    for gen_alias in args.generators:
        generator = GENERATORS[gen_alias]
        pkg = f"{args.name}-{gen_alias}" if len(args.generators) > 1 else args.name
        out = args.output / gen_alias if len(args.generators) > 1 else args.output
        generate(args.url, generator, pkg, out)


if __name__ == "__main__":
    main()
