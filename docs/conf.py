# Configuration file for the Sphinx documentation builder.

# -- Project information

# project = 'Manual de Suplementador Inteligente'
project = 'Manual-Suplementador-Inteligente'
copyright = '2022, Suplementar SAS.'
author = 'Suplementar SAS'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
#    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for internationalization
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
gettext_uuid = True

figure_language_filename = '{root}.{language}{ext}'

import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
