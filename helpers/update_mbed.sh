#!/usr/bin/env bash


if cd TFLu_benchmark-model_mbed; then
    echo "Updating repository ..."
    git stash
    git fetch
    git merge
else
    echo "Cloning repository ..."
    git clone git@gitlab.ethz.ch:tec/research/tensorflow/projects/ma_leheim/TFLu_benchmark-model_mbed.git
    cd TFLu_benchmark-model_mbed \
    && mbed config root . \
    && mbed deploy
fi
echo "Done."