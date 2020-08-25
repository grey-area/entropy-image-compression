#!/bin/bash

rm -f out.mp4
for dir in frames side_frames combined_frames; do
    mkdir -p $dir
    rm -f $dir/*
done

printf "Producing point cloud frames\n\n"
python make_pointcloud.py

printf "\nComputing file sizes and plotting\n\n"
python make_filesize_plot.py

printf "\nCombining frames\n\n\n"

total="$(ls -1 frames | wc -l)"
for f in $(ls -1 frames); do
    echo -e "\e[1A\e[K$f of $total\r"
    convert +append frames/$f side_frames/$f combined_frames/$f
done

printf "\nProducing video\n"

ffmpeg -framerate 30 -i combined_frames/%04d.png -c:v libx264 -r 30 -pix_fmt yuv420p -b:v 5M out.mp4