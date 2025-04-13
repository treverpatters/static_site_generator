from generate_page import *

def test_extract_title():
    # Case: Valid single `h1`
    assert extract_title("# Valid Title") == "Valid Title"

    # Case: Markdown with no `h1`
    try:
        extract_title("## Subheading only")
        assert False, "Expected an exception but none was raised!"
    except Exception as e:
        assert str(e) == "no h1 header"

    # Case: Multiple `#` headers
    markdown = """# First Title
    ## A Subheading
    # Second Title"""
    assert extract_title(markdown) == "First Title"

    # Case: Empty Markdown
    try:
        extract_title("")
        assert False, "Expected an exception but none was raised!"
    except Exception as e:
        assert str(e) == "no h1 header"

    # Case: Multiple `#` (not `h1`)
    try:
        extract_title("## Subheading\n### Smaller Header")
        assert False, "Expected an exception but none was raised!"
    except Exception as e:
        assert str(e) == "no h1 header"

    print("All tests passed!")





