#!/bin/bash

git submodule init
git submodule update

cd ui_app/ai/MNIST_pytorch
git submodule init
git submodule update