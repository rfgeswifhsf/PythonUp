'''
指定的文本模式去检查字符串的开头或者结尾

endwith
startwith
'''

filename='spam.txt'
print(filename.endswith('.txt'))  # True
print(filename.startswith('.txt')) # False

'''
多种检测可用元组
注意是元组：endswith(('.c','.h'))
'''

filename1=[ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]

filename_result=[name for name in filename1 if name.endswith(('.c','.h'))]
print(filename_result)      #['foo.c', 'spam.c', 'spam.h']
