python rl-toolkit/dm/ddpm.py \
    --traj-load-path ./expert_datasets/walker_5traj_processed.pt \
    --lr 0.0002 \
    --hidden-dim 1024 \
    --norm True \
    --scheduler-type sigmoid \
    --num-epoch 8000 