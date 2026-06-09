from pathlib import Path
import shutil

ARTIFACTS = Path("all_wheels")
OUTPUT = Path("site/simple")

OUTPUT.mkdir(parents=True, exist_ok=True)

for wheel in ARTIFACTS.glob("*.whl"):
    name = wheel.name

    pkg = name.split("-")[0].replace("_", "-")

    pkg_dir = OUTPUT / pkg
    pkg_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(wheel, pkg_dir / wheel.name)
