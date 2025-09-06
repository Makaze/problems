import check50
from re import escape


@check50.check()
def test_debug():
    """Print fpdf version"""

    packages = [
        "pygame",
        "opencv-python",
        "scikit-learn",
        "tensorflow",
        "pillow",
        "tensorflow",
        "transformers",
        "nltk",
    ]

    process = check50.run("pip3 freeze")
    result = process.stdout()
    for line in result.split():
        if any(p in line for p in packages):
            process.stdin(line, prompt=False)
    process.kill()
