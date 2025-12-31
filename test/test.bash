#!/bin/bash

# ROS 2 ワークスペースのセットアップ
source ~/ros2_ws/install/setup.bash

# clock.py ノードをバックグラウンドで起動
ros2 run mypkg_2 clock &
NODE_PID=$!

# ノードが起動するのを少し待つ
sleep 3

# ノードがまだ生きているか確認
if ps -p $NODE_PID > /dev/null
then
   echo "OK"
else
   echo "NO"
fi

# ノードを終了
kill $NODE_PID
