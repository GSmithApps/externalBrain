"""
how can I do simple parsing in python? for example,
first split by hyphens, then split by commas, and
in each element, trim whitespace

There may be at most one hyphen. The hyphen splits
the elements into two categories, and if there is
no hyphen present, all elements go into category 1
"""

def parse_text(text):
    # Check if a hyphen is present
    if '-' in text:
        cat1_text, cat2_text = text.split('-', 1)  # Split into two categories at most once
    else:
        cat1_text = text
        cat2_text = ""

    # Split by commas and trim whitespace for category 1
    cat1_elements = [element.strip() for element in cat1_text.split(',')]

    # Split by commas and trim whitespace for category 2
    cat2_elements = [element.strip() for element in cat2_text.split(',')] if cat2_text else []

    return cat1_elements, cat2_elements

# Test
text1 = "apple, banana - orange , grape"
cat1, cat2 = parse_text(text1)
print(cat1)  # ['apple', 'banana']
print(cat2)  # ['orange', 'grape']

text2 = "blueberry , raspberry"
cat1, cat2 = parse_text(text2)
print(cat1)  # ['blueberry', 'raspberry']
print(cat2)  # []
