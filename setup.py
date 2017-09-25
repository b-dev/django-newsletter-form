from setuptools import setup

setup(name='django-newsletter-form',
      version='0.1',
      description='Simple Django newsletter form for Mailchimp',
      url='http://github.com/b-dev/django-newsletter-form',
      author='Marco Minutoli',
      author_email='info@marcominutoli.it',
      license='MIT',
      packages=['newsletter_form'],
      install_requires=[
          'mailchimp3==2.0.17',
      ],
      zip_safe=False)
