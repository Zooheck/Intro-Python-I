f = open('foo.txt', 'r')
print(f.read())
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('bar.txt', 'w') as f:
    f.write('asdf' + '\n')
    f.write('jkl;' + '\n')
    f.write('qwer' + '\n')
