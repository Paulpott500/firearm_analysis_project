from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="firearm_analysis_project",  # Replace with your project name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A project to analyze firearm background checks in the United States.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" github link",  # Replace with your project URL
    packages=find_packages(),  # Automatically find packages in the current directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.0",
        "matplotlib>=3.0",
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'firearm_analysis=main:main',  # This allows you to run `firearm_analysis` in terminal
        ],
    },
)
