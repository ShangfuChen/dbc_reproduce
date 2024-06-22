python dbc/main.py \
    --alg=bc \
    --bc-num-epochs=1000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --env-name=Walker2d-v3 \
    --eval-interval=1000 \
    --eval-num-processes=10 \
    --log-interval=200 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --prefix=bc \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/walker_5traj_processed.pt \
    --vid-fps=100 \
    --seed=1

python dbc/main.py \
    --alg=bc \
    --bc-num-epochs=1000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --env-name=Walker2d-v3 \
    --eval-interval=1000 \
    --eval-num-processes=10 \
    --log-interval=200 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --prefix=bc \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/walker_5traj_processed.pt \
    --vid-fps=100 \
    --seed=2

python dbc/main.py \
    --alg=bc \
    --bc-num-epochs=1000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --env-name=Walker2d-v3 \
    --eval-interval=1000 \
    --eval-num-processes=10 \
    --log-interval=200 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=10 \
    --num-render=0 \
    --prefix=bc \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/walker_5traj_processed.pt \
    --vid-fps=100 \
    --seed=3