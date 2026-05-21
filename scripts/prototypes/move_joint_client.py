from __future__ import annotations

import sys

import rclpy
from dsr_msgs2.srv import MoveJoint
from rclpy.node import Node


SERVICE_NAME = "/dsr01/dsr_controller2/motion/move_joint"


class MoveJointClient(Node):
    """Minimal client for the Doosan MoveJoint service."""

    def __init__(self) -> None:
        super().__init__("move_joint_client")
        self.client = self.create_client(MoveJoint, SERVICE_NAME)

    def wait_until_available(self, timeout_sec: float = 5.0) -> bool:
        return self.client.wait_for_service(timeout_sec=timeout_sec)

    def send_relative_motion(self) -> bool:
        request = MoveJoint.Request()
        request.pos = [0.0, 0.0, 90.0, 0.0, -90.0, 0.0]
        request.vel = 10.0
        request.acc = 10.0
        request.time = 0.0
        request.radius = 0.0
        request.mode = 1
        request.blend_type = 0
        request.sync_type = 0

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()

        if response is None:
            self.get_logger().error("MoveJoint service returned no response.")
            return False

        self.get_logger().info(f"MoveJoint success: {response.success}")
        return bool(response.success)


def main() -> int:
    rclpy.init()

    node = MoveJointClient()

    try:
        if not node.wait_until_available():
            node.get_logger().error(f"Service not available: {SERVICE_NAME}")
            return 1

        success = node.send_relative_motion()
        return 0 if success else 1

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    sys.exit(main())