# Quantum Computing Exploration

A hands-on exploration of quantum computing built with [CUDA Quantum](https://developer.nvidia.com/quantum-computing) (cudaq).

## Quick Start

Clone the repository:

```bash
git clone https://github.com/shororxor/nus-qubits-workshop.git
cd nus-qubits-workshop
```

Install the project dependencies ([uv](https://docs.astral.sh/uv/) is required) and run the quantum program:

```bash
uv sync
uv run quantum
```

If your machine has NVIDIA hardware with the proper drivers, you will see the sampler output. This project currently demonstrates CUDA Quantum through Python, which keeps setup simple. Instructions for using the C++ workflow will be covered later.