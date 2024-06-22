from .maze_model import MazeEnv, MazeImgEnv, OPEN, U_MAZE, MEDIUM_MAZE, LARGE_MAZE, U_MAZE_EVAL, MEDIUM_MAZE_EVAL, LARGE_MAZE_EVAL
from .maze_toy import MazeToy, OPEN
from .maze_gen import MazeGen, GEN
from .maze_gen1 import MazeGen1
from .maze_gen2 import MazeGen2
from .maze_gen3 import MazeGen3
from .maze_gen4 import MazeGen4
from .maze_gen_eval import MazeGenEval
from .maze_gen_eval1 import MazeGenEval1
from .maze_gen_eval2 import MazeGenEval2
from .maze_gen_eval3 import MazeGenEval3
from .maze_gen_eval4 import MazeGenEval4
from .maze_gen_far_goal_eval import MazeGenFarGoalEval
from .maze_gen_far_goal_eval1 import MazeGenFarGoalEval1
from .maze_gen_far_goal_eval2 import MazeGenFarGoalEval2
from .maze_gen_far_goal_eval3 import MazeGenFarGoalEval3
from .maze_gen_far_goal_eval4 import MazeGenFarGoalEval4
from .maze_gen_diff_eval import MazeGenDiffEval
from .maze_gen_diff_eval1 import MazeGenDiffEval1
from .maze_gen_diff_eval2 import MazeGenDiffEval2
from .maze_gen_diff_eval3 import MazeGenDiffEval3
from .maze_gen_diff_eval4 import MazeGenDiffEval4
from .maze_gen_near_eval import MazeGenNearEval
from .maze_gen_near_eval1 import MazeGenNearEval1
from .maze_gen_near_eval2 import MazeGenNearEval2
from .maze_gen_near_eval3 import MazeGenNearEval3
from .maze_gen_near_eval4 import MazeGenNearEval4
from .maze_gen_near import MazeGenNear
from .maze_gen_near1 import MazeGenNear1
from .maze_gen_near2 import MazeGenNear2
from .maze_gen_near3 import MazeGenNear3
from .maze_gen_near4 import MazeGenNear4

from .maze_gen_far_eval import MazeGenFarEval
from .maze_gen_far_eval1 import MazeGenFarEval1
from .maze_gen_far_eval2 import MazeGenFarEval2
from .maze_gen_far_eval3 import MazeGenFarEval3
from .maze_gen_far_eval4 import MazeGenFarEval4
from .maze_gen_far import MazeGenFar
from .maze_gen_far1 import MazeGenFar1
from .maze_gen_far2 import MazeGenFar2
from .maze_gen_far3 import MazeGenFar3
from .maze_gen_far4 import MazeGenFar4


from gym.envs.registration import register

register(
    id='maze2d-open-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':OPEN,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 0.01,
        'ref_max_score': 20.66,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-sparse.hdf5'
    }
)

register(
    id='maze2d-umaze-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 0.94,
        'ref_max_score': 62.6,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-sparse.hdf5'
    }
)

register(
    id='maze2d-medium-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=250,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 5.77,
        'ref_max_score': 85.14,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse.hdf5'
    }
)


register(
    id='maze2d-large-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse.hdf5'
    }
)


register(
    id='maze2d-umaze-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 23.85,
        'ref_max_score': 161.86,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-medium-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'sparse',
        'reset_target': True,
        'ref_min_score': 13.13,
        'ref_max_score': 277.39,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5'
    }
)


register(
    id='maze2d-medium-v2',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=400,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 13.13,
        'ref_max_score': 277.39,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-medium-img-v2',
    entry_point='d4rl.pointmaze:MazeImgEnv',
    max_episode_steps=400,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 13.13,
        'ref_max_score': 277.39,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-large-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 6.7,
        'ref_max_score': 273.99,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-eval-umaze-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE_EVAL,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 36.63,
        'ref_max_score': 141.4,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-umaze-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-eval-medium-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE_EVAL,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 13.07,
        'ref_max_score': 204.93,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-medium-sparse-v1.hdf5'
    }
)


register(
    id='maze2d-eval-large-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE_EVAL,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 16.4,
        'ref_max_score': 302.22,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-large-sparse-v1.hdf5'
    }
)


register(
    id='maze2d-open-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':OPEN,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-toy-v0',
    entry_point='d4rl.pointmaze:MazeToy',
    max_episode_steps=200,
    kwargs={
        'maze_spec':OPEN,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-generalize-v0',
    entry_point='d4rl.pointmaze:MazeGen',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-generalize-v1',
    entry_point='d4rl.pointmaze:MazeGen1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-generalize-v2',
    entry_point='d4rl.pointmaze:MazeGen2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-generalize-v3',
    entry_point='d4rl.pointmaze:MazeGen3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-generalize-v4',
    entry_point='d4rl.pointmaze:MazeGen4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-eval-v0',
    entry_point='d4rl.pointmaze:MazeGenEval',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-eval-v1',
    entry_point='d4rl.pointmaze:MazeGenEval1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-eval-v2',
    entry_point='d4rl.pointmaze:MazeGenEval2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-eval-v3',
    entry_point='d4rl.pointmaze:MazeGenEval3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-eval-v4',
    entry_point='d4rl.pointmaze:MazeGenEval4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-goal-eval-v0',
    entry_point='d4rl.pointmaze:MazeGenFarGoalEval',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-goal-eval-v1',
    entry_point='d4rl.pointmaze:MazeGenFarGoalEval1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-goal-eval-v2',
    entry_point='d4rl.pointmaze:MazeGenFarGoalEval2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-goal-eval-v3',
    entry_point='d4rl.pointmaze:MazeGenFarGoalEval3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-goal-eval-v4',
    entry_point='d4rl.pointmaze:MazeGenFarGoalEval4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-diff-eval-v0',
    entry_point='d4rl.pointmaze:MazeGenDiffEval',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-diff-eval-v1',
    entry_point='d4rl.pointmaze:MazeGenDiffEval1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-diff-eval-v2',
    entry_point='d4rl.pointmaze:MazeGenDiffEval2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-diff-eval-v3',
    entry_point='d4rl.pointmaze:MazeGenDiffEval3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-diff-eval-v4',
    entry_point='d4rl.pointmaze:MazeGenDiffEval4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-eval-v0',
    entry_point='d4rl.pointmaze:MazeGenNearEval',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-eval-v1',
    entry_point='d4rl.pointmaze:MazeGenNearEval1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-eval-v2',
    entry_point='d4rl.pointmaze:MazeGenNearEval2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-eval-v3',
    entry_point='d4rl.pointmaze:MazeGenNearEval3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-eval-v4',
    entry_point='d4rl.pointmaze:MazeGenNearEval4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-v0',
    entry_point='d4rl.pointmaze:MazeGenNear',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-v1',
    entry_point='d4rl.pointmaze:MazeGenNear1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-v2',
    entry_point='d4rl.pointmaze:MazeGenNear2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-v3',
    entry_point='d4rl.pointmaze:MazeGenNear3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-near-v4',
    entry_point='d4rl.pointmaze:MazeGenNear4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-eval-v0',
    entry_point='d4rl.pointmaze:MazeGenFarEval',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-eval-v1',
    entry_point='d4rl.pointmaze:MazeGenFarEval1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-eval-v2',
    entry_point='d4rl.pointmaze:MazeGenFarEval2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-eval-v3',
    entry_point='d4rl.pointmaze:MazeGenFarEval3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-eval-v4',
    entry_point='d4rl.pointmaze:MazeGenFarEval4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-v0',
    entry_point='d4rl.pointmaze:MazeGenFar',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-v1',
    entry_point='d4rl.pointmaze:MazeGenFar1',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-v2',
    entry_point='d4rl.pointmaze:MazeGenFar2',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-v3',
    entry_point='d4rl.pointmaze:MazeGenFar3',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-gen-far-v4',
    entry_point='d4rl.pointmaze:MazeGenFar4',
    max_episode_steps=300,
    kwargs={
        'maze_spec':GEN,
        'reward_type':'dense',
        'reset_target': True,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-umaze-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 23.249793,
        'ref_max_score': 81.78995240126592,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-dense.hdf5'
    }
)

register(
    id='maze2d-medium-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=250,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 19.477620,
        'ref_max_score': 96.03474232952358,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-dense.hdf5'
    }
)


register(
    id='maze2d-large-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 27.388310,
        'ref_max_score': 215.09965671563742,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-dense.hdf5'
    }
)

register(
    id='maze2d-umaze-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 68.537689,
        'ref_max_score': 193.66285642381482,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-dense-v1.hdf5'
    }
)

register(
    id='maze2d-medium-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 44.264742,
        'ref_max_score': 297.4552547777125,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-dense-v1.hdf5'
    }
)


register(
    id='maze2d-large-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 30.569041,
        'ref_max_score': 303.4857382709002,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-dense-v1.hdf5'
    }
)

register(
    id='maze2d-eval-umaze-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE_EVAL,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 56.95455,
        'ref_max_score': 178.21373133248397,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-umaze-dense-v1.hdf5'
    }
)

register(
    id='maze2d-eval-medium-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE_EVAL,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 42.28578,
        'ref_max_score': 235.5658957482388,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-medium-dense-v1.hdf5'
    }
)


register(
    id='maze2d-eval-large-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE_EVAL,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 56.95455,
        'ref_max_score': 326.09647655082637,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-large-dense-v1.hdf5'
    }
)
