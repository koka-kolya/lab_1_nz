from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    # Declare arguments
    freq_arg = DeclareLaunchArgument(
        'publish_frequency',
        default_value='8.0',
        description='Publish frequency (Hz)'
    )

    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='80',
        description='Overflow threshold'
    )
    
    topic_arg = DeclareLaunchArgument(
        'topic_name',
        default_value='/even_numbers',
        description='Topic for even numbers'
    )
    
    ovf_topic_arg = DeclareLaunchArgument(
        'ovf_topic_name',
        default_value='/overflow',
        description='Topic for overflow messages'
    )

    # Get current values
    frequency = LaunchConfiguration('publish_frequency')
    threshold = LaunchConfiguration('overflow_threshold')
    topic_name = LaunchConfiguration('topic_name')
    ovf_topic_name = LaunchConfiguration('ovf_topic_name')

    return LaunchDescription([
        freq_arg,
        threshold_arg,
        topic_arg,
        ovf_topic_arg,

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