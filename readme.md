```shell
pip list # 列出所有已经安装的第三方模块
pip freeze > requirements.txt     # 生成 requirements.txt
pip install -r requirements.txt   # 安装 requirements 中的模块
pip uninstall [-y] -r requirements.txt # 卸载 requirements 中的模块
pip show <module_name>              # 显示一个或多个已安装模块的信息，包括这个包的依赖关系
pip uninstall [-y] <module_name>    # 卸载指定模块， -y 表示不需要进行确认
```