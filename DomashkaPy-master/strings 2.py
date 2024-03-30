ugly = " tiTle of MY new Book\n\n"

pretty = ugly.strip().title()
print(f"pretty: {pretty}")
assert pretty == "Title Of My New Book"