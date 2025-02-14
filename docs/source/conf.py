# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
#content_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "content"))
#sys.path.insert(0, content_path)

#print(f"Sphinx is searching for content in: {content_path}")  # Debugging outpu
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "content")))

#content_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "content"))
#sys.path.insert(0, content_path)

#print(f"Sphinx is searching for content in: {content_path}")

project = 'chetaa'
copyright = '2024, Mo Oyedeji'
author = 'Mo Oyedeji'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    "sphinx_tabs.tabs",
    'sphinxcontrib.httpdomain',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.plantuml',
    'sphinx_tabs.tabs',
    "myst_parser"
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
  'colon_fence',
  'attrs_block',
  # ... other extensions
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "navigation_depth": 4,  # Keeps nested items visible
    "collapse_navigation": False,  # Ensures sidebar stays expanded
    "sticky_navigation": True,  # Keeps sidebar visible while scrolling
    "includehidden": True,  # Ensures sub-items remain visible
    "titles_only": False,  # Displays all headings, not just titles
}
#html_theme = "sphinx_book_theme"
#html_theme = "alabaster"
html_static_path = ['_static']
html_css_files = ['custom.css']
# -- Options for EPUB output
epub_show_urls = 'footnote'

sphinx_tabs_valid_builders = ['linkcheck']
sphinx_tabs_disable_tab_closing = True
