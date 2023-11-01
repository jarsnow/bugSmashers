from qiskit import Aer, QuantumCircuit, transpile

# coinflip.py creates a state that goes by the fancy name of the
# "GHZ" state (either all 1s or all 0s for the qubits)
# this script automates it for n qubits!

def main():
    # getting the qubit count from the user
    # n must be >1 for the GHZ state
    qbs = ""
    while type(qbs) is str:
        qbs = input("Enter the amount of qubits you want: ")

        try:
            qbs = int(qbs)
            # restricting qbs between 2 and 12
            # > 12 could start running slow
            # but experimentation is encouraged
            if qbs < 2 or qbs > 12:
                qbs = ""
        except:
            qbs = ""

    # creating a quantum circuit with (qbs) qubits and (qbs) classical bits
    qc = QuantumCircuit(qbs, qbs)

    # adding an H gate to q0 to set up the initial coinflip
    qc.h(0)

    # adding the CNOT gates sequentially down to qbs
    for n in range(qbs - 1):
        qc.cx(n, n + 1)

    # creating a measure barrier for clarity
    qc.barrier(range(qbs))

    # measuring both qubits and mapping to classical bits
    qc.measure(range(qbs), range(qbs))

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
