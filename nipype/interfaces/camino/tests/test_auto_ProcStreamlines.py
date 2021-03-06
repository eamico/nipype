# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.convert import ProcStreamlines
def test_ProcStreamlines_inputs():
    input_map = dict(outputsc=dict(argstr='-outputsc',
    ),
    mintractlength=dict(units='mm',
    argstr='-mintractlength %d',
    ),
    datadims=dict(units='voxels',
    argstr='-datadims %s',
    ),
    truncateloops=dict(argstr='-truncateloops',
    ),
    mintractpoints=dict(units='NA',
    argstr='-mintractpoints %d',
    ),
    maxtractlength=dict(units='mm',
    argstr='-maxtractlength %d',
    ),
    waypointfile=dict(argstr='-waypointfile %s',
    ),
    outputcbs=dict(argstr='-outputcbs',
    ),
    iterations=dict(units='NA',
    argstr='-iterations %d',
    ),
    outputtracts=dict(argstr='-outputtracts',
    ),
    directional=dict(units='NA',
    argstr='-directional %s',
    ),
    seedfile=dict(argstr='-seedfile %s',
    ),
    seedpointmm=dict(units='mm',
    argstr='-seedpointmm %s',
    ),
    in_file=dict(position=1,
    mandatory=True,
    argstr='-inputfile %s',
    ),
    truncateinexclusion=dict(argstr='-truncateinexclusion',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    endpointfile=dict(argstr='-endpointfile %s',
    ),
    args=dict(argstr='%s',
    ),
    outputroot=dict(argstr='-outputroot %s',
    ),
    maxtractpoints=dict(units='NA',
    argstr='-maxtractpoints %d',
    ),
    targetfile=dict(argstr='-targetfile %s',
    ),
    inputmodel=dict(usedefault=True,
    argstr='-inputmodel %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    seedpointvox=dict(units='voxels',
    argstr='-seedpointvox %s',
    ),
    regionindex=dict(units='mm',
    argstr='-regionindex %d',
    ),
    out_file=dict(position=-1,
    genfile=True,
    argstr='> %s',
    ),
    voxeldims=dict(units='mm',
    argstr='-voxeldims %s',
    ),
    outputcp=dict(argstr='-outputcp',
    ),
    noresample=dict(argstr='-noresample',
    ),
    discardloops=dict(argstr='-discardloops',
    ),
    outputacm=dict(argstr='-outputacm',
    ),
    exclusionfile=dict(argstr='-exclusionfile %s',
    ),
    allowmultitargets=dict(argstr='-allowmultitargets',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    gzip=dict(argstr='-gzip',
    ),
    resamplestepsize=dict(units='NA',
    argstr='-resamplestepsize %d',
    ),
    )
    inputs = ProcStreamlines.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ProcStreamlines_outputs():
    output_map = dict(proc=dict(),
    )
    outputs = ProcStreamlines.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
