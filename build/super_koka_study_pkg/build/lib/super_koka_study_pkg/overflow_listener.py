#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):

    def __init__(self):
        # name for node "listener_overflow"
        super().__init__('listener_overlow')
        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.callback,
            10
        )

        self.get_logger().info("Node listener_overflow is run and listen topic")

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
