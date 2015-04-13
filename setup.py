#!/usr/bin/env python

import os
import glob

from setuptools import setup, Command


class BuildNotes(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        import os
        import shutil
        import tempfile

        from IPython.nbconvert.nbconvertapp import NbConvertApp

        import sys
        for arg in range(len(sys.argv[1:])):
            sys.argv.pop(-1)

        # First convert the lecture notes to slides - we have to do them
        # individually in order to be able to specify a custom output prefix for
        # each.

        app = NbConvertApp()
        app.initialize()
        app.export_format = 'slides'
        app.config.Exporter.template_file = 'config/slides.tpl'
        for notebook in glob.glob('lectures/*.ipynb'):
            app.notebooks = [notebook]
            app.output_base = notebook.replace('.ipynb', '')
            app.start()

        # Now convert the lecture notes, problem sets, and practice problems to
        # HTML notebooks.

        app = NbConvertApp()
        app.initialize()
        app.export_format = 'html'
        for notebook in glob.glob('lectures/*.ipynb'):
            app.notebooks = [notebook]
            app.output_base = notebook.replace('.ipynb', '')
            app.start()


setup(name='python-course', cmdclass={'build': BuildNotes})
