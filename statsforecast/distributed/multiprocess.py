# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/distributed.multiprocess.ipynb.

# %% auto 0
__all__ = ['MultiprocessBackend']

# %% ../../nbs/distributed.multiprocess.ipynb 4
from typing import Any

from ..core import StatsForecast
from .core import ParallelBackend

# %% ../../nbs/distributed.multiprocess.ipynb 5
# This parent class holds common `forecast` and `cross_validation` methods 
# from `core.StatsForecast` to enable the `FugueBackend` and the `RayBackend`.

# This Parent class is inherited by [FugueBakend](https://nixtla.github.io/statsforecast/distributed.fugue.html) 
# and [RayBackend](https://nixtla.github.io/statsforecast/distributed.ray.html).

class MultiprocessBackend(ParallelBackend):
    """MultiprocessBackend Parent Class for Distributed Computation.

    **Parameters:**<br>
    `n_jobs`: int, number of jobs used in the parallel processing, use -1 for all cores.<br>

    **Notes:**<br>
    
    """
    def __init__(self, n_jobs: int) -> None:
        self.n_jobs = n_jobs
        super().__init__()

    def forecast(self, df, models, freq, fallback_model=None, **kwargs: Any) -> Any:
        model = StatsForecast(df=df, models=models, freq=freq, 
                              fallback_model=fallback_model, n_jobs=self.n_jobs)
        return model.forecast(**kwargs)

    def cross_validation(self, df, models, freq, fallback_model=None, **kwargs: Any) -> Any:
        model = StatsForecast(df=df, models=models, freq=freq, 
                              fallback_model=fallback_model, n_jobs=self.n_jobs)
        return model.cross_validation(**kwargs)
