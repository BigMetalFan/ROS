#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time
from datetime import datetime as dt

def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = Node('timeNode')               # создаём узел с именем hello_nodes
    while True:
        node.get_logger().info(str(dt.now()))  
        time.sleep(5)                      # запускаем цикл обработки
    #rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



