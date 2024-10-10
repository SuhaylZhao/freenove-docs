# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'freenove-docs'
copyright = '2024, suhayl'
author = 'suhayl'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for PDF output -----------------------------------------------
 
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto, or owner's choice]).
pdf_documents = [
    (master_doc, 'myproject.pdf', 'My Project Documentation', author, 'manual'),
]
 
# Latex elements for use with the LaTeX writer.
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
    
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage{graphicx}
        \usepackage{hyperref}
    ''',
    
    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
