import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='django-newsletter-form',
      version='0.1',
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
      zip_safe=False)
