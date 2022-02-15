#### TRY IT YOURSELF - Chapter 10 - Page 202 - Cats and Dogs
def cats_dogs(filename):
    """Print contents of file."""
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"'{filename}' can't be found.")
    else:
        print(f"{filename}: ")
        for line in lines:
            print(f"\t{line.strip()}")

filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    cats_dogs(file)