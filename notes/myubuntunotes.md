## My Ubuntu Notes

TLDR; Important notes related to Ubuntu

### [Login Loop Fix](https://askubuntu.com/questions/223501/ubuntu-gets-stuck-in-a-login-loop)
* Log in shell (Ctrl+Alt+[F1 to F6]) and type:
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```
* Search for latest NVIDIA package and install it:
```
sudo apt-cache search nvidia-[0-9]+$
sudo apt install nvidia-[latest package number]
```
* If it suceeds, reboot:
```
sudo reboot
```

### Installing Tensorflow
0. Tensorflow version outside of tensorflow directory:

    ```python -c 'import tensorflow as tf; print(tf.__version__)'```

1. [Install CUDA 7.5](http://www.r-tutor.com/gpu-computing/cuda-installation/cuda7.5-ubuntu)
    ```
    cd ./Desktop/tensorflow/
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb
    sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb
    sudo apt-get update -y
    sudo apt-get install cuda-toolkit-7-5 -y
    ```

  * Check if everything is okay
    ```/usr/local/cuda/bin/nvcc --version```

2. Install cuDNN v5.1 and copy cudnn.h to cuda/include and libcudnn* to cuda/lib64
  * Installing v5.1: Download from [website](https://developer.nvidia.com/rdp/cudnn-download)
    ```
    sudo cp cuda/include/cudnn.h /usr/local/cuda-7.5/include/
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda-7.5/lib64/
    ```

3. Edit bash file
    ```sudo gedit ~/.bashrc```

  * Add at end of file:
    ```
    export PATH=/usr/local/cuda-7.5/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-7.5/lib64
    export CUDA_HOME=/usr/local/cuda-7.5
    ```
    
  * Recompile bash file:
    ```source ~/.bashrc```

4. Install JDLK8, Git and other dependencies
    ```sudo apt-get install -y python-numpy swig python-dev python-wheel python-pip libcurl3-dev libcupti-dev git```

  * Install JDLK 8
    ```
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update -y
    sudo apt-get install oracle-java8-installer
    ```

5. Install [Bazel](bazel.io/docs/install.html)

  * Add Bazel distribution URI as a package source (one time setup)
    ```
    echo "deb http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
    curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo apt-key add -
    ```

  * Update and install Bazel
    ```
    sudo apt-get update && sudo apt-get install bazel
    sudo apt-get upgrade bazel
    ```

  * [Check installation](http://askubuntu.com/questions/87415/how-can-i-find-out-if-a-specific-program-is-installed)
    ```apt-cache policy bazel```

  * [Fix key error](http://askubuntu.com/questions/127326/how-to-fix-missing-gpg-keys)
    ```
    sudo add-apt-repository ppa:webupd8team/y-ppa-manager  
    sudo apt-get update -y 
    ``` 

    * Once you install it start it, then go to advance and select "import all missing GPG keys"


6. Installing Tensorflow 
  * Copy files downloaded using the git command to ```/usr/local/cuda-7.5/```
  
    ```sudo git clone https://github.com/tensorflow/tensorflow```

  * Go to ```/usr/local/cuda-7.5/tensorflow``` and run ```sudo TF_UNNOFICIAL_SETTING=1 ./configure```
    * Chosen settings:
       ```
       /usr/local/lib/python2.7/dist-packages
       /usr/bin/gcc
       7.5
       /usr/local/cuda-7.5
       5.1.10
       /usr/local/cuda-7.5
       Cuda compute capabilities, defaul: "3.5,5.2"
       ```

7. Testing Tensorflow
   * Try import module
   
       ```
       python
       import tensorflow as tf
       ```

   * [Download tensorflow models](https://github.com/tensorflow/models)

   * Try convolutional.py in: ```~/Desktop/tensorflow/models-master/tutorials/image/mnist/convolutional.py```
    ```sudo python convolutional.py```

8. Notes
   * PixelCNN needs CuDNNv5.1
   * CUDA 8.0 required on Ubuntu 16.04
   * If python doesn't work, try ```/usr/bin/python```
