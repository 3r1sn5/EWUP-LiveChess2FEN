import tensorrt as trt
import os

TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
trt_runtime = trt.Runtime(TRT_LOGGER)

def build_engine(onnx_path, engine_path, input_shape):
    """Builds a TensorRT engine from an ONNX file."""
    with trt.Builder(TRT_LOGGER) as builder, builder.create_network(1) as network, trt.OnnxParser(network, TRT_LOGGER) as parser:
        builder.max_workspace_size = 1 << 30 # 1GB
        builder.max_batch_size = 1
        builder.fp16_mode = True

        with open(onnx_path, 'rb') as model:
            if not parser.parse(model.read()):
                for error in range(parser.num_errors):
                    print(parser.get_error(error))
                return None
        
        network.get_input(0).shape = input_shape

        engine = builder.build_cuda_engine(network)
        with open(engine_path, "wb") as f:
            f.write(engine.serialize())

        return engine

# Example usage:
onnx_path = "/path/to/your/onnx/model.onnx"
engine_path = "/path/to/save/engine.trt"
input_shape = (1, 3, 299, 299)
engine = build_engine(onnx_path, engine_path, input_shape)
if engine:
    print("Engine was built successfully and saved to:", engine_path)
