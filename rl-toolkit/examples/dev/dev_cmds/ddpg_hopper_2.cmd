python tests/run_alg.py --prefix ddpg  --use-proper-time-limits --save-interval -1 --alg ddpg --env-log-dir ~/tmp --trans-buffer-size 1000000 --batch-size 128 --lr 1e-3 --critic-lr 1e-3 --num-env-steps 3000000 --noise-std 0.1 --warmup-steps 0 --noise-type gaussian --noise-std 0.1 --n-rnd-steps 10000 --env-name "Hopper-v3" --tau 5e-3 --warmup-steps 1000 --update-every 50 
