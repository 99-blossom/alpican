#!/usr/bin/env python3
import argparse
import hashlib
import platform
import sys
import tarfile
from datetime import datetime
from pathlib import Path


def get_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def write_sha256sums(files: list[Path], output_file: Path) -> None:
    lines = []

    for file_path in files:
        checksum = get_sha256(file_path)
        lines.append(f"{checksum}  {file_path.name}")

    output_file.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--version", required=True)
args = parser.parse_args()

version = args.version.strip()

if not version:
    print("error: version is required")
    sys.exit(1)

osname = platform.system().lower()
stamp = datetime.now().strftime("%Y%m%d-%H%M")

input_dir = Path("alpican")
output_dir = Path("output")

if not input_dir.exists():
    print(f"error: input directory not found: {input_dir}")
    sys.exit(1)

output_dir.mkdir(parents=True, exist_ok=True)

base_name = f"alpican-{version}-{stamp}-from-{osname}"

archive_name = f"{base_name}.tar.gz"
archive_path = output_dir / archive_name


print("creating archive...")

with tarfile.open(archive_path, "w:gz") as tar:
    tar.add(input_dir, arcname=input_dir.name)


size = archive_path.stat().st_size
archive_checksum = get_sha256(archive_path)

print(f"output file: {archive_path}")
print(f"size: {size / 1024 / 1024:.2f} MiB")
print(f"sha256: {archive_checksum}")


# generate SHA256SUMS.txt

sha_file = output_dir / "SHA256SUMS.txt"

files_for_hash = [
    archive_path
]

write_sha256sums(
    files_for_hash,
    sha_file
)

print("-" * 40)
print(f"sha256 file: {sha_file}")
