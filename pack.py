#!/usr/bin/env python3
import hashlib
import os
import platform
import tarfile
import shutil
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


osname = platform.system().lower()
stamp = datetime.now().strftime("%Y%m%d-%H%M")

input_dir = Path("alpican")
output_dir = Path("output")

if not input_dir.exists():
    print(f"error: input directory not found: {input_dir}")
    exit(1)

output_dir.mkdir(parents=True, exist_ok=True)

version = input("version: ").strip()

if not version:
    print("error: version is required")
    exit(1)


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


target_boot_member = f"{input_dir.name}/boot.img"

extracted_boot_name = f"boot-{base_name}.img"
extracted_boot_path = output_dir / extracted_boot_name


with tarfile.open(archive_path, "r:gz") as tar:
    try:
        member = tar.getmember(target_boot_member)

        boot_file_obj = tar.extractfile(member)

        if boot_file_obj is not None:
            with extracted_boot_path.open("wb") as out_f:
                shutil.copyfileobj(boot_file_obj, out_f)

            boot_checksum = get_sha256(extracted_boot_path)

            print("-" * 40)
            print(f"extracted: {extracted_boot_path}")
            print(f"boot sha256: {boot_checksum}")

        else:
            print(
                f"\nwarning: '{target_boot_member}' is not a regular file"
            )

    except KeyError:
        print(
            f"\nwarning: '{target_boot_member}' not found in archive, "
            "skipping extraction"
        )


#generate SHA256SUMS.txt

sha_file = output_dir / "SHA256SUMS.txt"

files_for_hash = [
    archive_path
]

if extracted_boot_path.exists():
    files_for_hash.append(extracted_boot_path)

write_sha256sums(
    files_for_hash,
    sha_file
)

print("-" * 40)
print(f"sha256 file: {sha_file}")
