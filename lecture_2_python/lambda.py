people = [
  {"name": "Bb", "house": "Ff"},
  {"name": "Aa", "house": "Ee"},
  {"name": "Cc", "house": "Dd"}
]

pople = people

# the code below and the code with lambda (belower) do the same thing
#def f(person):
#  return person["house"]
#people.sort(key=f)

people.sort(key=lambda person: person["house"])
print('first sort using lambda')
print(people)

def f(person):
  return person["house"]
pople.sort(key=f)
