# MIRV

## Summary
ROS files for the MIRV project

## Quick notes
Similar projects to gain insight from: 
- [ClearPath Jackal](https://github.com/jackal/jackal)
- [ROBOTIS Turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3) and [simulations](https://github.com/ROBOTIS-GIT/turtlebot3_simulations)

## Installation
Check out the instructions [here](installation_instructions.md)

## Usage
Currently the only launch file is road_slight_curve.launch in mirv_simulation, which launches the vehicle with sensors on a road in gazebo. 

## Folder Structure
recommended folder structure:
- mirv (metapackage)
  - mirv_control (real world/simulation-agnostic nodes)
  - mirv_real (real-world sensor drivers/calibration)
  - mirv_description (simulation meshes/sensor plugins/robot description,  just robot specifics. If someone else wanted to use the robot for a different task, they would want these files)
  - mirv_simulation (simulation launch files/worlds)

optional other packages:
  - mirv_msgs (any custom messages that we define)
  - mirv_tutorials (tutorials for using the rover/simulator)
  - mirv_documentation
