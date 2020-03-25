import os
import re
import ast
import imp
import inspect
from .graphviz_plot import render as grender
from .nltk_plot import render as nrender

# from IPython.core.magic import register_cell_magic
# from IPython.display import display
    
    
__all__ = ['show_ast', 'show_source', 'Settings', 'Renderers',]


# RENDERING_PATH = os.path.join(os.path.dirname(__file__), 'rendering')


class Renderers:
    graphviz = 'graphviz' #, [RENDERING_PATH]
    nltk = 'nltk'        # , [RENDERING_PATH]
    

Settings = dict(
    # Styling options:
    scale=2,
    font='courier',
    shape='none',
    terminal_color='#008040',
    nonterminal_color='#004080',

    # AST display options:
    omit_module=True,
    omit_docstrings=True,

    # Rendering engine is expected to expose "render" function
    # renderer=Renderers.graphviz,
)
        
save_path = os.getcwd() + "\\images\\temp"
format = "png"

def show_ast(module, settings=Settings, nltk_plot=False, save_path=save_path, format=format):
    """
    可视化python代码的抽象语法树AST
    :param
        module: ast.AST
        settings: 绘图选项设置
        nltk_plot: False-使用Graphviz渲染，True-使用nltk渲染
        save_path: 生成的可视化文件路径,无需指定文件名后缀
        format: 期望生成的文件格式
    :return
        返回可视化文件的路径
    """
    omit_docstrings = settings['omit_docstrings']
    if settings['omit_module'] and len(module.body) == 1:
        node = module.body[0]
    else:
        node = module
    # renderer = imp.load_module(
    #     'renderer', 
    #     *imp.find_module(*settings['renderer'])
    # )
    if nltk_plot:
        return nrender(node, settings, save_path, format)
    else:
        save_path = save_path + ".gv"
        return grender(node, settings, save_path, format)


# @register_cell_magic
# def showast(__, cell):
#     m = ast.parse(cell)
#     show_ast(m)


def show_source(item, settings=Settings, nltk_plot=False, save_path=save_path, format=format):
    """
    可视化 inspectable objects的抽象语法树AST
    参数和返回值同show_ast()
    """
    src = inspect.getsource(item)
    try:
        module = ast.parse(src)
    except IndentationError:
        initial_whitespace = re.match(r'^\s+', src)
        if initial_whitespace is not None:
            amt_whitespace = len(initial_whitespace.group())
            src = '\n'.join(
                line[amt_whitespace:]
                for line in
                src.splitlines()
            )
        module = ast.parse(src)
    return show_ast(ast.parse(src), settings, nltk_plot, save_path, format)
