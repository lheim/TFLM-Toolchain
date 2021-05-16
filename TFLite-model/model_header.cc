// Automatically created from a TensorFlow Lite flatbuffer using the command:
// xxd -i sine_model.tflite > sine_model_data.cc
// See the README for a full description of the creation process.

// Further additions by a Jupyter notebook.

#include "model_data.h"

// We need to keep the data array aligned on some architectures.
#ifdef __has_attribute
#define HAVE_ATTRIBUTE(x) __has_attribute(x)
#else
#define HAVE_ATTRIBUTE(x) 0
#endif
#if HAVE_ATTRIBUTE(aligned) || (defined(__GNUC__) && !defined(__clang__))
#define DATA_ALIGN_ATTRIBUTE __attribute__((aligned(4)))
#else
#define DATA_ALIGN_ATTRIBUTE
#endif

// Comment with benchmarking settings and time comes here:
