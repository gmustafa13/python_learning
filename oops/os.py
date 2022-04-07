import os;
# for current working dir
print(os.getcwd())

#changing dir
os.chdir("/home/gulam/Desktop/projects/python_learning/projects")

print(os.getcwd())

#  write file in cwd
with open('test.txt','w') as f:
    f.write('this is test file')