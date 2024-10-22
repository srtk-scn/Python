import random
import string

for each in range(1,2):
  Fiveh1 = ''.join(random.choices(string.ascii_uppercase + " " + string.digits + " ", k=500))
  Fiveh2 = ''.join(random.choices(string.ascii_lowercase +  " " + string.digits, k=500))
  Fiveh3 = ''.join(random.choices(string.ascii_uppercase + " " + string.punctuation, k=500))
  twent20 = ''.join(random.choices(string.ascii_uppercase, k=64000))
  simple = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits, k=5))

  # print(Fiveh1)
  # print(Fiveh2)
  # print(Fiveh3)
  # print(twent20)
  print(simple)