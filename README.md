Post-Quantum Cryptography: Benchmarks and Attack Simulations for NIST PQC Algorithms (Kyber, Dilithium, SPHINCS).


Reproduce This

Option A - Using Docker

docker build -t capstone:dev .; docker run --rm -v "$PWD":/work capstone:dev

The command docker build -t pqc:dev . && docker run --rm -v "$PWD":/work pqc:dev is used to make entire analysis process reproducible in any environment. First, docker build -t pqc:dev . tells Docker to create an image named pqc:dev based on the instructions in Dockerfile located in the current directory; this image contains all the dependencies and code needed for analysis. Next, if the build succeeds, docker run --rm -v "$PWD":/work pqc:dev starts a fresh container from the image and mounts current project directory into the container's /work folder, so the analysis step has access to both input data and a place to store output files. The --rm flag ensures that the container is automatically deleted after it finishes, keeping system clean. This workflow guarantees that anyone can run your analysis, see exactly the same input and output files, and reproduce your results with a single command, regardless of  local setup.

What we should see after run: 
\docs\mean_latency_by_algorithm.txt containing algorithm average latency values.
\docs\min_attack_rate_by_sector.txt comtaining attack rate by sector

Option B- Without Docker 

run ./run_analysis.ps1

What we should see after run: 
\docs\mean_latency_by_algorithm.txt containing algorithm average latency values.
\docs\min_attack_rate_by_sector.txt comtaining attack rate by sector