import check50

debugging_text = "\n".join(["Debugging" + ("_" * 30) for _ in range(100)])


@check50.check()
def test_debug():
    """Print fpdf version"""

    # With random.seed(0) in testing.py, 6 + 6 is expected output from randint and randrange with range of 0–9
    check50.run("pip3 freeze").stdout(debugging_text, debugging_text, regex=True)
