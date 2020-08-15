namespace Bell {
       open Microsoft.Quantum.Intrinsic;
       open Microsoft.Quantum.Canon;

        // (name : type, args...) : returned type
        operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
            if (desired != M(q1)) {
                X(q1);
            }
        }

        @EntryPoint() // concrete compilator used by .net
        operation TestBellState(count : Int, initial : Result) : (Int, Int, Int) {

        mutable numOnes = 0; // changable variable, variable arguments are not changeable
        mutable agree = 0;
        using ((qubit1, qubit2) = (Qubit(), Qubit())) {

            for (test in 1..count) {
                SetQubitState(initial, qubit1);
                SetQubitState(Zero, qubit2);

                // revert
                // X(qubit1);
                // set qubit in superposition state
                // H(qubit1)

                
                H(qubit1);
                CNOT(qubit1, qubit2); // assigns q2 to q1 if q1 is One
                let res = M(qubit1);

                if (M(qubit2) == res) {
                    set agree += 1;
                }
                // Count the number of ones we saw:
                if (res == One) {
                    set numOnes += 1;
                }
            }
                
            SetQubitState(Zero, qubit1);
            SetQubitState(Zero, qubit2);
        }

        // Return number of times we saw a |0> and number of times we saw a |1>
        Message("Test results (# of 0s, # of 1s): ");
        return (count - numOnes, numOnes, agree);
    }
}
