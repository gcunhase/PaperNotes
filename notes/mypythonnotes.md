## My Python Notes

TLDR; Important notes related to Python

### [How to submit package to PyPI](http://peterdowns.com/posts/first-time-with-pypi.html)

### [Pipenv and Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### TextBlob
* [Github source](http://textblob.readthedocs.io/en/dev/index.html)

### Good practice
1. [Proper structure](https://airbrake.io/blog/python/python-best-practices)
    * *root*: License, README, setupy.py, requirements.txt
    * */module*: Module Code (*root* for just 1 file)
    * */docs*: Documentation
    * */tests*: Tests

2. [Naming](https://gist.github.com/sloria/7001839#naming)

3. [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Timing a program
```python
from timeit import default_timer as timer
start = timer()
print("Program ran for: "+str((timer()-start)/60)+" minutes")
```

### Installing pydub and tqdm
```
pip install git+https://github.com/jiaaro/pydub.git@master
pip install -e git+https://github.com/tqdm/tqdm.git@master#egg=tqdm
from tqdm import tqdm
```

### [PyCharm](https://itsfoss.com/install-pycharm-ubuntu/)
* PyCharm Pro version is now available in Ubuntu Software Center in Ubuntu 16.04. So you can just install it from there.
* If not available,
  ```
  sudo add-apt-repository ppa:mystic-mirage/pycharm
  sudo apt-get update
  ```

    * To download the community edition of PyCharm:
    ```
    sudo apt-get install pycharm-community
    ```

    * To download the professional edition of PyCharm:
    ```
    sudo apt-get install pycharm
    ```
   
    
### [Anaconda](https://www.anaconda.com/download/)
```
wget https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh
sudo chmod +x Anaconda2-4.4.0-Linux-x86_64.sh
./Anaconda2-4.4.0-Linux-x86_64.sh
conda install anaconda-navigator
```

Environments (Example: create environment with Python 3 and list existing environments)
```
conda create --name my_env python=3
source activate my_env
source deactivate
conda info --envs
```

### [Spark](https://spark.apache.org/examples.html) for faster code
```
pip install pyspark
```

* About: "Spark is built on the concept of *distributed datasets*, which contain arbitrary Java or Python objects. You create a dataset from external data, then apply parallel operations to it. The building block of the Spark API is its RDD API. In the RDD API, there are two types of operations: *transformations*, which define a new dataset based on previous ones, and *actions*, which kick off a job to execute on a cluster."

* Example: [Scrapping wikidate with spark](https://github.com/n4group/tf-idf-python-spark-tutorial), [Other examples](https://github.com/apache/spark/tree/master/examples/src/main/python)

### Using GPU

#### [PyTorch](http://pytorch.org/)
Basically same as numpy but with GPU compatibility.
1. Pip install
```
sudo pip install http://download.pytorch.org/whl/cu91/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl
sudo pip install torchvision 
```

2. [Install dependencies](http://pytorch.org/tutorials/beginner/pytorch_with_examples.html)
```
export CMAKE_PREFIX_PATH="$(dirname $(which conda))/../" # [anaconda root directory]

# Install basic dependencies
conda install numpy pyyaml mkl setuptools cmake gcc cffi

# Add LAPACK support for the GPU
conda install -c soumith magma-cuda80 # or magma-cuda75 if CUDA 7.5
```

   * Install Torch
   ```
   git clone --recursive https://github.com/pytorch/pytorch
   python setup.py install
   reboot
   ```

* Example powers

| n | CPU (secs) | GPU (secs) |
|:--:|:--:|:--:|
| 50 | 0.0034 | 2.28 |
| 500 | 0.36 | 4.96 |
| 5,000 | 31.78 | 28.16 |
| 50,000 | not enough mem | not enough mem |


#### [With Tensorflow](https://github.com/gcunhase/PaperNotes/blob/master/notes/python_tf_gpu.py)
<table>
 <tr>
   <td colspan="2" align="center"><b>powers</b> (secs)<p>n = 5,000,000</p></td><td colspan="2" align="center"><b>matmul</b> (secs)</td><td colspan="2" align="center"><b>powers_func</b> (secs)</td>
 </tr>
 <tr>
  <td align="center">CPU</td><td align="center">GPU</td><td align="center">CPU</td><td align="center">GPU</td><td align="center">CPU</td><td align="center">GPU</td>
 </tr>
 <tr>
  <td align="center">1.04</td><td align="center">0.654</td><td align="center">0.40</td><td align="center">0.013</td><td align="center">killed</td><td align="center">killed</td>
 </tr>
</table>


#### [PyCUDA](https://developer.nvidia.com/how-to-cuda-python)
* In case of error, check [link](https://notgnoshi.github.io/installing-numba-on-ubuntu/)
* Examples to practice ```git clone git://github.com/numba/numba.git```
* [Intro to Python GPU programming with Numba](https://github.com/ContinuumIO/numbapro-examples/blob/master/webinars/2014_06_17/intro_to_gpu_python.ipynb)

### Running Python on Matlab in Ubuntu
```
[own_path, ~, ~] = fileparts(mfilename('../LSTM-Neural-Network-for-Time-Series-Prediction/'));
module_path = fullfile(own_path, '..');
python_path = py.sys.path;
if count(python_path, module_path) == 0
    insert(python_path, int32(0), module_path);
end
py.helloworld.main();
```

### [Running Python codes on Matlab](http://adared.ch/matpy/)
* On Matlab, make it see Xcode: [first try](https://kr.mathworks.com/matlabcentral/answers/246507-why-can-t-mex-find-a-supported-compiler-in-matlab-r2015b-after-i-upgraded-to-xcode-7-0), if it doesn't work, [try this](https://bitbucket.org/d2d-development/d2d-software/issues/46/xcode-7-on-osx-with-matlab-r2015a-b). Add the following lines in all *.xml* files in */Applications/MATLAB_R2015b.app/bin/maci64/mexopts/*
```
<dirExists name="$$/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk" />
<cmdReturns name="find $$ -name MacOSX10.13.sdk" />
```

* Install Python and check existence of file */System/Library/Frameworks/Python.framework/Headers/Python.h*
```
brew install python
```
  * Python is a framework on Mac OS X so you need to, 
  ```
  #include <Python/Python.h>
  ```
  
* On Matlab, run:
```
mex -setup
mex py.cpp -lpython
```

* Run
  * Example 1
```
stmt = sprintf(['print(2)']);
py('eval', stmt);
```

  * Example 2: SIP not working
```
[X,Y]=meshgrid(-10:0.1:10,-10:0.1:10);
Z=sin(X)+cos(Y);
py_export('X','Y','Z')
stmt = sprintf(['import matplotlib\n' ...
'matplotlib.use(''Qt4Agg'')\n' ...
'import matplotlib.pyplot as plt\n' ...
'from mpl_toolkits.mplot3d import axes3d\n' ...
'f=plt.figure()\n' ...
'ax=f.gca(projection=''3d'')\n' ...
'cset=ax.plot_surface(X,Y,Z)\n' ...
'ax.clabel(cset,fontsize=9,inline=1)\n' ...
'plt.show()']);
py('eval', stmt);
```

### From Python2.7 to 3.5
* *TypeError: object of type 'zip' has no len()*
   * "In Python 2 using shuffle after zip works, because zip returns a list, whilst in Python 3 it returns an iterator.
   * [Solution](https://stackoverflow.com/questions/18048310/len-error-for-zipping-in-python), use list() to convert to a list:
    ```
    combined = list(zip(question, answer))
    random.shuffle(combined)
    ```
    
### Tensorboard on Tensorflow

* [On server](https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server)
  ```
  ssh -L 16006:127.0.0.1:6006 olivier@my_server_ip
  tensorboard --logdir=path/to/log-or-train-directory
  ```
  On local machine, go to http://127.0.0.1:16006 to access the remote TensorBoard

* On server (already sshed)
  ```
  tensorboard --port=8900 --logdir=path/to/log-or-train-directory
  ```
  On local machine: https://ip_address:port (port = 8900, 9000)

* On local machine: http://0.0.0.0:6006/#scalars
