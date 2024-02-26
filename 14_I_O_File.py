
s = "Hello there we are learning python"

# Writing in the file 
# with open('text.txt','w') as f:
#     f.write(s)


# fp = open('text.txt','w')
# fp.write(s)
# fp.close

# Reading the file

with open('text.txt','r') as f:
  read_file =  f.read()
print(read_file)
