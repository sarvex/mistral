name: Run Tests: Train
on: [push]
jobs:
  Run-Mistral-Tests-Train:
    runs-on: self-hosted
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v2
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: Run mistral tests
        run: |
          # set up test environment
          bash
          . /home/stanzabuild/miniconda3/etc/profile.d/conda.sh
          conda activate mistral
          # set up wandb in recent checkout dir
          cp -r /home/stanzabuild/mistral/wandb .
          export PYTHONPATH=/home/stanzabuild/github-actions/actions-runner/_work/mistral/mistral
          export MISTRAL_TEST_DIR=/home/stanzabuild/mistral-test-dir
          cd tests
          wandb offline
          CUDA_VISIBLE_DEVICES=0 pytest test_train.py
      - run: echo "🍏 This job's status is ${{ job.status }}."