import pytest
from src.display import display_search_results
from io import StringIO
import sys

@pytest.mark.parametrize(
    "search_results, expected_output",
    [
        (["file1.txt", "file2.txt"], "Matching Files:\nfile1.txt\nfile2.txt\n"),
        ([], "No matching files found.\n"),
    ],
)
def test_display_search_results(search_results, expected_output):
    captured_output = StringIO()
    sys.stdout = captured_output
    display_search_results(search_results)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output
