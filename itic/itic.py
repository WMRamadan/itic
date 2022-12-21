import typer
import pathlib
from PIL import Image
from rich import print


def get_extension(file_path: str):
    file_extension = pathlib.Path(file_path).suffix
    return file_extension

def convert_image(input_file: str, output_file: str):
    try:
        img = Image.open(input_file)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(output_file)
        return False, None
    except Exception as e:
        return True, e

def app(input_file: str, output_file: str):
    conv, e = convert_image(input_file=input_file, output_file=output_file)
    if conv:
        print(f"[bold red]{e}")
    else:
        input_file_ext = get_extension(input_file)
        output_file_ext = get_extension(output_file)
        d = {
            "Input File": input_file,
            "Input File Extention": input_file_ext,
            "Output File": output_file,
            "Output File Extention": output_file_ext
        }
        print(d)

def main() -> None:
    typer.run(app)
