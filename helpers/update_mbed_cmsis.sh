#!/usr/bin/env bash

if cd TFLu_benchmark-model_mbed_cmsis-nn; then
    echo "Updating mbed cmsis-nn repository ..."
    git stash
    git fetch
    git merge
else
    echo "Cloning mbed cmsis-nn repository ..."
    git clone git@gitlab.ethz.ch:tec/research/tensorflow/projects/ma_leheim/TFLu_benchmark-model_mbed_cmsis-nn.git
    cd TFLu_benchmark-model_mbed_cmsis-nn \
    && mbed config root . \
    && mbed deploy \
    && echo "Patching cmsis-nn ..." \
    && ./patch-cmsis.sh
fi
echo "Done."  