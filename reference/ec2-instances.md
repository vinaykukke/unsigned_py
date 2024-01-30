# How to setup a custom AMI to install any version of a 3D software

- [REFERENCE DOCUMENTATION](https://docs.thinkboxsoftware.com/products/deadline/10.1/1_User%20Manual/manual/aws-custom-ami.html)
- In EC2 goto the AMI sections and select the `Deadline Base Worker 10.x.x.x` for Windows or Linux and launch an instance from it.
- Once the instance is launched, connect to the instance using `SSH (Linux)` or `RDP (Windows)`
- Once connected install the 3D software that you would like to have e.g Blender
- Install the `Nvidia Graphic Driver`, these do not come automatically installed in the EC2 instance. To install them refere to the guide:
    - [Windows Nvidia Drivers](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/install-nvidia-driver.html#nvidia-GRID-driver)
    - [Linux Nvidia Drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html#nvidia-GRID-driver)
- `Linux` 
    > `NOTE:` *Here the Linux being used is the Amazon Linux 2. This does not have a head and all softwares that are installed on it must be able to run headless.*
    - GIT
        - Run system update, this will update the existing packages and also refresh the system’s repository cache.
            ``` bash
            sudo yum update
            sudo yum install git
            ```
        - Check that git is working
        ```bash
        git version
        ```
    - Install `Snap`

    ```bash
    sudo yum install snapd
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
    ```

    - Install blender using snap
    ```bash
    snap install blender --classic
    ```
    - Once blender is installed please check the installation location using
    ```bash
    which blender
    ```
- `Windows`:
    - Once the Windows instance has been configured, you must stop the Deadline Launcher Service. To do this, open the start menu and type “Powershell”. “Windows Powershell” should come up as the first item in the search results. Hit Enter and a Powershell window will open. In the powershell Window, run the following command:

    ``` batch
    :: Only for windows
    Stop-Service -Name "deadline10launcherservice"
    ```

    - Next, run EC2LaunchSettings from the start menu. 
        - Go to the start menu, type Ec2LaunchSettings and launch it.
        - Make sure Set Computer Name is selected. This will ensure each instance you create has a unique name.
        - Select Run EC2Launch on every boot.
        - Click - Shutdown without Sysprep
- Once the instance has been configured go to `AWS Management Console > EC2 > Instance`. Right click your instance, `select Image > Create Image`. Then input the Image Name, Note that Image Names must be unique per region per account. Click Create Image after you have input the Image Name.
- Once your AMI has been created make a launch template from the running instance.
    - Once your new AMI is listed as available, go to Services → EC2 and click Instances (running).
    - Right-click your Workstation instance and choose Image and templates → Create template from instance.
    - Name your launch template (e.g., My-Studio-Workstation-LT). Write down the name on your cheat sheet.
    - Under Network interfaces, set Auto-assign public IP to Enable, otherwise you will not be able to connect to the instances you launch.
    - Add the necessary security groups:
        - Windows: `unsigned-windows-SG`
        - Linux: `unsigned-linux-SG`

# Choosing the right EC2 Instance for rendering.

Please refer to these blog post about the same:
- [Part 1](https://aws.amazon.com/blogs/media/choosing-the-right-amazon-ec2-instance-types-for-rendering-with-thinkbox-deadline-part-1/)
- [Part 2](https://aws.amazon.com/blogs/media/choosing-the-right-amazon-ec2-instance-types-for-rendering-with-thinkbox-deadline-part-2/)

## Anatomy of Instances

- Instance families
    - C – Compute optimized
    - D – Dense storage
    - F – FPGA
    - G – Graphics intensive
    - Hpc – High performance computing
    - I – Storage optimized
    - Im – Storage optimized with a one to four ratio of vCPU to memory
    - Is – Storage optimized with a one to six ratio of vCPU to memory
    - Inf – AWS Inferentia
    - M – General purpose
    - Mac – macOS
    - P – GPU accelerated
    - R – Memory optimized
    - T – Burstable performance
    - Trn – AWS Trainium
    - U – High memory
    - VT – Video transcoding
    - X – Memory intensive

- Processor families
    - a – AMD processors
    - g – AWS Graviton processors
    - i – Intel processors

- Additional capabilities
    - b – EBS optimized
    - d – Instance store volumes
    - n – Network and EBS optimized
    - e – Extra storage or memory
    - z – High performance
    - q – Qualcomm inference accelerators
    - flex – Flex instance

## Sizes

The size is how powerful the instance type is, and can be one of the following:

    - nano
    - micro
    - small
    - medium
    - large
    - xlarge
    - #xlarge (where # is a number)

Each size has twice the vCPUs and RAM of the size before it. For example:

    - c4.large has 2 vCPU and 3.75 GB of RAM
    - c4.xlarge has 4 vCPU and 7.5 GB of RAM
    - c4.2xlarge has 8 vCPU and 15 GB of RAM

Not all instance types include all sizes. For example, T2 instances go from nano to 2xlarge but C4 instances only go from large to 8xlarge.

## Presets in Deadline

When you press one of the buttons in the instance presets, all of the instances that meet the specs of the preset are automatically added to your selected instance types.

    Small — All available instance types that have 8 vCPUs and at least 15 GB of RAM.
    Medium — All available instance types that have 16 vCPUs and at least 30 GB of RAM.
    Large — All available instance types that have 32 vCPUs and at least 60 GB of RAM.
    XLarge — All available instance types that have 64 vCPUs and at least 120 GB of RAM.
    GPU — All available GPU instances types.

## GPU'S

With AWS Portal and Spot Instances, you also have access to GPU instances, which allow you to use GPU renderers like Redshift without the expense of having to pay for costly GPUs yourself. The G3 instances type is recommended for rendering, and they feature NVIDIA ® Tesla M60 GPUs, each with 2048 CUDA ® cores and 8 GB of GPU memory.

The following G3 instance types are currently available:

    g3.4xlarge has 1 GPU with 8 GB of GPU RAM, and 16 vCPUs with 122 GB of RAM
    g3.8xlarge has 2 GPUs with 16 GB of GPU RAM, and 32 vCPUs with 244 GB of RAM
    g3.16xlarge has 4 GPUs with 32 GB of GPU RAM, and 64 vCPUs with 488 GB of RAM

There are also the P3 instance types, which are designed for general-purpose GPU computing, such as machine learning and computational fluid dynamics. They feature NVIDIA ® Tesla V100 GPUs, each with 5,120 CUDA cores and 640 Tensor Cores.

The following P3 instance types are currently available:

    p3.xlarge has 1 GPU with 16 GiB of GPU RAM, and 8 vCPUs with 61 GiB of RAM
    p3.8xlarge has 4 GPUs with 64 GiB of GPU RAM, and 32 vCPUs with 244 GiB of RAM
    p3.16xlarge has 8 GPUs with 128 GiB of GPU RAM, and 64 vCPUs with 488 GiB of RAM

The P3 instance types have CUDA Compute Capability 7.0 and G3 instance types have CUDA Compute Capability 5.2. The latter is recommended for Redshift rendering.
