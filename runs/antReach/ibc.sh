python dbc/main.py \
    --alg=ibc \
    --ant-noise=0.01 \
    --bc-num-epochs=30000 \
    --bc-state-norm=False \
    --clip-actions=True \
    --cuda=True \
    --depth=1 \
    --env-name=AntGoal-v0 \
    --eval-interval=100000 \
    --eval-num-processes=10 \
    --hidden-dim=1200 \
    --il-in-action-norm=False \
    --il-out-action-norm=False \
    --log-interval=200 \
    --lr=5e-05 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --prefix=ibc \
    --save-interval=100000 \
    --seed=1 \
    --traj-frac=1 \
    --traj-load-path=./expert_datasets/ant_10000.pt \
    --vid-fps=100

python dbc/main.py \
    --alg=ibc \
    --ant-noise=0.01 \
    --bc-num-epochs=30000 \
    --bc-state-norm=False \
    --clip-actions=True \
    --cuda=True \
    --depth=1 \
    --env-name=AntGoal-v0 \
    --eval-interval=100000 \
    --eval-num-processes=10 \
    --hidden-dim=1200 \
    --il-in-action-norm=False \
    --il-out-action-norm=False \
    --log-interval=200 \
    --lr=5e-05 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --prefix=ibc \
    --save-interval=100000 \
    --seed=2 \
    --traj-frac=1 \
    --traj-load-path=./expert_datasets/ant_10000.pt \
    --vid-fps=100

python dbc/main.py \
    --alg=ibc \
    --ant-noise=0.01 \
    --bc-num-epochs=30000 \
    --bc-state-norm=False \
    --clip-actions=True \
    --cuda=True \
    --depth=1 \
    --env-name=AntGoal-v0 \
    --eval-interval=100000 \
    --eval-num-processes=10 \
    --hidden-dim=1200 \
    --il-in-action-norm=False \
    --il-out-action-norm=False \
    --log-interval=200 \
    --lr=5e-05 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --prefix=ibc \
    --save-interval=100000 \
    --seed=3 \
    --traj-frac=1 \
    --traj-load-path=./expert_datasets/ant_10000.pt \
    --vid-fps=100