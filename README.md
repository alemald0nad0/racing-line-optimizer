# Racing Line Optimizer

Research and development project for computing optimized racing lines under
vehicle, tyre, aerodynamic, fuel-load and track-condition constraints.

## Project status

Early research and prototyping stage.

## Initial objectives

1. Represent a circuit from centerline and track-boundary data.
2. Calculate geometric properties such as curvature and heading.
3. Generate a minimum-curvature racing line.
4. Estimate a feasible longitudinal speed profile.
5. Progress toward minimum-lap-time and optimal-control formulations.
6. Validate results using synthetic and real telemetry data.

## Development environment

- Fedora Linux
- Python 3.12
- Miniconda
- uv
- Git and GitHub

## Installation

```bash
conda env create -f environment.yml
conda activate racing-line-optimizer
conda env config vars set UV_PROJECT_ENVIRONMENT="$CONDA_PREFIX"
conda deactivate
conda activate racing-line-optimizer
uv sync --inexact --all-groups 



