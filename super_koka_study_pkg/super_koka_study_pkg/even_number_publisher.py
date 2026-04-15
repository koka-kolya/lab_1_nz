#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class EvenTalker(Node):

    num = 0;

    def __init__(self):
        #Name for node "even_talker"
        super().__init__('even_talker')

        self.publisher_data = self.create_publisher(Int32, 'even_numbers', 10)

        time_period = 0.1
        self.timer = self.create_timer(time_period, self.timer_callback)

        self.get_logger().info("Node even_talker is run")

    #------------------------------------
    # This function runs at every 0.1s
    #------------------------------------
    def timer_callback(self):
        msg = Int32() # empty message
        msg.data = self.num
        if self.num < 100:
            self.publisher_data.publish(msg)
            self.get_logger().info(str(msg.data))
            self.num += 2
        else:
            self.overflow_handler()

    def overflow_handler(self):
        self.publisher_ovf = self.create_publisher(Int32, 'overflow', 10)
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

    
