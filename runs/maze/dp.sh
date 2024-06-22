python dbc/main.py \
    --alg=dp \
    --bc-num-epochs=20000 \
    --bc-state-norm=False \
    --clip-actions=True \
    --cuda=True \
    --depth=4 \
    --env-name=maze2d-medium-v2 \
    --eval-interval=55000 \
    --eval-num-processes=20 \
    --hidden-dim=256 \
    --il-in-action-norm=False \
    --il-out-action-norm=False \
    --log-interval=5000 \
    --lr=0.0002 \
    --normalize-env=False \
    --num-eval=5 \
    --num-render=0 \
    --prefix=dp \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/maze2d_100.pt \
    --vid-fps=30 \
    --seed=1

python dbc/main.py \
    --alg=dp \
    --bc-num-epochs=20000 \
    --bc-state-norm=False \
    --clip-actions=True \
    --cuda=True \
    --depth=4 \
    --env-name=maze2d-medium-v2 \
    --eval-interval=55000 \
    --eval-num-processes=20 \
    --hidden-dim=256 \
    --il-in-action-norm=False \
    --il-out-action-norm=False \
    --log-interval=5000 \
    --lr=0.0002 \
    --normalize-env=False \
    --num-eval=5 \
    --num-render=0 \
    --prefix=dp \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/maze2d_100.pt \
    --vid-fps=30 \
    --seed=2

python dbc/main.py \
    --alg=dp \
    --bc-num-epochs=20000 \
    --bc-state-norm=False \
    --clip-actions=True \
    --cuda=True \
    --depth=4 \
    --env-name=maze2d-medium-v2 \
    --eval-interval=55000 \
    --eval-num-processes=20 \
    --hidden-dim=256 \
    --il-in-action-norm=False \
    --il-out-action-norm=False \
    --log-interval=5000 \
    --lr=0.0002 \
    --normalize-env=False \
    --num-eval=5 \
    --num-render=0 \
    --prefix=dp \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/maze2d_100.pt \
    --vid-fps=30 \
    --seed=3