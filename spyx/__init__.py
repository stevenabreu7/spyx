# spyx/__init__.py

import jax
import jax.numpy as jnp
import haiku as hk

from ._version import __version__
from . import nn
from . import axn
from . import fn
from . import data