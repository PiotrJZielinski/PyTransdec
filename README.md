# PyTransdec

**PyTransdec** is a Python library prepared for controlling [**TransdecEnvironment**](https://github.com/PiotrJZielinski/TransdecEnvironment) by PWr Diving Crew (KN Robocik) at Wrocław University of Science and Technology.

It wraps [Unity ML-Agents library](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents).

The project is maintained by Pwr Diving Crew software team members (Unity3D section).

[KN Robocik website](http://www.robocik.pwr.edu.pl/)

Should any issues be noticed, please submit a **New issue** on GitHub.

## Installation

### Python

To use Python API **Python 3.6** is required. On Windows it is recommended to use Anaconda ([64-bit](https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe) or [32-bit](https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86.exe), but you can use your own preferred Python installation.

For Anaconda use default installation settings. After installation open **Anaconda Navigator** to finish the setup.

![image](https://user-images.githubusercontent.com/23311513/53694120-659c7d80-3daa-11e9-967d-adccde7ca095.png)

In case environment variables were not created, you will see error `conda is not recognized as internal or external command` when you type `conda` into command line. To solve this problem set the environment variables: open `Edit environment variables for your account`, click `Environment Variables` button, then double click `Path under` under `System variable`. Add the following paths using `New` button:

```
%UserProfile%\Anaconda3\Scripts
%UserProfile%\Anaconda3\Scripts\conda.exe
%UserProfile%\Anaconda3
%UserProfile%\Anaconda3\python.exe
```
![image](https://user-images.githubusercontent.com/23311513/53694104-371ea280-3daa-11e9-8351-23eba97e3793.png)

Before proceeding check your installation by executing `python --version`, which should output something like this:

```
Python 3.6.x :: ...
```

You also need **pip** (which is installed by default in Anaconda). Check if it is correctly installed by executing `pip --version`. The output should look like this:

```
pip x.x...
```

If any error occurred, please check your installation.

### PyTransdec package

To use the package install it using pip (it is recommended to use a **virtual environment** such as [**Pipenv**](https://pipenv.readthedocs.io/en/latest/) (preferred), [**conda env**](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [**virtualenv**](https://virtualenv.pypa.io/en/latest/).

Installation command:

```
pip install git+https://github.com/PiotrJZielinski/PyTransdec
```

PyTransdec package automatically installs all required dependencies.
