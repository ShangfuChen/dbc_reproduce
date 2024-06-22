python rl-toolkit/dm/ddpm.py \
    --traj-load-path ./expert_datasets/ant_10000.pt \
    --lr 0.0002 \
    --hidden-dim 1024 \
    --norm False \
    --scheduler-type sigmoid \
    --num-epoch 20000 