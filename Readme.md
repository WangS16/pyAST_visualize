# pyAST_visualize


该项目为python代码的抽象语法树(AST)可视化程序

原文件来自于python库[showast](https://github.com/hchasestevens/show_ast)，由于`showast`只能在jupyter notebook中使用，本人对源代码进行了修改，可以直接使用python脚本或从python命令行生成可视化文件。

## 使用方法

使用show_ast可视化抽象语法树

使用show_source可视化inspectable对象

nltk_plot参数默认为False(使用Graphviz渲染)，使用nltk渲染可将参数设置为True(生成图片不够清晰，不能生成svg矢量格式，生成速度慢，不推荐)

```python
from py_ast_visualize.visualize import show_ast, show_source

show_ast(tree, settings=Settings, nltk_plot=True, save_path=ast_save_file, format='svg')

show_source(this, settings=Settings, nltk_plot=False, save_path=source_save_file, format='png')
```

修改Settings字典能够更改可视化风格选项，具体参数设置可以参考[Graphviz](http://www.graphviz.org)官网的文档介绍[http://www.graphviz.org](http://www.graphviz.org/documentation/)
```python
from py_ast_visualize.visualize import Settings
Settings['shape'] = 'box'
```


## 项目文件结构

```
astshow
    |--py_ast_visualize
    |    |
    |    |--__init__.py
    |    |
    |    |--visualize.py
    |    |  AST可视化主文件，定义了函数show_ast和show_source
    |    |          |                 |
    |    |          ↓                 |
    |    |--graphviz_plot.py----------┼---╮
    |    |  使用graphviz引擎渲染图像   |   |
    |    |                            ↓   |
    |    |------------------nltk_plot.py--|
    |    |  使用nltk引擎渲染图像           |
    |    |          |                     |
    |    |          ↓                     |
    |    |--contextmanagers.py            |
    |    |  nltk_plot.py的依赖文件         ▏
    |    |                                |
    |    ╰--asts.py ←---------------------╯
    |       定义了一个*_plot.py的共同依赖函数
    |
    |--example.py
    |  一个使用实例
    |
    |--test.py
    |   example.py的测试文件
    |
    ╰--images
       生成图片的文件夹
```
    
