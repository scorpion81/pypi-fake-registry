from pathlib import Path

BASE = Path("site/simple")

for pkg_dir in BASE.iterdir():
    if not pkg_dir.is_dir():
        continue

    wheels = sorted(pkg_dir.glob("*.whl"))

    html = ["<html><body>"]

    for wheel in wheels:
        html.append(
            f'<a href="{wheel.name}">{wheel.name}</a><br/>'
        )

    html.append("</body></html>")

    (pkg_dir / "index.html").write_text(
        "\n".join(html),
        encoding="utf-8"
    )

print("Index generated")
