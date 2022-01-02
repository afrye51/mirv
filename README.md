# Summary
ROS files for the MIRV project

# Installation
This code is written for ROS 1 Noetic running on Ubuntu 20.04. 

Clone this repository into an existing ros workspace, or create a new one. 
Also clone the dependencies: gazebo_ros_pkgs hector_gazebo: 

```
git clone https://github.com/afrye51/mirv
git clone https://github.com/ros-simulation/gazebo_ros_pkgs
git clone https://github.com/tu-darmstadt-ros-pkg/hector_gazebo
```
# Usage
Currently the only launch file is road_slight_curve.launch in mirv_simulation, which launches the vehicle with sensors on a road in gazebo. 

