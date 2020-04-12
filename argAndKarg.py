'''
参数调用顺序：
        常规调用，
        *args调用，
        **kwargs调用
'''


def test_arg(f_arg,*args):
    print('f_arg : ',f_arg) # f_arg :  1
    print('*args : ',args)  # *args :  (2, 3, 4)

test_arg(1,2,3,4)

def test_kargs(f_arg,**kwargs):
    print('f_arg_kw : ',f_arg)  #f_arg_kw :  1
    print('**kwags : ' ,kwargs) #**kwags :  {'k1': 2, 'k2': 3, 'k3': 4, 'k4': 5}
test_kargs(1,k1=2,k2=3,k3=4,k4=5)

def test_kwargs_me(**kwargs):
    for k,v in kwargs.items():
        print('{0} is {1}'.format(k,v)) #name is tomas
test_kwargs_me(name='tomas')

