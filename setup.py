from distutils.core import setup

import comgate

setup(
    name='django_comgate',
    version=comgate.__version_str__,
    packages=['comgate', 'comgate.migrations', ],
    url='',
    license='BSD',
    author='MTProduction s.r.o.',
    author_email='jakub.skaryd@mtproduction.cz',
    description='An interface for ComGate payment gateway'
)
