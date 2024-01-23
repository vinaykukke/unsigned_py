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
