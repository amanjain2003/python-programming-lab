st = "aman"
all_freq = {}
  
for i in st:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters :\n "+str(all_freq))