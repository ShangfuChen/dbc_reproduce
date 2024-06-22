python dbc/main.py \
    --alg=dbc \
    --bc-num-epochs=2000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --coeff=30 \
    --coeff-bc=1 \
    --cuda=True \
    --ddpm-path=./rl-toolkit/dm/trained_models/maze2d_100_ddpm_0.0001_128_sigmoid.pt \
    --depth=3 \
    --env-name=maze2d-medium-v2 \
    --eval-interval=2000 \
    --eval-num-processes=10 \
    --hidden-dim=256 \
    --il-in-action-norm=True \
    --il-out-action-norm=True \
    --log-interval=200 \
    --lr=0.00005 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --save-interval=20000 \
    --traj-load-path=./expert_datasets/maze2d_100.pt \
    --vid-fps=60 \
    --traj-batch-size 128 \
    --scheduler-type sigmoid \
    --prefix=dbc \
    --seed=1

python dbc/main.py \
    --alg=dbc \
    --bc-num-epochs=2000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --coeff=30 \
    --coeff-bc=1 \
    --cuda=True \
    --ddpm-path=./rl-toolkit/dm/trained_models/maze2d_100_ddpm_0.0001_128_sigmoid_norm.pt \
    --depth=3 \
    --env-name=maze2d-medium-v2 \
    --eval-interval=2000 \
    --eval-num-processes=10 \
    --hidden-dim=256 \
    --il-in-action-norm=True \
    --il-out-action-norm=True \
    --log-interval=200 \
    --lr=0.00005 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --save-interval=20000 \
    --traj-load-path=./expert_datasets/maze2d_100.pt \
    --vid-fps=60 \
    --traj-batch-size 128 \
    --scheduler-type sigmoid \
    --prefix=dbc \
    --seed=2

python dbc/main.py \
    --alg=dbc \
    --bc-num-epochs=2000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --coeff=30 \
    --coeff-bc=1 \
    --cuda=True \
    --ddpm-path=./rl-toolkit/dm/trained_models/maze2d_100_ddpm_0.0001_128_sigmoid_norm.pt \
    --depth=3 \
    --env-name=maze2d-medium-v2 \
    --eval-interval=2000 \
    --eval-num-processes=10 \
    --hidden-dim=256 \
    --il-in-action-norm=True \
    --il-out-action-norm=True \
    --log-interval=200 \
    --lr=0.00005 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --save-interval=20000 \
    --traj-load-path=./expert_datasets/maze2d_100.pt \
    --vid-fps=60 \
    --traj-batch-size 128 \
    --scheduler-type sigmoid \
    --prefix=dbc \
    --seed=3