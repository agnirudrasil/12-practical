#Read from the text file

def not_starting_A(path='./STORY.txt'):
    text = open(path,'r').read()
    t = text.split('\n')
    t = [i for i in t if len(i)>0]
    c = 0
    for i in t:
        if i[0] != 'A': #IDK if case sensitive
            c += 1
    return c

def count_is(path='./STORY.txt'):  
    text = open(path,'r').read()
    return text.count('is')

