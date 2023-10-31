from qiskit import Aer, QuantumCircuit, transpile

def main():
    # creating a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)

    # adding an H gate to q0
    qc.h(0)

    # adding a CNOT gate to q0 that controls q1
    # if q0 is 1, q1 = !q1
    qc.cx(0, 1)

    # creating a measure barrier for clarity
    qc.barrier(range(2))

    # measuring both qubits and mapping to classical bits
    qc.measure(range(2), range(2))

    # drawing the circuit!
    print(qc.draw())

    # getting the noisy simulator backend
    backend = Aer.get_backend("qasm_simulator")

    # transpiling/running the circuit
    job = backend.run(transpile(qc, backend), shots=1000)

    # getting the result from the job
    result = job.result()

    # getting the counts of what the different shots measured
    counts = result.get_counts(qc)
    print(counts)


if __name__ == "__main__":
    main()
