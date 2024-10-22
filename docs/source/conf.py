# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())


# os.system("pip install myst_parser")

# os.system("git clone --depth 1 https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi freenove_kit")

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
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
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


html_logo = "_static/images/freenove-logo.jpg"
# html_theme = 'alabaster'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'logo_only': True,
    'navigation_depth': -1,
    'version_selector': True,
    'includehidden': True,
    'style_nav_header_background': '#FFF',

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

rst_prolog = """
.. include:: <s5defs.txt>
"""

html_css_files = [
    "css/color-roles.css",
]

extlinks = {
    "tutorial-link": (
        "rpi-starter-kit/%s",
        "tutorial-link%s"
    )
}

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")


intersphinx_mapping = {
    "rpi-starter-kit": ("https://docs.freenove.com/projects/rpi-starter-kit/en/latest/", None),
}
intersphinx_disabled_reftypes = ["*"]