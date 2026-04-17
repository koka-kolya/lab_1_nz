#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time

def timer_callback():
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    print(f"Timestamp: {timestamp}")

def main(args=None):
    rclpy.init(args=args)
    node = Node('time_printer')

    timer = node.create_timer(5.0, timer_callback)
    # node.get_logger().info(timer.clock)
    rclpy.spin(node)        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



