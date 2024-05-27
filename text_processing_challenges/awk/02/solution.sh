#!/usr/bin/env bash
awk 'ORS=NR%2?";":"\n"' sample_input.txt
