from pathlib import Path

import numpy as np

from tests import MISTRAL_TEST_DIR, run_tests, run_train_process, get_samples, check_samples_equal
import json

# common paths and resources for tests

# paths
CACHE_DIR = f"{MISTRAL_TEST_DIR}/artifacts"
RUNS_DIR = f"{MISTRAL_TEST_DIR}/runs"
RUN_ID = "eval_test"

# run training processes for tests
TRAIN_ARGS = {
    "nnodes": "1",
    "nproc_per_node": "1",
    "file": "conf/train.yaml",
    "training_arguments.fp16": "false",
    "training_arguments.max_steps": "3",
    "training_arguments.per_device_train_batch_size": "1",
    "artifacts.cache_dir": CACHE_DIR,
    "log_level": "20",
    "effective_bsz": "16",
    "run_final_eval": "true",
    "training_arguments.dataloader_num_workers": "0",
}

trainer_after_training = run_train_process(cl_args_dict=TRAIN_ARGS, runs_dir=RUNS_DIR, run_id=RUN_ID)


def test_eval_works() -> None:
    # mostly want to ensure it doesn't crash, but also want to be sure eval does what we want
    metrics = Path(RUNS_DIR) / RUN_ID / "final-metrics.json"
    with open(metrics, 'r') as f:
        metrics = json.load(f)
    base_ppl = metrics["eval/wikitext2_ppl"]
    clone_ppl = metrics["eval/wikitext2_clone_ppl"]
    assert np.isclose(base_ppl, clone_ppl)


if __name__ == "__main__":
    run_tests()