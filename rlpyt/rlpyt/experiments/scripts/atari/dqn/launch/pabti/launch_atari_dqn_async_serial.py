
from rlpyt.utils.launching.affinity import encode_affinity
from rlpyt.utils.launching.exp_launcher import run_experiments
from rlpyt.utils.launching.variant import make_variants, VariantLevel

script = "rlpyt/experiments/scripts/atari/dqn/train/atari_dqn_async_serial.py"
affinity_code = encode_affinity(
    n_cpu_core=24,
    n_gpu=8,
    async_sample=True,
    sample_gpu_per_run=0,
    gpu_per_run=1,
    hyperthread_offset=24,
    # n_socket=2,
)
runs_per_setting = 2
experiment_title = "atari_dqn_async_serial"
variant_levels = list()

games = ["pong", "seaquest", "qbert", "chopper_command"]
values = list(zip(games))
dir_names = ["{}".format(*v) for v in values]
keys = [("env", "game")]
variant_levels.append(VariantLevel(keys, values, dir_names))

variants, log_dirs = make_variants(*variant_levels)

default_config_key = "cpu"  # "serial"

run_experiments(
    script=script,
    affinity_code=affinity_code,
    experiment_title=experiment_title,
    runs_per_setting=runs_per_setting,
    variants=variants,
    log_dirs=log_dirs,
    common_args=(default_config_key,),
)
