import io
from setuptools import setup, find_packages

main_ns = {}
exec(open("dash/version.py").read(), main_ns)  # pylint: disable=exec-used


def read_req_file(req_type):
    with open("requires-{}.txt".format(req_type)) as fp:
        requires = (line.strip() for line in fp)
        return [req for req in requires if req and not req.startswith("#")]


setup(
    name="dash",
    version=main_ns["__version__"],
    author="chris p",
    author_email="chris@plot.ly",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    license="MIT",
    description=(
        "A Python framework for building reactive web-apps. "
        "Developed by Plotly."
    ),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=read_req_file("install"),
    extras_require={"ci": read_req_file("ci")},
    entry_points={
        "console_scripts": [
            "dash-generate-components ="
            " dash.development.component_generator:cli"
        ],
        "pytest11": ["dash = dash.testing.plugin"],
    },
    url="https://plot.ly/dash",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Widget Sets",
    ],
)
