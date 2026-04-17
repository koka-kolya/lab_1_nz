#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class EvenTalker(Node):

    num = 0;

    def __init__(self):

        # Declare node even_talker_params
        super().__init__('even_talker_params')

        # Declare default parameters
        self.declare_parameter('publish_frequency', 8.0) # Freq, Hz
        self.declare_parameter('overflow_threshold', 80) # Threshold
        self.declare_parameter('topic_name', 'even_talker') # Topic name
        self.declare_parameter('ovf_topic_name', 'overflow')
        self.declare_parameter('add_value', 2)  # Value by add

        # Read parameters
        self.freq = self.get_parameter('publish_frequency').value
        self.threshold = self.get_parameter('overflow_threshold').value
        self.topic = self.get_parameter('topic_name').value
        self.ovf_topic_name = self.get_parameter('ovf_topic_name').value
        self.add_value = self.get_parameter('add_value').value

        # Create publisher by parameter name
        self.publisher_data = self.create_publisher(Int32, self.topic, 10)

        # Calculate time period and check for zero
        if self.freq != 0:
            time_period = 1.0 / self.freq
        else:
            time_period = 1.0

        # Create timer
        self.timer = self.create_timer(time_period, self.timer_callback)

        self.get_logger().info(f"Node even_talker_params is run. \n" \
                                f"Freq = {self.freq} Hz,\n" \
                                f"Threshold = {self.threshold}, \n" \
                                f"Topic name: {self.topic}\n"
                                f"Overflow topic name := {self.ovf_topic_name}.")

    #------------------------------------
    # This function runs with frequency
    #------------------------------------
    def timer_callback(self):
        msg = Int32() # empty message
        msg.data = self.num
        if self.num < self.threshold:
            self.publisher_data.publish(msg)
            self.get_logger().info(f"Value = {str(msg.data)}")
            self.num += self.add_value
        else:
            self.overflow_handler()

    def overflow_handler(self):
        self.publisher_ovf = self.create_publisher(Int32, self.ovf_topic_name, 10)
        msg_ovf = Int32()
        msg_ovf.data = self.num
        self.publisher_ovf.publish(msg_ovf)
        self.get_logger().info(str(msg_ovf.data))
        self.num = 0

#------------------------------------
# Main function
#------------------------------------
def main():
    rclpy.init()    # begin work with ROS 2

    node = EvenTalker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

    
