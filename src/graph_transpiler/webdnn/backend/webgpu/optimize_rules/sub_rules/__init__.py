from webdnn.backend.webgpu.optimize_rules.sub_rules import concat_lstm_input_and_hidden
from webdnn.backend.webgpu.optimize_rules.sub_rules import replace_convolution_by_im2col
from webdnn.backend.webgpu.optimize_rules.sub_rules import replace_deconvolution_by_col2im
from webdnn.backend.webgpu.optimize_rules.sub_rules import replace_linear_by_sgemm