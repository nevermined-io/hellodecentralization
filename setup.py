from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = [
    "nevermined-sdk-py==0.8.0",
    "jupyter~=1.0.0",
    "jupyterlab~=2.2.9",
    "xain-sdk==0.8.0",
    "pytest~=6.2.2",
    "papermill~=2.3.2"
]

setup(
    author="nevermined-io",
    author_email="root@nevermined.io",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    description="🐳 Nevermined Hellodecentralization Workshop.",
    install_requires=install_requirements,
    packages=find_packages(exclude=['tests*']),
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="nevermined hellodecentralization workshop",
    name="workshop",
    url="https://github.com/nevermined-io/hellodecentralization",
    version="0.1.0",
    zip_safe=False,
)
