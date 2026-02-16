"""
[TR] PyTorch tabanlı Autoencoder mimarisi. Veriyi sıkıştırıp (Encoder) tekrar açarak (Decoder) gürültü paternini öğrenir.
[EN] PyTorch-based Autoencoder architecture. Learns noise patterns by compressing (Encoder) and reconstructing (Decoder) data.
"""
import torch
import torch.nn as nn

class AnomalyDetector(nn.Module):
    def __init__(self, input_dim):
        super(AnomalyDetector, self).__init__()
        # [TR] Encoder: Veriyi 3 boyuttan 2 boyuta düşürerek en önemli özellikleri öğrenir.
        # [EN] Encoder: Learns key features by reducing data from 3 dimensions to 2.
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 8),
            nn.ReLU(),
            nn.Linear(8, 2) 
        )
        # [TR] Decoder: Sıkışmış veriyi orijinal haline geri döndürmeye çalışır.
        # [EN] Decoder: Attempts to reconstruct the compressed data back to its original state.
        self.decoder = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, input_dim)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))