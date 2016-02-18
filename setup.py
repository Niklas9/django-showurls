
import setuptools


setuptools.setup(
    name='django-showurls',
    version='1.0.0',
    author='Niklas Andersson',
    author_email='nandersson900@gmail.com',
    description='Adds a mgmt command to print urls from your Django project',
    url='https://github.com/Niklas9/django-showurls',
    zip_safe=False,
    install_requires=[
        'django',
    ],
    tests_require=[
    ],
    packages=setuptools.find_packages(),
    #test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
