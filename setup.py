"""
Flask-Squeeze
-------------

Automatically minify JS/CSS and crompress all responses with brotli, with caching for static assets.
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Flask-Authorization",
    version="1.3",
    url="https://github.com/mkrd/flask-authorization",
    license="MIT License",
    author="Marcel Kröker",
    author_email="kroeker.marcel@gmail.com",
    description="Simple user authorization to use alongside with Flask-Login",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["flask_authorization"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[  
        "flask",
        "flask-login"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)