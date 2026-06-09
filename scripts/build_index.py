from pathlib import Path

BASE = Path("site/simple")
PKGS = []
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

    PKGS.append(pkg_dir)

html = ["<html><body>"]
for pkg in PKGS:
    html.append(
        f'<a href="{pkg}">{pkg}</a><br/>'
    )
html.append("</body></html>")

(BASE / "index.html").write_text(
    "\n".join(html),
    encoding="utf-8"
)

root = Path("site")
(root / "index.html").write_text("""
<html>
  <body>
    <a href="simple/">Simple Index</a>
  </body>
</html>
""")

print("Index generated")
