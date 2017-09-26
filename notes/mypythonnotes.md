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

### [Using GPU]

#### [PyTorch](http://pytorch.org/tutorials/beginner/pytorch_with_examples.html)

#### [With Tensorflow](https://github.com/gcunhase/PaperNotes/blob/master/notes/python_tf_gpu.py)
<table>
 <tr>
   <td colspan="2" align="center"><b>powers</b> (secs)</td><td colspan="2" align="center"><b>matmul</b> (secs)</td>
 </tr>
 <tr>
  <td align="center">CPU</td><td align="center">GPU</td><td align="center">CPU</td><td align="center">GPU</td>
 </tr>
 <tr>
  <td align="center">1.04</td><td align="center">0.654</td><td align="center">0.40</td><td align="center">0.013</td>
 </tr>
</table>


#### [PyCUDA](https://developer.nvidia.com/how-to-cuda-python)
* In case of error, check [link](https://notgnoshi.github.io/installing-numba-on-ubuntu/)
* Examples to practice ```git clone git://github.com/numba/numba.git```
* [Intro to Python GPU programming with Numba](https://github.com/ContinuumIO/numbapro-examples/blob/master/webinars/2014_06_17/intro_to_gpu_python.ipynb)

