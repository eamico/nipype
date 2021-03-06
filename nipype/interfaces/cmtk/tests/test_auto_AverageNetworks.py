# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.cmtk.nx import AverageNetworks
def test_AverageNetworks_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    resolution_network_file=dict(),
    out_gexf_groupavg=dict(),
    in_files=dict(mandatory=True,
    ),
    out_gpickled_groupavg=dict(),
    group_id=dict(usedefault=True,
    ),
    )
    inputs = AverageNetworks.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_AverageNetworks_outputs():
    output_map = dict(matlab_groupavgs=dict(),
    gexf_groupavg=dict(),
    gpickled_groupavg=dict(),
    )
    outputs = AverageNetworks.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
