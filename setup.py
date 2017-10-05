import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='django-newsletter-form',
      version='0.1.1',
      description='Simple Django newsletter form for Mailchimp',
      url='http://github.com/b-dev/django-newsletter-form',
      author='Marco Minutoli',
      author_email='info@marcominutoli.it',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'mailchimp3==2.0.17',
      ],
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',  # example license
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          # Replace these appropriately if you are stuck on Python 2.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      zip_safe=False)
