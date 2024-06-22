python rl-toolkit/dm/ddpm.py \
    --traj-load-path ./expert_datasets/hand_10000_v2.pt \
    --lr 0.00003 \
    --hidden-dim 2048 \
    --norm True \
    --scheduler-type sigmoid \
    --num-epoch 10000 