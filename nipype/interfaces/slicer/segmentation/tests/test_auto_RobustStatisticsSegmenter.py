# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.segmentation.specialized import RobustStatisticsSegmenter
def test_RobustStatisticsSegmenter_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    originalImageFileName=dict(position=-3,
    argstr='%s',
    ),
    expectedVolume=dict(argstr='--expectedVolume %f',
    ),
    args=dict(argstr='%s',
    ),
    curvatureWeight=dict(argstr='--curvatureWeight %f',
    ),
    segmentedImageFileName=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    labelValue=dict(argstr='--labelValue %d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    labelImageFileName=dict(position=-2,
    argstr='%s',
    ),
    intensityHomogeneity=dict(argstr='--intensityHomogeneity %f',
    ),
    maxRunningTime=dict(argstr='--maxRunningTime %f',
    ),
    )
    inputs = RobustStatisticsSegmenter.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_RobustStatisticsSegmenter_outputs():
    output_map = dict(segmentedImageFileName=dict(position=-1,
    ),
    )
    outputs = RobustStatisticsSegmenter.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
