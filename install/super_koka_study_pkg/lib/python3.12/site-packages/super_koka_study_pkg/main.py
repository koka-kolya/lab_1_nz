#!/usr/bin/env python3

import rclpy
from rclpy import Node
import time

def timer_callback():
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    return f"Current time: {timestamp}"

def main(args=None):
    rclpy.init(args=args)
    node = Node('time_printer')
    node.get_logger().info(f"{timer_callback()}")
    rclpy.spin(node)        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



