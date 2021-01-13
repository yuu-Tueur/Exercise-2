# Exercise-2
 ロボットシステム学の課題２です
 
 このリポジトリーは講義内で作成したものに改良を加えて作成しました
 
 信号機っぽいものを作りました
# 動作環境
　OS:Ubuntu 18.04.5 LTS
 
　ROS Distribution: Melodic Morenia 1.14.3
 
　python 2.7.17
 
# 環境構築
1.本パッケージのインストールを行います

※このパッケージはワークスペースがある前提です

```
cd ~/catkin_ws/src
git clone https://github.com/yuu-Tueur/Exercise-2.git
cd ~/catkin_ws
catkin_make

```

# 実行方法
```
roscore &
cd ~/catkin_ws/src/Exercise-2/scripts
chmod +x traffic_light.py
rosrun Exercise-2 traffic_light.py 
```

# 実践動画
下のURLから見ることができます

<https://youtu.be/BJxbhjLeAko>

# ライセンス
This repository is licensed BSD 3-Clause License
