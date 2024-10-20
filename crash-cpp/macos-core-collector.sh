#!/bin/bash

ls -la /cores/*

for f in /cores/*
do
    echo "Processing $f..."
    lldb -c $f --one-line "bt all" --one-line "frame variable" --batch
done