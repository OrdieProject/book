# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ordie: The Primordial Microcontroller'
copyright = '2022, Sean "xobs" Cross'
author = 'Sean "xobs" Cross'
html_baseurl = 'https://black-magic.org'
language  = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.napoleon',
    'sphinxcontrib.platformpicker',
    'sphinxcontrib.asciinema',
    'sphinxcontrib.youtube',
    'sphinx-favicon',
    'sphinxext.opengraph',
    'ablog',
    'guzzle_sphinx_theme',
]

source_suffix = {
	'.rst': 'restructuredtext',
	'.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
import guzzle_sphinx_theme

html_theme = 'guzzle_sphinx_theme'
html_static_path = ['_static']
html_theme_path = guzzle_sphinx_theme.html_theme_path()

html_theme_options = {
    "project_nav_name": "Ordie",
    "base_url": "https://book.ordie.dev/",
    "projectlink": "https://ordie.dev/",
}
