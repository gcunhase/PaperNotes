## My Python Notes

TLDR; Important notes related to Python

### [How to CUDA Python](https://developer.nvidia.com/how-to-cuda-python)
* Install CUDA and [Anaconda](https://repo.continuum.io/archive/)
  ```
    wget https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh
    sudo chmod +x Anaconda2-4.4.0-Linux-x86_64.sh
    ./Anaconda2-4.4.0-Linux-x86_64.sh
  ```
  
* Close and open terminal, then install Accelerate package (includes Numba)
  ```
    conda update conda
    conda install accelerate
    conda install numbapro
  ```
  * In case of error, check [link](https://notgnoshi.github.io/installing-numba-on-ubuntu/)
  * Examples to practice ```git clone git://github.com/numba/numba.git```



