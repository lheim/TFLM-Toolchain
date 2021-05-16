# Measuring what Really Matters: Optimizing Neural Networks for TinyML - Models

This repository contains multiple Jupyter notebooks which were used for the implementation part of the paper *Measuring what Really Matters: Optimizing Neural Networks for TinyML*.
This repository contains the trained models which were evaluated and deployed on microcontrollers:

- LeNet5 on MNIST
- ResNet-20 on CIFAR-10
- Dense layers benchmarking
- Convolutional layers benchmarking
- Depth-wise convolutional layers benchmarking

The models were trained and saved as a Keras file by using TensorFlow.

For the conversion process to `.tflite` see the [toolchain repository](../TFLM-toolchain).


## LeNet

![LeNet](LeNet-MNIST.png)

## ResNet

![ResNet](01d_ResNet20_CIFAR-10.png)

## Dense layers benchmarking

![Dense](A_01ec_DenseBenchmark_varying-input_U-Y.png)

## Convolutional layers benchmarking

![Conv](A_01dg_ConvBenchmark_SingleConv_F-Y_K-3.png)

## Depth-wise convolutional layers benchmarking

![DW Conv](A_01f_Depthwise-Conv_f-1Y_K-3.png)