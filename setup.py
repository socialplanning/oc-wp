from setuptools import setup, find_packages

version = '0.3'

long_description = "Changes:\n\n%s" % open('CHANGES.txt').read()

setup(name='oc-wp',
      version=version,
      description="opencore wordpress client package",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='The OpenCore community',
      author_email='opencore-dev@lists.coactivate.org',
      url='http://coactivate.org/projects/opencore',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['opencore'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [opencore.versions]
      oc-wp = opencore.wordpress
      [topp.zcmlloader]
      opencore = opencore.wordpress
      """,
      )
