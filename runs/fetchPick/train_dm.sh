python rl-toolkit/dm/ddpm.py \
    --traj-load-path expert_datasets/pick_10000_clip.pt \
    --lr 0.001 \
    --hidden-dim 1024 \
    --norm True \
    --scheduler-type sigmoid \
    --num-epoch 10000 