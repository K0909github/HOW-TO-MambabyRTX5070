__version__ = "2.2.4"

from mamba_ssm.ops.selective_scan_interface import selective_scan_fn, mamba_inner_fn
from mamba_ssm.modules.mamba_simple import Mamba

try:
	from mamba_ssm.modules.mamba2 import Mamba2
except Exception:
	Mamba2 = None

# HF/transformers 依存を持つため、環境によっては import できない。
try:
	from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel
except Exception:
	MambaLMHeadModel = None
