# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
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
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.plantuml',
    'sphinx_tabs.tabs'
    "myst_parser"
]

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
html_static_path = ['_static']
html_css_files = ['custom.css']
# -- Options for EPUB output
epub_show_urls = 'footnote'

plantuml = 'java -jar {}'.format(os.path.join(os.path.dirname(__file__), 'plantuml.jar'))

sphinx_tabs_valid_builders = ['linkcheck']
sphinx_tabs_disable_tab_closing = True
