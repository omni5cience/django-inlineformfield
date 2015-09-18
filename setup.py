from setuptools import setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='django-inlineformfield',
    version='0.0.1',
    description='Django inline form field.',
    author='Ben Beecher',
    author_email='ben@lightmatter.com',
    url='http://github.com/lightmatter/django-inlineformfield',
    keywords="django",
    packages=['django_inlineformfield', 'django_inlineformfield.forms'],
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ]
)
