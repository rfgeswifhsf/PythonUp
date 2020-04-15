#conding==utf-8
with open('text.txt','wt') as f:
    # ways1
    # data=f.read()
    # print('data -- ',data)

    f.write('失落的宝藏')
    # ways2
    # for line in f:
    #     print('line -- ',line)
    #
import urllib.request
import io

u = urllib.request.urlopen('https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p16_add_change_encoding_of_already_open_file.html')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)
