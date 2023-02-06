This workspace holds the deliverables for Assignment 1B - Task 2.

Task 2 is comprised of 3 parts -
1. circle.py - This script makes the Turtle to move in a circle with a constant twist velocity.
![Screenshot](https://github.com/Vasanth2796/AuE8230Spring23_VasanthSeethapathi/tree/master/assignment2_ws/src/assignment1b/Screenshots/circle.png)


2. square_openloop.py - This script makes the turtle to move in a constant linear velocity of 0.2 and an angular velocity of 0.2 rad/sec. The turtle moves in a trajectory of square shape having 2*2 units.
![Screenshot](https://github.com/Vasanth2796/AuE8230Spring23_VasanthSeethapathi/tree/master/assignment2_ws/src/assignment1b/Screenshots/square_openloop.png)


3. square_closedloop.py - This script makes the turtle to move in a trajectory of square (3*3 units). A P controller is implemented to control the linear velocity and the heading angle to obtain the desired square trajectory.
![Screenshot](https://github.com/Vasanth2796/AuE8230Spring23_VasanthSeethapathi/tree/master/assignment2_ws/src/assignment1b/Screenshots/square_closedloop.png)




The workproducts for this assignment is available in the below folders in this directory -
Git Path : https://github.com/Vasanth2796/AuE8230Spring23_VasanthSeethapathi.git
Folder Structure: ../assignment2_ws/src/assignment1b




Screenshots - There "png" files showing the trajectory of turtle while running the baove 3 python files.
src - This folder comprises of the source code for Task 2.
Video - There "mkv" files shows the execution of python file and shows the trajectory of turtle while running the code.




HOW TO RUN THE CODE -
1. Firstly open a new terminal and execute the command "roscore"
2. Open another new terminal and execute the command "rosrun turtlesim turtlesim_node".
3. Make sure the python file created for the Task is converted into executable by tight clicking on the properties of the file. This option is available in the permissions tab.
4. Then, open another terminal and type the command "rosrun assignment1b square_closedloop.py"



Citations:
1. http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line
2. http://wiki.ros.org/turtlesim/Tutorials/Rotating%20Left%20and%20Right
3. The file received in Canvas - "gotogoal.py"
4. https://www.youtube.com/watch?v=STSPDYFDE8E - How to control turtlebot by a python file in ROS
