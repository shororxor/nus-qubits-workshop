import sys
import cudaq
import numpy as np
import matplotlib.pyplot as plt
import qutip

print(f"Running on targer {cudaq.get_target().name}")
qubit_count = int(sys.argv[1]) if 1 < len(sys.argv) else 2

# Basic quantum circuit
@cudaq.kernel
def kernel():
    qubits = cudaq.qvector(qubit_count)
    h(qubits[0])
    for i in range(1, qubit_count):
        x.ctrl(qubits[0], qubits[i])
    mz(qubits)

# Basic quantum circuit
@cudaq.kernel
def kernel2(qubit_count: int):
    qvector = cudaq.qvector(qubit_count)
    h(qvector[0])
    for i in range(0, qubit_count - 1):
        x.ctrl(qvector[i], qvector[i + 1])
    mz(qvector)

# Manipulate qubit with quantum gates
# and visualize with bloch sphere
@cudaq.kernel
def state_to_qvector(state: list[complex]):
    qubit = cudaq.qvector(state)

def visualization():
    minus_state = [complex(np.sqrt(2)/2, 0), complex(-np.sqrt(2)/2,0)]
    zero_state = [complex(1, 0), complex(0, 0)];

    minus_state_sphere = cudaq.add_to_bloch_sphere(cudaq.get_state(state_to_qvector, minus_state))
    zero_state_sphere = cudaq.add_to_bloch_sphere(cudaq.get_state(state_to_qvector, zero_state))

    minus_state_sphere.save('src/quantum/output/minus_state_sphere.png')
    zero_state_sphere.save('src/quantum/output/zero_state_sphere.png')


def main() -> None:
    result = cudaq.sample(kernel2, 3)
    print(f"Result = {result}");

    visualization()
    print("Running succefully")


if __name__ == "__main__":
    main()
