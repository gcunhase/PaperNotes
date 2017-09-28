## My Ubuntu Notes

TLDR; Important notes related to Ubuntu

### Which Ubuntu
```
lsb_release -a
```

### Find files
   ```find ~/ -type f -name [filename]```

### Tar
* Compress
   ```tar -zcvf archive_name.tar.gz folder_to_compress```

* Extract
   ```tar -zxvf archive_name.tar.gz```

### Recording a log file
* Type the following to store all input and output in the terminal in *screen.log*: ```script screen.log```

* To stop the script: ```exit```

### Selecting a GPU to use
* Check available GPUs: ```nvidia-smi```

* Select GPU id 0: ```sudo CUDA_VISIBLE_DEVICES=0 python script.py```

### Server ssh error
* *WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!*
    * Remove that entry from known_hosts using the following command then try again:
    
         ```ssh-keygen -R *ip_address_or_hostname*```

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

### Installing Tensorflow (0.10.0)
0. Tensorflow version outside of tensorflow directory (my computer and IBM's Minsky server respectively):

    ```
    python -c 'import tensorflow as tf; print(tf.__version__)'
    python -c 'import sys; sys.path.insert(0, "/opt/DL/tensorflow/lib/python2.7/site-packages"); import tensorflow as tf; print(tf.__version__)'
    ```

1. Install CUDA

    * [CUDA 7.5](http://www.r-tutor.com/gpu-computing/cuda-installation/cuda7.5-ubuntu)
    ```
    cd ~/Desktop/tensorflow/
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb
    sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb
    sudo apt-get update -y
    sudo apt-get install cuda-toolkit-7-5 -y
    ```

    * [CUDA 8.0](https://developer.nvidia.com/cuda-downloads)
    ```
    cd ~/Desktop/tensorflow/
    wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb
    mv cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
    sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
    sudo apt-get update
    sudo apt-get install cuda
    ```

    * Check if everything is okay
  
    ```/usr/local/cuda/bin/nvcc --version```

    * Test CUDA
    ```
    cd /usr/local/cuda-8.0/samples/5_Simulations/nbody
    sudo make
    ./nbody
    ```

2. Install cuDNN v5.1 or 6.0.21 ([download](https://developer.nvidia.com/rdp/cudnn-download)) and copy cudnn.h to cuda/include and libcudnn* to cuda/lib64
  
    ```
    sudo cp cuda/include/cudnn.h /usr/local/cuda-8.0/include/
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda-8.0/lib64/
    sudo chmod a+r /usr/local/cuda-8.0/include/cudnn.h /usr/local/cuda-8.0/lib64/libcudnn*
    ```

3. Edit bash file

    ```sudo gedit ~/.bashrc```

    * Add at end of file:
  
    ```
    export PATH=/usr/local/cuda-8.0/bin:$HOME/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
    export CUDA_HOME=/usr/local/cuda-8.0
    ```
    
    * Recompile bash file:
  
    ```source ~/.bashrc```

4. Install JDLK8, Git and other dependencies (**NOT NECESSARY** if you want to install most current version)

    ```sudo apt-get install -y python-numpy swig python-dev python-wheel python-pip libcurl3-dev libcupti-dev git```

    * Install JDLK 8
  
    ```
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update -y
    sudo apt-get install oracle-java8-installer
    ```

5. Install [Bazel](bazel.io/docs/install.html) (**NOT NECESSARY** if you want to install most current version)

    * Add Bazel distribution URI as a package source (one time setup)
    ```
    echo "deb http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
    curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo apt-key add -
    ```

    * Update and install Bazel 0.5.2 (error on 0.5.3)
    ```
    sudo apt-get update
    wget https://github.com/bazelbuild/bazel/releases/download/0.5.2/bazel-0.5.2-installer-linux-x86_64.sh
    sudo chmod +x bazel-0.5.2-installer-linux-x86_64.sh
    sudo ./bazel-0.5.2-installer-linux-x86_64.sh
    ```

    * [Check installation](http://askubuntu.com/questions/87415/how-can-i-find-out-if-a-specific-program-is-installed)
    ```
    sudo bazel version
    apt-cache policy bazel
    ```

    * [Fix key error](http://askubuntu.com/questions/127326/how-to-fix-missing-gpg-keys)
    ```
    sudo add-apt-repository ppa:webupd8team/y-ppa-manager  
    sudo apt-get update -y 
    ``` 

      * Once you install it start it, then go to advance and select "import all missing GPG keys"


6. Installing Tensorflow

    * First try running: ```pip install tensorflow-gpu``` (**THIS MIGHT BE THE ONLY NECESSARY THING**)

    * Copy files downloaded using the git command to ```/usr/local/cuda-8.0/```
  
    ```sudo git clone https://github.com/tensorflow/tensorflow```

    * Go to ```/usr/local/cuda-8.0/tensorflow``` and run ```sudo TF_UNNOFICIAL_SETTING=1 ./configure```
        * Chosen settings:
       ```
       /usr/local/lib/python2.7/dist-packages
       /usr/bin/gcc
       8.0
       /usr/local/cuda-8.0
       5.1.10 or 6.0.21
       /usr/local/cuda-8.0
       Cuda compute capabilities, defaul: "3.5,5.2"
       ```
    
    * Build target with GPU Support using Bazel
    
    ```
    sudo bazel build -c opt //tensorflow/tools/pip_package:build_pip_package
    sudo bazel build -c opt --config=cuda-8.0 //tensorflow/tools/pip_package:build_pip_package
    bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
    sudo pip install /tmp/tensorflow_pkg/tensorflow-NAME.whl
    ```

7. Testing Tensorflow
    * Try import module
   
       ```
       python
       import tensorflow as tf
       ```

    * [Download tensorflow models](https://github.com/tensorflow/models)

    * Try *convolutional.py*:
    
        ```
        cd ~/Desktop/tensorflow/models-master/tutorials/image/mnist/convolutional.py
        sudo python convolutional.py
        ```

8. Notes
   * PixelCNN needs CuDNNv5.1
   * CUDA 8.0 required on Ubuntu 16.04
   * If python doesn't work, try ```/usr/bin/python```
   * Good [tutorial](http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html)
   * All versions of Tensorflow's [source code](https://github.com/tensorflow/tensorflow/releases)
   * All versions of Tensorflow's install link:
      ```
      curl -s https://storage.googleapis.com/tensorflow |xmllint --format - |grep whl
      ```
   
   * Installing Tensorflow 1.2
   
      * Needs CUDA 8.0 and Cudnn 6 (6.0.21)
        
      * In step 6, in *Build target with GPU Support using Bazel*, switch the last two commands with:
        
      ```python
      cd /tmp/tensorflow-pkg/; wget https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.2.1-cp27-none-linux_x86_64.whl
      sudo pip install --ignore-installed --upgrade /tmp/tensorflow-pkg/tensorflow_gpu-1.2.1-cp27-none-linux_x86_64.whl
      ```
            
### Installing [Keras](https://keras.io/)
```sudo pip install keras```

* For Seq2Seq models using keras: [link](https://github.com/farizrahman4u/seq2seq)
* Other [keras examples](https://github.com/fchollet/keras)

### [Installing tflearn](https://github.com/tflearn/tflearn) (Keras optimized for Tensorflow)
```
python setup.py install
```
