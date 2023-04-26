# eteration_ROS_pubsub

## Summary

After setting up ROS Noetic on my Ubuntu 20.04 machine and setting up my environment, I made 2 ROS Nodes (Node is an executable file); composiv_talker and composiv_listener.
While composiv_talker keeps sending messages to a ROS Topic (think of ROS Topics as an Telegram chatroom where only composiv_talker can send messages and every other node that checks this room can only read), composiv_listener reads messages from this topic and prints it on the console.
In the end, I have written a launch file so that user can run multiple nodes with a single command in one terminal.

## How it works? 
in the catkin_ws folder, run the command $roslaunch composiv_tryouts composiv_tryout.launch
