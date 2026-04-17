import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/koka-kolya/ros2_ws/src/install/super_koka_study_pkg'
