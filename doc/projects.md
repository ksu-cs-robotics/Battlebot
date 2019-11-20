<p align="center">
  <a href="" rel="noopener">
 <img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/ATR-logo.gif" alt="ATR"></a>
</p>

<h3 align="center">Software Development for Robotics</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![build](https://img.shields.io/badge/build-melodic-green)]()
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Final Projects
</p>

## 🏁 Individual Project
### The project folder is locate at [HERE](https://github.com/ksu-cs-robotics/Software-Development-for-Robotics/tree/master/src/project_ws)

#### commands for launch individual project playground
launch the gazebo environment with single robot inside
```
export TURTLEBOT3_MODEL=waffle_pi
roslaunch project_gazebo single_robot.launch
```
launch autonomous driving package
```
export TURTLEBOT3_MODEL=waffle_pi
roslaunch project_navigation single_AmclStack.launch
```
launch rviz for autonomous driving and visualize
```
roslaunch project_navigation rviz_single_robot.launch
```
launch teleop to control the robot
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=tb3_0/cmd_vel
```

### Goal:
1. change all topic name from **/tb3_0/TOPIC_NAME** to **/YOUR_NAME/TOPIC_NAME** (for example: /tb3_0/odom to /shawn/odom)

    (hint: look into how **group** tag work and how **prefix** work in ROS)

1. make sure the autonomous driving function still works after you are done with the first one.

1. detecting different color in Gazebo environment then modify original image and publish result to new topics: "YOUR_NAME/color_detected" (for colors detected, such as "red", "yellow", "green"); "YOUR_NAME/modified_image" (for the new modified image).

    you only need to detect whatever colors in the middle of your screen

    (hint: subscribe to original image topic, and publish modified image to a new topic)


when there is no color in the middle of your screen
<img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/not_found.png" alt="not_found">

when there are colors in the middle of your screen
<img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/found.png" alt="found">