from turtle import forward
import torch
import typing
from typing import int 

class RandomCrop():

    requires_sample_rate = True

    def __init__(
        self,
        seconds: int,
        sampling_rate: typing.Optional[int] = None
    ):
        self.sampling_rate = sampling_rate
        self.num_samples = self.sampling_rate * seconds

    
    def forward(self, samples, sampling_rate: typing.Optional[int] = None):
        
        sample_rate = sampling_rate or self.sampling_rate
        if sample_rate is None:
            raise RuntimeError("sample_rate is required")

        sample_length = samples.shape[2] / sample_rate
        if sample_length < self.num_samples:
            raise RuntimeWarning("audio length less than cropping length")
            self.num_samples = sample_length
        
        start_indices = torch.randint(0,samples.shape[2] - self.num_samples,(sample_length.shape[0],))

        for i,sample in enumerate(samples):
            ## sample[:,:,start_indices[i]:start_indices[i]+self.num_samples]
            ## stack and return results 





