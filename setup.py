from setuptools import setup, find_packages
import disk_smart_tool

setup(
    name=disk_smart_tool.name,
    version=disk_smart_tool.__version__,
    description=(
        'Get S.M.A.R.T. of SATA and NVME disks.'
    ),
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='Okeyja',
    author_email='okeyja@abc.xyz',
    maintainer='Okeyja',
    maintainer_email='okeyja@abc.xyz',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/okeyja/disk-smart-tool',
    python_requires=">3.4.0",
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[]
)
