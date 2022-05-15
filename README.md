# Nussinovs_Algorithm
Runs a customized version of Nussinov's Algorithm given an input genetic sequence.

In particular, s[i,j] represents the maximum number of complementary base pairings in the sequence vi,..., vj.


              s[i, j] = max(
                            0, if i ≥ j,          
                            s[i + 1, j − 1] + 1, if i < j and (vi, vj) ∈ Γ,
                            s[i + 1, j − 1], if i < j and (vi, vj) ∈/ Γ,              
                            s[i + 1, j], if i < j,              
                            s[i, j − 1], if i < j,
                            max({s[i, k] + s[k + 1, j]}) for i < k < j, if i < j. 
                        )
              
where Γ = {(A, U),(U, A),(G, C),(C, G)}

Just enter the RNA sequence as the "String" variable in test.py
