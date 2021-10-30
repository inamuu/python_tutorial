from urllib.request import urlopen

with urlopen('https://inamuu.com') as response:
  for line in response:
    line = line.decode('utf-8')
    print(line)
