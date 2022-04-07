# Biomedical downstream evaluation

## Dependencies
```bash
pip install torch==1.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
pip install transformers==4.9.1 datasets==1.11.0 wandb sklearn seqeval
```

## Usage
For PubMedQA, go to `seqcls/` and run the following command:

```bash
task=pubmedqa_hf
datadir=data/$task
outdir=runs/$task/GPT2
mkdir -p $outdir
python3 -u run_seqcls_gpt.py --tokenizer_name gpt2 --model_name_or_path gpt2 \
  --train_file $datadir/train.json --validation_file $datadir/dev.json --test_file $datadir/test.json \
  --do_train --do_eval --do_predict --per_device_train_batch_size 16 --gradient_accumulation_steps 1 --fp16 \
  --learning_rate 2e-5 --warmup_steps 100 --num_train_epochs 30  --max_seq_length 512  --logging_steps 100 \
  --save_strategy no --evaluation_strategy no --output_dir $outdir --overwrite_output_dir \
  |& tee $outdir/log.txt &
```

For NER tasks (EBM-PICO, BC5CDR-disease), go to `tokcls/` and run the following command:
```bash
task=ebmnlp_hf
datadir=data/$task
outdir=runs/$task/GPT2
mkdir -p $outdir
python3 -u run_ner.py --tokenizer_name gpt2 --model_name_or_path gpt2 \
  --train_file $datadir/train.json --validation_file $datadir/dev.json --test_file $datadir/test.json \
  --do_train --do_eval --do_predict --per_device_train_batch_size 32 --gradient_accumulation_steps 1 --fp16 \
  --learning_rate 5e-5 --warmup_steps 100 --num_train_epochs 1  --max_seq_length 512  --logging_steps 100 \
  --save_strategy no --evaluation_strategy no --output_dir $outdir --overwrite_output_dir \
  --return_macro_metrics \
  |& tee $outdir/log.txt &
```
```bash
task=BC5CDR-disease_hf
datadir=data/$task
outdir=runs/$task/GPT2
mkdir -p $outdir
python3 -u run_ner.py --tokenizer_name gpt2 --model_name_or_path gpt2 \
  --train_file $datadir/train.json --validation_file $datadir/dev.json --test_file $datadir/test.json \
  --do_train --do_eval --do_predict --per_device_train_batch_size 16 --gradient_accumulation_steps 1 --fp16 \
  --learning_rate 5e-5 --warmup_steps 100 --num_train_epochs 20  --max_seq_length 512  --logging_steps 100 \
  --save_strategy no --evaluation_strategy no --output_dir $outdir --overwrite_output_dir \
  |& tee $outdir/log.txt &
```