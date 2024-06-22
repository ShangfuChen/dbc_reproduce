python dbc/main.py \
    --alg=ibc \
    --bc-num-epochs=10000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --depth=2 \
    --env-name=HalfCheetah-v3 \
    --eval-interval=4000 \
    --eval-num-processes=10 \
    --hidden-dim=512 \
    --log-interval=200 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=3 \
    --num-render=0 \
    --prefix=ibc \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/halfcheetah_5trajs_processed.pt \
    --vid-fps=100 \
    --seed=1

python dbc/main.py \
    --alg=ibc \
    --bc-num-epochs=10000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --depth=2 \
    --env-name=HalfCheetah-v3 \
    --eval-interval=4000 \
    --eval-num-processes=10 \
    --hidden-dim=512 \
    --log-interval=200 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=3 \
    --num-render=0 \
    --prefix=ibc \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/halfcheetah_5trajs_processed.pt \
    --vid-fps=100 \
    --seed=2

python dbc/main.py \
    --alg=ibc \
    --bc-num-epochs=10000 \
    --bc-state-norm=True \
    --clip-actions=True \
    --cuda=True \
    --depth=2 \
    --env-name=HalfCheetah-v3 \
    --eval-interval=4000 \
    --eval-num-processes=10 \
    --hidden-dim=512 \
    --log-interval=200 \
    --lr=0.0001 \
    --normalize-env=False \
    --num-eval=3 \
    --num-render=0 \
    --prefix=ibc \
    --save-interval=100000 \
    --traj-load-path=./expert_datasets/halfcheetah_5trajs_processed.pt \
    --vid-fps=100 \
    --seed=3