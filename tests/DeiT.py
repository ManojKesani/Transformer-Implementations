from models.transformer import DeiT

import torch
import torch.nn as nn

torch.manual_seed(0)


def test_out_size(img_size=28, patch_size=7, channel_size=3, n_classes=10, batch_size=2, device="cpu"):
    x = torch.rand(batch_size, channel_size, img_size, img_size).to(device)

    embed_size = 512
    num_heads = 8
    num_layers = 2
    hidden_size = 256
    dropout = 0.2

    model = DeiT(img_size,
                 channel_size,
                 patch_size,
                 embed_size,
                 num_heads,
                 n_classes,
                 num_layers,
                 hidden_size,
                 dropout=dropout
                 ).to(device)

    y = model(x)

    assert list(y.size()) == [batch_size, n_classes], "Output Size Incorrect"

    del model
    del x
    del y
    torch.cuda.empty_cache()


if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    test_out_size(90, device=device)
    test_out_size(100, device=device)
    test_out_size(110, device=device)
