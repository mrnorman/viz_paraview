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

> ffmpeg -framerate 30 -i disk_animation.%04d.png -c:v libx264 -preset slow -c:a aac -crf 23  -movflags +faststart -pix_fmt yuv420p disk_video.mp4
> ffmpeg -framerate 30 -i blades_animation.%04d.png -c:v libx264 -preset slow -c:a aac -crf 23  -movflags +faststart -pix_fmt yuv420p blades_video.mp4
> ffmpeg -i ./blades_video.mp4 -i ./disk_video.mp4 -filter_complex "[0:v]crop=w=iw:h=ih*0.7:x=0:y=ih*0.2[v0]; [1:v]crop=w=iw:h=ih*0.7:x=0:y=ih*0.2[v1]; [v0][v1]vstack=inputs=2[out]" -map "[out]"  -c:v libx264 -preset slow -c:a aac -crf 23  -movflags +faststart -pix_fmt yuv420p combined.mp4
