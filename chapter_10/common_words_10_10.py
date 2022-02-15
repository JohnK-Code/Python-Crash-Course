#### TRY IT YOURSELF - Chapter 10 - Page 202 - Common Words
def word_count(filename, word):
    """Count the number of times a word appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{filename} not found.")
    else:
        print(f"File '{filename}' contains the word '{word}' {content.lower().count(word)} times.")

filenames = ['little_women.txt', 'moby_dick.txt', 'the_teeth_of_the_tiger.txt']
for filename in filenames:
    word_count(filename, 'the ')