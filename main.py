import re
from tkinter.filedialog import askopenfilename
import sys

filename = askopenfilename()

with open(filename, 'r') as data:
  plaintext = data.read()

sys.stdout = open('output.csv', 'wt')

plaintext = re.sub('\$ ', '$', plaintext)
plaintext = re.sub('[ ]+', ',', plaintext)


print(plaintext)