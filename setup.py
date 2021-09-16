# WQChartPy setup script
#
# Created on...Sep 14, 2021 10:23:05

DESCRIPTION = "Python Package for Visualization of Water Geochemistry Data"
LONG_DESCRIPTION = """\
WQChartPy is an open source python package developed for graphical diagrams 
of water geochemistry data. Utilizing the commonly used Excel XLSX or 
CSV (Comma Separated Value) as the input data format, WQChartPy can produce 
twelve diagrams including not only the traditional Piper diagram, 
Stiff diagram, Durov diagram and Schoeller diagram, but also the recently 
proposed new diagrams such as the rectangle Piper, colored Piper and HFE-D 
that has not implemented in previous software. 

This is the first release of WQChartPy. As a Python-based cross platform 
program, WQChartPy works on Windows, MacOS X and GNU/Linux. We provided a 
self-contained Jupyter notebook file to illustrate how to use WQChartPy. 
Users with a little Python experience can do the whole process from data to 
the graphical diagrams. Buidling on the oldest and most popular Python 
plotting library Matplotlib, the figures generated by WQChartPy can be saved 
as portable network graphics (PNG), scalable vector graphics (SVG) or portable 
document format (PDF). WQChartPy is an open-source project and any
assistance is welcomed. Please email the development team if you want to
contribute.

"""

DISTNAME = 'wqchartpy'
MAINTAINER = 'Jing Yang'
MAINTAINER_EMAIL = 'jingyang@cug.edu.cn'
LICENSE = 'BSD (3-clause)'
VERSION = '0.1.0'
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    'numpy>=1.19.2',
    'pandas>=1.0.3',
    'matplotlib>=3.3.4'
    'scipy>=1.6.2',
    ]

if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 6):
        raise RuntimeError("seaborn requires python >= 3.6.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        version=VERSION,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
    )