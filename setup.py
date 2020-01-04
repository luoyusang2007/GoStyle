from setuptools import setup, find_packages

with open('README.md') as fp:
    readme = fp.read()

setup(
    # 以下为必需参数
    name='gostyle',  # 模块名
    version='0.1.4',  # 当前版本
    description='Golang Syntax For Python',  # 简短描述
    # py_modules=["my_module"], # 单文件模块写法
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法
    packages=find_packages("gostyle"),

    # 以下均为可选参数
    long_description=readme,# 长描述
    long_description_content_type='text/markdown',
    url='https://github.com/luoyusang2007/gostyle', # 主页链接
    author='Luo Yusang', # 作者名
    author_email='luoyusang2007@hotmail.com', # 作者邮箱
    classifiers=[
    #    'Development Status :: 3 - Alpha',  # 当前开发进度等级（测试版，正式版等）
    #    'Intended Audience :: Developers', # 模块适用人群
    #    'Topic :: Software Development :: Build Tools', # 给模块加话题标签
    #    'License :: OSI Approved :: MIT License', # 模块的license

    #    'Programming Language :: Python :: 2', # 模块支持的Python版本
    #    'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='go golang routine thread',  # 模块的关键词，使用空格分割
    # install_requires=['peppercorn'], # 依赖模块
    # extras_require={  # 分组依赖模块，可使用pip install sampleproject[dev] 安装分组内的依赖
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    # package_data={  # 模块所需的额外文件
    #     'sample': ['package_data.dat'],
    # },
    # data_files=[('my_data', ['data/data_file'])], # 类似package_data, 但指定不在当前包目录下的文件
    # entry_points={  # 新建终端命令并链接到模块函数
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
    project_urls={  # 项目相关的额外链接
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/luoyusang2007/gostyle',
    }
)   
