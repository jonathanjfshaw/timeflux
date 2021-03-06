#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Timeflux documentation build configuration file
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from timeflux import __version__
from sphinx.util import logging
logger = logging.getLogger(__name__)


# -- Auto-generate API documentation --------------------------------------

api_packages = ['timeflux', 'timeflux_example', 'timeflux_dsp', 'timeflux_ml', 'timeflux_ui', 'timeflux_bci', 'timeflux_openbci', 'timeflux_brainflow', 'timeflux_gazepoint', 'timeflux_bitalino', 'timeflux_amti', 'timeflux_pl4']
#api_packages += ['timeflux_nexus', 'timeflux_eego']
api_path = 'api'

def run_apidoc(_):
    from sphinx.ext.apidoc import main
    from importlib.util import find_spec
    for package in api_packages:
        try:
            module_path = find_spec(package).submodule_search_locations[0]
            main(['--tocfile', 'modules_' + package, '--separate', '--force', '--module-first', '--implicit-namespaces', '-o', api_path, module_path])
        except:
            logger.warning('Package %s not found.' % package)


# -- Setup-----------------------------------------------------------------

def setup(app):
    #app.add_js_file('https://www.googletagmanager.com/gtag/js?id=UA-25274760-3', async='async')
    app.add_js_file('https://www.googletagmanager.com/gtag/js?id=UA-25274760-3') # kwargs broken?
    app.add_js_file('js/ga.js')
    #app.add_js_file('js/ui.js')
    app.connect('builder-inited', run_apidoc)

rst_prolog = """
.. |br| raw:: html

   <br>
"""


# -- General configuration ------------------------------------------------

needs_sphinx = '1.8'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax'
]

# Autodoc settings
# Sphinx 1.8
autodoc_default_options = {
    'special-members': '__init__',
    'member-order': 'bysource'
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_ivar = True

source_suffix = ['.rst', '.md']

master_doc = 'index'

# General information about the project.
project = 'Timeflux'
copyright = '2018-2019, Pierre Clisson and the Timeflux community'
author = 'Pierre Clisson'

# The short X.Y version.
version = __version__

# The full version, including alpha/beta/rc tags.
release = __version__

language = None
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True

html_static_path = ['static']


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    # 'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
    'display_version': True,  # Display the docs version
    # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}
html_logo = 'static/img/logo.png'


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'timeflux_doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
      \usepackage{hyperref}
      \setcounter{tocdepth}{3}
    '''

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Timeflux.tex', 'Timeflux Documentation', '', 'manual', False),
]

#latex_use_parts = False


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'timeflux', 'Timeflux Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Timeflux', 'Timeflux Documentation',
     author, 'Timeflux', '', ''),
]

