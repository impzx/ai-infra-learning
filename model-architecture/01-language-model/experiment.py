"""Python 3, standard library only. Synthetic data; no downloads."""
from collections import Counter, defaultdict
import math

TRAIN = ["我 喜欢 苹果", "我 喜欢 香蕉", "你 喜欢 苹果", "你 讨厌 香蕉",
         "他 喜欢 音乐", "她 喜欢 音乐", "他 讨厌 苹果", "她 讨厌 香蕉"]
VALID = ["我 讨厌 苹果", "你 喜欢 音乐", "她 喜欢 苹果", "他 喜欢 香蕉"]
BOS, EOS, UNK = "<bos>", "<eos>", "<unk>"
# Vocabulary comes only from training data. BOS is context, not an output.
vocab = sorted({w for line in TRAIN for w in line.split()} | {EOS, UNK})
unigram = Counter()
bigram = defaultdict(Counter)
for line in TRAIN:
    prev = BOS
    for word in line.split() + [EOS]:
        unigram[word] += 1
        bigram[prev][word] += 1
        prev = word

def probability(word, prev, model, alpha=1.0):
    if model == "uniform":
        return 1 / len(vocab)
    counts = unigram if model == "unigram" else bigram.get(prev, Counter())
    return (counts[word] + alpha) / (sum(counts.values()) + alpha * len(vocab))

def evaluate(lines, model):
    total_loss, n = 0.0, 0
    for line in lines:
        prev = BOS
        for raw in line.split() + [EOS]:
            word = raw if raw in vocab else UNK
            total_loss -= math.log(probability(word, prev, model))
            n += 1
            prev = word
    return total_loss / n, math.exp(total_loss / n), n

if __name__ == "__main__":
    assert set(TRAIN).isdisjoint(VALID)
    for model in ("uniform", "unigram", "bigram"):
        for prev in [BOS] + vocab:
            assert math.isclose(sum(probability(w, prev, model) for w in vocab), 1.0)
    print(f"vocabulary={len(vocab)}, alpha=1.0, EOS scored, BOS not scored")
    print("model       split   tokens  loss(nats)  perplexity")
    for model in ("uniform", "unigram", "bigram"):
        for split, lines in (("train", TRAIN), ("valid", VALID)):
            loss, ppl, n = evaluate(lines, model)
            print(f"{model:11} {split:5} {n:7d} {loss:11.4f} {ppl:11.4f}")
    print("P(苹果 | 喜欢) =", round(probability("苹果", "喜欢", "bigram"), 6))
    print("P(苹果 | 讨厌) =", round(probability("苹果", "讨厌", "bigram"), 6))
