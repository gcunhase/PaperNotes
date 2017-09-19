## My Python Notes

TLDR; Important notes related to Python

### [How to CUDA Python](https://developer.nvidia.com/how-to-cuda-python)
* Install CUDA and [Anaconda](https://repo.continuum.io/archive/)
   * Python 3.6
  ```
    wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh
  ```

   * Python 2.7

  ```
    wget https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh
    sudo chmod +x file.sh
    ./file.sh
  ```
  
* Close and open terminal, then install Accelerate package (includes Numba)
  ```
    conda update conda
    conda update --all
    conda install accelerate
  ```
  * In case of error, check [link](https://notgnoshi.github.io/installing-numba-on-ubuntu/)
  * Examples to practice ```git clone git://github.com/numba/numba.git```

* Numbapro needs python 3.5

  ```
    conda create -n py35 python=3.5 anaconda
    source activate py35
    #conda install -c menpo opencv3
    conda install -c conda-forge numbapro
    source deactivate
  ```

  * If error:
    ```
      conda clean --packages
    ```
