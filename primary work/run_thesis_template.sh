#!/bin/bash
# ============================================================
# SLURM GPU Job Script — Template for the cluster
# ============================================================
# HOW TO USE THIS FILE:
#   1. Fill in every section marked with TODO
#   2. Submit your job with: sbatch run_thesis_template.sh
#   3. Monitor it with:       squeue -u <your_username>
#   4. View output logs:      cat <job_name>_<jobid>.out
# ============================================================

# --- SLURM Job Configuration ---
# TODO: Change the job name to something descriptive for your project
SBATCH --job-name=MY_JOB_NAME

# These cluster settings are shared — leave them as-is
SBATCH --partition=gpu
SBATCH --account=slurm-students

# TODO: Adjust the time limit to suit your expected runtime (HH:MM:SS)
SBATCH --time=10:00:00

# TODO: Rename output/error log files to match your job name
SBATCH --output=my_job_%j.out
SBATCH --error=my_job_%j.err

# ============================================================
echo "--- Initializing Environment ---"

# TODO: Update this path to point to YOUR virtual environment
# Example: source ~/my_project/my_env/bin/activate
source ~/YOUR_PROJECT/YOUR_ENV/bin/activate

# ============================================================
echo "--- Starting Local Ollama Server on GPU Node ---"

# This starts Ollama in the background — no changes needed here
# as long as you have Ollama installed at ~/bin/ollama
OLLAMA_HOST=0.0.0.0:11434 ~/bin/ollama serve &

# Wait for the Ollama daemon to finish starting up
sleep 10

# ============================================================
# TODO: Replace the blocks below with your own scripts.
# Add or remove blocks as needed — one per experiment/step.
# Format:  echo "--- Description ---"
#          python3 your_script.py

echo "--- Running Step 1: [Describe what this does] ---"
# TODO: Replace with your first script
python3 your_step_1_script.py

# ============================================================
echo "--- All steps complete! Releasing GPU. ---"
