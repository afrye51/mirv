# Full installation instructions

1) Start with an Ubuntu 18.04 installation, should be fine live or VM
2) Install ROS Melodic [installation instructions](http://wiki.ros.org/melodic/Installation/Ubuntu)
3) Create a workspace for the mirv project
```
mkdir ~/mirv_ws
cd ~/mirv_ws
mkdir src
catkin_make
echo "source ~/mirv_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
4) Install some dependencies
```
sudo apt install ros-melodic-teleop-twist-joy ros-melodic-joy
```
5) Clone this repo plus some dependencies, then build the workspace
```
git clone https://github.com/afrye51/mirv
git clone https://github.com/ros-simulation/gazebo_ros_pkgs
git clone https://github.com/tu-darmstadt-ros-pkg/hector_gazebo
catkin_make
```
6) Test it out
```
roslaunch mirv_simulation road_slight_curve.launch
```
