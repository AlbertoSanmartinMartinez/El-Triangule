#!/usr/bin/env python3
"""Generate API clients from an OpenAPI specification using openapi-generator-cli (Docker)."""

import argparse
import json
import subprocess
import sys
from pathlib import Path

DOCKER_IMAGE = "openapitools/openapi-generator-cli:latest"

GENERATORS = {
    "typescript": "typescript-fetch",
    "python": "python",
}

TYPESCRIPT_PACKAGE_JSON_OVERRIDES = {
    "type": "module",
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "import": "./dist/index.js",
        }
    },
    "scripts": {"build": "tsc"},
    "devDependencies": {"typescript": "^5.0"},
}

TYPESCRIPT_TSCONFIG = {
    "compilerOptions": {
        "declaration": True,
        "target": "ES2020",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "outDir": "dist",
        "lib": ["ES2020", "DOM"],
        "esModuleInterop": True,
        "skipLibCheck": True,
        "strict": False,
    },
    "include": ["src"],
    "exclude": ["dist", "node_modules"],
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

    print(f"[OK] Client generated at {output.resolve()}")


def patch_typescript(output: Path, package_name: str) -> None:
    """Apply ESM/build patches to the generated TypeScript client."""

    pkg_path = output / "package.json"
    if pkg_path.exists():
        pkg = json.loads(pkg_path.read_text())
        pkg.update(TYPESCRIPT_PACKAGE_JSON_OVERRIDES)
        pkg["name"] = package_name
        pkg_path.write_text(json.dumps(pkg, indent=2) + "\n")
        print(f"[PATCH] package.json updated for ESM")

    tsconfig_path = output / "tsconfig.json"
    tsconfig_path.write_text(json.dumps(TYPESCRIPT_TSCONFIG, indent=2) + "\n")
    print(f"[PATCH] tsconfig.json replaced for ESM/bundler")

    print(f"[BUILD] Installing dependencies and compiling...")
    subprocess.run(["npm", "install"], cwd=output, check=True, capture_output=True)
    subprocess.run(["npx", "tsc"], cwd=output, check=True, capture_output=True)
    print(f"[OK] TypeScript client built successfully\n")


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

        if gen_alias == "typescript":
            patch_typescript(out, pkg)


if __name__ == "__main__":
    main()
