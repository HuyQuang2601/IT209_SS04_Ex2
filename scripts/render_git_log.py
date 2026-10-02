"""Render the real Git graph output as a terminal-style PNG."""

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images" / "git-log-graph.png"
COMMAND = ["git", "log", "--graph", "--oneline"]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "consolab.ttf" if bold else "consola.ttf"
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)


def main() -> None:
    result = subprocess.run(
        COMMAND,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    lines = result.stdout.rstrip().splitlines()

    width, height = 1400, 540
    image = Image.new("RGB", (width, height), "#0c0c0c")
    draw = ImageDraw.Draw(image)
    normal = load_font(27)
    bold = load_font(27, bold=True)

    # Thanh tiêu đề giúp ảnh có hình thức của một cửa sổ terminal độc lập.
    draw.rectangle((0, 0, width, 48), fill="#202020")
    draw.ellipse((18, 16, 34, 32), fill="#ff5f57")
    draw.ellipse((44, 16, 60, 32), fill="#febc2e")
    draw.ellipse((70, 16, 86, 32), fill="#28c840")
    draw.text((110, 10), "Git Bash — Ex2", font=bold, fill="#e8e8e8")

    y = 78
    draw.text((24, y), "$ git log --graph --oneline", font=bold, fill="#7ee787")
    y += 48
    for line in lines:
        draw.text((24, y), line, font=normal, fill="#f0f0f0")
        y += 42

    draw.text(
        (24, height - 42),
        "Repository: homework/session_04/ex2",
        font=normal,
        fill="#8b949e",
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
