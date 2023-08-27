import io
import os
from shutil import copyfile
#print(os.getcwd())
f=open('text.txt','w')
f.close()
#os.chdir(r'Đường dẫn mới')
os.rename('text.txt','testfile.txt') #đổi tên file
# os.remove('tên đường dẫn or ten file cần xóa')
# copyfile('testfile.txt','filenew.txt')

#viết file không utf8
#def writeFileline(filename, nd_line):
#   f=open('filename','a')
#   f.write(nd_line + '\n')
#   f.close()

#viết file có utf8
#def writeUtf8(filename,nd_line):
#   f=io.open(filename, mode="a",encoding="utf-8")
#   f.write(nd_line + '\n')
#   f.close()

# Đọc File có Utf8
#   f=io.open("File Name",mode="r",endcoding="utf-8")
#   list_line=f.readlines()
#   print(list_line)
#   for line in list_line:
#       print(line)

# Đọc File Không có Utf8
#   f=open("File Name",mode="r")
#   f.read()
#   f.readlines()