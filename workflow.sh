> ssh -Y andes.olcf.ornl.gov

[imn@andes-login8:/lustre/orion/stf006/scratch/imn/turbine_viz/blades/paraview] 8-) module load paraview/5.13.3-osmesa imagemagick

[imn@andes-login8:/lustre/orion/stf006/scratch/imn/turbine_viz/blades/paraview] 8-) cat job_andes.sh 
#!/bin/bash
#SBATCH -A stf006
#SBATCH -J vizzzzz
#SBATCH -o %x-%j.out
#SBATCH -t 24:00:00
#SBATCH -N 1
#SBATCH --partition gpu
#SBATCH --exclusive
module load paraview/5.13.3-osmesa
cd /lustre/orion/stf006/scratch/imn/turbine_viz/blades/paraview
srun -n 1 -c 32 --gpus-per-task=1 --gpu-bind=closest /sw/andes/paraview/5.13.3-osmesa/bin/pvbatch ./script.py

[imn@andes-login8:/lustre/orion/stf006/scratch/imn/turbine_viz/blades/paraview] 8-) sbatch job_andes.sh

# Copy png files to local machine, e.g., scp dtn.olcf.ornl.gov:/lustre/orion/stf006/scratch/imn/turbine_viz/disk/paraview/*.png .
# Install ffmpeg on your machine, e.g., snap install ffmpeg

> ffmpeg -framerate 30 -i blades_animation.%04d.png -c:v libx264 -crf 18 blades_video.mp4
