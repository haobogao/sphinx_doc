# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import recommonmark
from recommonmark.transform import AutoStructify

# At the bottom of conf.py
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
            'enable_math': True,
#            'enable_auto_doc_ref': True,
            'enable_inline_math': False,
            }, True)
    app.add_transform(AutoStructify)

project = 'sphinx_demo'
copyright = '2021, haobo'
author = 'haobo'

# The full version, including alpha/beta/rc tags
release = '0.1rc1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

master_doc = 'index'

pygments_style = None
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import sphinx_theme
#html_theme = "neo_rtd_theme"
#html_theme_path = [sphinx_theme.get_html_theme_path('neo_rtd_theme')]
#html_theme = "sphinx_rtd_theme"
import stanford_theme
html_theme = "stanford_theme"
html_theme_path = [stanford_theme.get_html_theme_path()]
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'navigation_depth': 3,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']



source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']


autosectionlabel_prefix_document = True


graphviz_dot = 'dot'
graphviz_dot_args = ['-Gfontname=Georgia',
                     '-Nfontname=Georgia',
                     '-Efontname=Georgia']
graphviz_output_format = 'svg'


plantuml = 'java -jar /plantuml.jar'
plantuml_output_format = 'svg'
plantuml_latex_output_format = 'eps'



latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'fontpkg': r'''
\setsansfont{gbsn00lp.ttf}  %  选择系统字体, fc-list查看 当前系统可用的字体, 我使用的是 SimSun 宋体
''',
  'preamble': r'''
\usepackage{sphinx}
\usepackage{xeCJK}
\geometry{a4paper,left=3cm,right=3cm,top=2cm,bottom=2cm}
\usepackage[titles]{tocloft}
\usepackage{hyperref} 
\usepackage{xunicode}
\parindent 2em
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
    'papersize' : 'a4paper'
}
latex_show_urls = 'footnote'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'note.tex', u'Kernel Research Notes',
     u'haobo', 'manual'),
]



