#!/usr/bin/env python3
#SPDX-FileCopyrightText: 2025 Akari Sunagawa
#SPDX-License-Indentifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from datetime import datetime
from std_msgs.msg import String

class ClockDisplay(Node):
    def __init__(self):
        super().__init__('clock_display')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # 現在時刻（秒）
        now = self.get_clock().now()
        sec = now.nanoseconds * 1e-9

        # 変換
        time_str = datetime.fromtimestamp(sec).strftime('%H:%M:%S')

        self.get_logger().info(f'現在の時刻: {time_str}')

def main():
    rclpy.init()
    node = ClockDisplay()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
