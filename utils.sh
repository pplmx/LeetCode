#!/usr/bin/env bash

function build_ssh_trust() {
    local i=$1
    if [[ ${i} == 10 ]];then
        echo 2
    fi
    echo 1
    `cd ~ || exit`
    while read line; do
        echo ${line}
    done
}

build_ssh_trust 3