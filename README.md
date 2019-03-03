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
