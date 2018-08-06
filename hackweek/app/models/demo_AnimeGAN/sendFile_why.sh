#!/bin/expect

set timeout 3
set remotePath root@47.106.247.165:/AnimeProject
#set remotePath unique@115.156.207.244:/disk/unique/why/AnimeProject

proc sendFile {path name} {
    spawn scp $name remote $path 
    expect {
        "(yes/no)" { send "yes\r"; exp_continue }
        "password:" { send "23333333\r" }
    }
    interact
}


sendFile $remotePath train_DCGAN.py
sendFile $remotePath model2.py
sendFile $remotePath test.py
sendFile $remotePath model/Gnn-epoch20-lr=0.0002.pkl
#sendFile $remotePath train_DCGAN.py
