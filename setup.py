from setuptools import setup, find_packages

setup(
    name="performance-predictor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow==2.15.0",
        "numpy==1.24.3",
        "pandas==2.1.4",
        "scikit-learn==1.3.2",
        "flask==3.0.0",
        "plotly==5.18.0",
        "python-dotenv==1.0.0",
        "gunicorn==21.2.0"
    ],
    author="Vaibhav Khandelwal",
    author_email="vaibhav.dev.arch@gmail.com",
    description="A performance prediction application using machine learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vaibhav-dev-arch/aiops",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 