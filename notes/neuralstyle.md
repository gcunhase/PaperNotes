## [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
Leon A. Gatys, Alexander S. Ecker and Matthias Bethge, Submitted on 26 Aug 2015

TLDR; The authors introduce an artificial system based on a Deep Neural Network (namely CNN) that creates artistic images of high perceptual quality by combining the content of an image and the style of another.

### Key Points
* Model: CNN obtains feature representations from both images and the weights are combined to get the generated image
* Content representation: extracted in higher layers of the network
* Style representation: a feature space originally designed to capture texture information is used, computes correlations between the different features in different layers of the CNN
* VGG-Network: "CNN that rivals human performance on a common visual object recognition benchmark task"

### Notes / Questions
* "[...] used the feature space provided by the 16 convolutional and 5 pooling layers of the 19 layer VGGNetwork"

### Results

* Code1: [anishathalye's neural-style](https://github.com/anishathalye/neural-style)

 ```
  python neural_style.py --content <content file> --styles <style file> --output <output file> --network <pre-trained vgg network>
  python neural_style.py --content examples/2-content.jpg --styles examples/2-style2.jpg --output examples/test.jpg --network imagenet-vgg-verydeep-19.mat
 ```

<p align="center">
 <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/neuralstyle_content.jpg" height="150" alt="Content"> +
 <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/neuralstyle_style.jpg" height="150" alt="Style"> = 
 <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/neuralstyle_output.jpg" height="150" alt="Output">
</p>

  * *--style-layer-weight-exp 0.05*
<p align="center">
 <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/neuralstyle_output2.jpg" height="150" alt="Output">
</p>
  


* Code2: [andersbll's neural_artistic_style](https://github.com/andersbll/neural_artistic_style)
  * [Installation steps](http://blog.josephmisiti.com/making-neural-art)
 
 
* [code3](https://github.com/cysmith/neural-style-tf), [code4](https://github.com/lengstrom/fast-style-transfer)


