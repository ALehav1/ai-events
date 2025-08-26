from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

def render_html(sections: dict, out_path: Path):
    """Render HTML report using Jinja2 template"""
    env = Environment(
        loader=FileSystemLoader(str(Path(__file__).parent / "templates")),
        autoescape=select_autoescape(["html"])
    )
    tpl = env.get_template("report.html.j2")
    html = tpl.render(report={
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        **sections
    })
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return out_path
