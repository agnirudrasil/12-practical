f=open("word.txt",'w')
string="The text file is a computer file that only contains text and has no special formatting such as bold text, italic text, image, etc.\nWith Microsoft Windows computers text files are identified with the .txt file extension."
f.write(string)
f.close()


def count_sentence(string):
    return len(string.split("\n"))

def count_words(string):
    return len(string.split(" "))




#alternate

file_1=open("word.txt","w")
l1= "A text file is a computer file that contains only text and has no special formatting such as bold text, italic text, images etc."
l2="With Microsoft Windows computers text files are identified with the. txt file extension."
file_1.write(l1)
file_1.write('\n')
file_1.write(l2)
file_1.write('\n')
file_1.close()


file_2=open("word.txt","r")
s=file_2.readlines()
linecount=len(s)
file_2.close()
i=0
wordcount=0
for i in range (0,len(s)) :
    wordcount+=len(s[i].split())
print("Number of words in the file is : ",wordcount)
print("Number of lines in the file is : ",linecount)

