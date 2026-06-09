from pathlib import Path

base = Path("docs/simple")

for pkg in base.iterdir():
    if not pkg.is_dir():
        continue

    wheels = sorted(pkg.glob("*.whl"))

    html = "<html><body>\n"

    for w in wheels:
        # optional: highlight platform in name
        html += f'<a href="{w.name}">{w.name}</a><br/>\n'

    html += "</body></html>"

    (pkg / "index.html").write_text(html)

print("Cross-platform index built")
