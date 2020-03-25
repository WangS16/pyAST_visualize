import ast
import sys
import antigravity
import this
import os
from py_ast_visualize.visualize import show_ast, show_source
from py_ast_visualize.visualize import Settings

# 绘图可调的选项设置
# Settings = dict(
#     # Styling options:
#     scale=2,
#     font='courier',
#     shape='none',
#     terminal_color='#008040',
#     nonterminal_color='#004080',

#     # AST display options:
#     omit_module=True,
#     omit_docstrings=True
# )

def read_file_to_string(filename):
    f = open(filename, 'rt')
    s = f.read()
    f.close()
    return s

directory, file  = os.path.split(sys.argv[0])
test_file = directory + "/test.py"
ast_save_file = directory + "/images/temp"
source_save_file = directory + "/images/this"



Settings['shape'] = 'box'
os.mkdir(directory+"/images")

tree = ast.parse(read_file_to_string(test_file), test_file)
show_ast(tree, settings=Settings, nltk_plot=False, save_path=ast_save_file, format='png')


show_source(this, settings=Settings, nltk_plot=False, save_path=source_save_file, format='png')
