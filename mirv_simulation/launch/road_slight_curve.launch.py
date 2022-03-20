from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
      DeclareLaunchArgument(
        'initial_x',
        default_value="0.0",
        description='Initial robot x value'
      ),
      DeclareLaunchArgument(
        'initial_y',
        default_value="0.0",
        description='Initial robot y value'
      ),
      DeclareLaunchArgument(
        'initial_z',
        default_value="0.05",
        description='Initial robot z value'
      ),
      DeclareLaunchArgument(
        'initial_yaw',
        default_value="0.0",
        description='Initial robot yaw value'
      ),
      DeclareLaunchArgument(
        'initial_pitch',
        default_value="0.0",
        description='Initial robot pitch value'
      ),
      DeclareLaunchArgument(
        'initial_roll',
        default_value="0.0",
        description='Initial robot roll value'
      ),
  <node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher">
      <param name="publish_frequency" type="double" value="50.0"/>
    <param name="robot_description" value="robot_description"/>
  </node>

        Node(
            package='robot_state_publisher',
            namespace='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[]
        )
    ])

<launch>
  <arg name="initial_x" default="0.0"/>
  <arg name="initial_y" default="0.0"/>
  <arg name="initial_z" default="0.05"/>
  <arg name="initial_yaw" default="0.0"/>
  <arg name="initial_pitch" default="0.0"/>
  <arg name="initial_roll" default="0.0"/>

  <!-- Launch gazebo world -->
  <arg name="debug" default="false" />
  <arg name="gui" default="true" />
  <arg name="pause" default="false" />
  <arg name="world" default="$(find mirv_simulation)/world/road_slight_curve.world" />
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(arg world)" />
    <arg name="debug" value="$(arg debug)" />
    <arg name="gui" value="$(arg gui)" />
    <arg name="paused" value="$(arg pause)" />
    <arg name="use_sim_time" value="true" />
  </include>

  <!-- Start RViz for visualization -->
  <node type="rviz" name="rviz" pkg="rviz" args="-d $(find mirv_simulation)/rviz/mirv_sensors.rviz" />

  <param name="robot_description" command="$(find xacro)/xacro $(find mirv_description)/urdf/mirv_gazebo.urdf.xacro" />

  <node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher">
      <param name="publish_frequency" type="double" value="50.0"/>
    <param name="robot_description" value="robot_description"/>
  </node>

  <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher">
    <param name="rate" type="double" value="50.0"/>
  </node>

  <node name="spawn_urdf" pkg="gazebo_ros" type="spawn_model" args="-urdf -model mirv -x $(arg initial_x) -y $(arg initial_y) -z $(arg initial_z) -Y $(arg initial_yaw) -param robot_description" output="screen"/>
</launch>
