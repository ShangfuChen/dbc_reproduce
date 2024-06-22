python dbc/main.py \
    --alg=dp \
    --bc-num-epochs=10000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --depth=4 \
    --env-name=Walker2d-v3 \
    --eval-interval=20000 \
    --eval-num-processes=10 \
    --hidden-dim=1200 \
    --log-interval=500 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=3 \
    --num-render=0 \
    --prefix=dp \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/walker_5traj_processed.pt \
    --vid-fps=100 \
    --dp-scheduler-type sigmoid \
    --seed=1

python dbc/main.py \
    --alg=dp \
    --bc-num-epochs=10000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --depth=4 \
    --env-name=Walker2d-v3 \
    --eval-interval=20000 \
    --eval-num-processes=10 \
    --hidden-dim=1200 \
    --log-interval=500 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=3 \
    --num-render=0 \
    --prefix=dp \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/walker_5traj_processed.pt \
    --vid-fps=100 \
    --dp-scheduler-type sigmoid \
    --seed=2

python dbc/main.py \
    --alg=dp \
    --bc-num-epochs=10000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --depth=4 \
    --env-name=Walker2d-v3 \
    --eval-interval=20000 \
    --eval-num-processes=10 \
    --hidden-dim=1200 \
    --log-interval=500 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=3 \
    --num-render=0 \
    --prefix=dp \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/walker_5traj_processed.pt \
    --vid-fps=100 \
    --dp-scheduler-type sigmoid \
    --seed=3