# eteration_ROS_pubsub

## Summary

After setting up ROS Noetic on my Ubuntu 20.04 machine and setting up my environment, I made 2 ROS Nodes (Node is an executable file); composiv_talker and composiv_listener.
While composiv_talker keeps sending messages to a ROS Topic (think of ROS Topics as an Telegram chatroom where only composiv_talker can send messages and every other node that checks this room can only read), composiv_listener reads messages from this topic and prints it on the console.
In the end, I have written a launch file so that user can run multiple nodes with a single command in one terminal.

## Composiv_talker
You can find the code for talker node under composiv_tryouts/scripts/composiv_talker.py

Initialized the node as "composiv_talker" 

Publishes messages to "chatter" topic

Keeps sending the message "hello world, i am a ROS talker node!" within 10Hz until the process gets cancelled (CTRL+C or shutdown)

reference: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

## Composiv_listener
You can find the code for listener node under composiv_tryouts/scripts/composiv_listener.py

Initialized the node as "composiv_listener" 

Subscribes to the "chatter" topic

If a message occurs on the chatter topic, callback function is called.

reference: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

## composiv_tryout.launch
You can find the launch file under composiv_tryouts/launch/composiv_tryout.launch

Creates 1 composiv_talker and 1 composiv_listener nodes.

Feel free to add more talker/listeners

## How it works? 
in the catkin_ws folder, run the command $roslaunch composiv_tryouts composiv_tryout.launch

## Resources
Some resources that might be helpful for more detailed information: 
http://wiki.ros.org/ROS/Tutorials

