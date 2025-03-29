from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    """
    This function reads the requirements file and returns a list of dependencies.
    """
    with open(file_path, "r") as f:
        requirements = f.readlines()
    
    # Strip newlines and spaces
    requirements = [req.strip() for req in requirements]

    # Remove '-e .' if present
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Pratham",
    author_email="dumppp.00001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
