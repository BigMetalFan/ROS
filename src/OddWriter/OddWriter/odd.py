
#!/usr/bin/env python3
import rclpy                        
from rclpy.node import Node         
from std_msgs.msg import String    




class OddWriterNode(Node):

    def __init__(self):
        super().__init__('neoddWriter')

        self.publisher = self.create_publisher(String, 'odd_stream', 10)

        timer_period = 0.1        
        self.counter = 0
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info("Узел запущен, сэр!")

    def timer_callback(self):
        msg = String()                      

        msg.data = f"Очень четное число {self.counter}"  
        self.counter+=2
        if self.counter > 98: self.counter = 0
        self.publisher.publish(msg)         
        self.get_logger().info(msg.data)    


def main():
    rclpy.init()                    

    node = OddWriterNode()                 

    try:
        rclpy.spin(node)            
    except KeyboardInterrupt:
        pass                        
    finally:
        node.destroy_node()         
        rclpy.shutdown()            


if __name__ == '__main__':
    main()

