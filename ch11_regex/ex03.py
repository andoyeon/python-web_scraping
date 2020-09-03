import re

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)


# The Double Split Pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# The Regex Version
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print(y)

# Even Cooler Regex Version
y = re.findall('^From .*@([^ ]*)', lin)
print(y)