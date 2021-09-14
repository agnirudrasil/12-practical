f=open("word.txt",'w')
string="""The text file is a computer file that only contains text and has no special formatting such as bold text, italic text, image, etc.
With Microsoft Windows computers text files are identified with the .txt file extension."""
f.write(string)
f.close()


def count_sentence(string):
    return len(string.split("\n"))

def count_words(string):
    return len(string.split(" "))

print(f"Sentences: {count_sentence(string)}")
print(f"Words: {count_words(string)}")
