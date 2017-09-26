## My Python Notes

TLDR; Important notes related to Python

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

### Using GPU

#### [PyTorch](http://pytorch.org/tutorials/beginner/pytorch_with_examples.html)
Basically same as numpy but with GPU compatibility.
* Install dependencies
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

