#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):

    def __init__(self):
        # Declare overflow_listener_params node
        super().__init__('overflow_listener_params')
        
        # Declare param
        self.declare_parameter('node_name', 'overflow_listener_params')
        self.declare_parameter('subscription_name', 'overflow')

        self.subscription_name = self.get_parameter('subscription_name').value
        self.node_name = self.get_parameter('node_name').value

        # Subscribing
        self.subscription = self.create_subscription(
            Int32,
            self.subscription_name,
            self.callback,
            10
        )

        self.get_logger().info(f"Node {self.node_name} is run \n" \
                               f"Subscription name: {self.subscription_name}")

    def callback(self, msg):
        self.get_logger().info(f"!!! Overflow !!! Recieved value = {msg.data}")

def main():
    rclpy.init()
    node = OverflowListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
