---
---
## Clone and Setup Custom Workspace

1. Clone the idealab repository

    ```bash
    git clone https://github.com/idealabasu/code_idealab_ros.git
    ```

1. Compile

    ```bash
    cd code_idealab_ros/
    catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
    ```

1. Source your workspace (whenever you clone a new repository/workspace)

    ```bash
    # one time:
    #source devel/setup.bash
    # or permanent:
    echo "source ~/code_idealab_ros/devel/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    ```
