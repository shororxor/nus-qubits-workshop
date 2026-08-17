import sys
import cudaq

print(f"Running on targer {cudaq.get_target().name}")
qubit_count = int(sys.argv[1]) if 1 < len(sys.argv) else 2

@cudaq.kernel
def kernel():
    qubits = cudaq.qvector(qubit_count)
    h(qubits[0])
    for i in range(1, qubit_count):
        x.ctrl(qubits[0], qubits[i])
    mz(qubits)

@cudaq.kernel
def kernel2(qubit_count: int):
    qvector = cudaq.qvector(qubit_count)
    h(qvector[0])
    for i in range(0, qubit_count - 1):
        x.ctrl(qvector[i], qvector[i + 1])
    mz(qvector)

def main() -> None:
    result = cudaq.sample(kernel)
    print(f"Result = {result}");
    print("Succefully")


if __name__ == "__main__":
    main()
