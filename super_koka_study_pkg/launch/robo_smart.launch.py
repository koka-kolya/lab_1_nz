from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    
    # Declare arguments

    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='slow',
        description='Select mode for run'
    )

    # Get current values
    mode = LaunchConfiguration('mode')

    frequency = PythonExpression([
        "20.0 if '", mode, "' == 'fast' else 5.0"
    ])

    threshold = PythonExpression([
        "50 if '", mode, "' == 'fast' else 150"
    ])

    topic_name = PythonExpression([
        "'/even_numbers_fast' if '", mode, "' == 'fast' else '/even_numbers_slow'"
    ])

    ovf_topic_name = PythonExpression([
        "'/overflow_fast' if '", mode, "' == 'fast' else '/overflow_slow'"
    ])

    return LaunchDescription([
        mode_arg,

        # Publisher node
        Node(
            package='super_koka_study_pkg',
            executable='even_talker_params',
            name='even_pub_params',
            parameters=[
                {'publish_frequency': frequency},
                {'overflow_threshold': threshold},
                {'topic_name': topic_name},
                {'ovf_topic_name': ovf_topic_name},
            ],
            output='screen',
        ),
        
        # Listener node
        Node(
            package='super_koka_study_pkg',
            executable='overflow_listener_params',
            name='overflow_listener_params',
            parameters=[
                {'subscription_name': ovf_topic_name},
            ],
            output='screen',
        ),
    ])