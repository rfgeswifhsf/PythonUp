'''

创建一个隔离的环境
避免某个模块被升级对自己的影响
可同时用2.X与3.x的包

pip install virtualenv  安装

virtualenv myproject  创建环境

source myproject/bin/activate  激活环境

virtualenv --system-site-packages mycoolproject 全局化（根据需求考虑是否使用）

deactivate 退出

'''
