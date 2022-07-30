import pandas as pd
import random
random.seed(0)

gpt2_1542m = pd.read_json("./data/gpt-2-output-dataset/data/xl-1542M-k40.train.jsonl", lines=True)
webtext_train = pd.read_json("./data/gpt-2-output-dataset/data/webtext.train.jsonl", lines=True)

dataset = [(a, 1) for a in list(gpt2_1542m['text'])]
dataset.extend([(a, 0) for a in list(webtext_train['text'])])
random.shuffle(dataset)


# DO IT MANUALLY IF YOU HAVE TO, SILLY.