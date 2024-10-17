# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

import os

os.system("pip install myst_parser")

os.system("git clone --depth 1 https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi freenove_kit")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'freenove-docs'
copyright = '2024, suhayl'
author = 'suhayl'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['recommonmark','sphinx_markdown_tables']
extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    ]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']



html_logo = "_static/2.png"
# html_theme = 'alabaster'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': -1,
    'version_selector': True,
    'flyout_display': "attached",
    
}

# html_theme = 'groundwork'
# import sphinx_pdj_theme
# html_theme = 'sphinx_pdj_theme'
# html_theme_path  = [sphinx_pdj_theme.get_html_theme_path()]


# multi-language docs
language = 'en'
locale_dirs = ['../locales/']   # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.

