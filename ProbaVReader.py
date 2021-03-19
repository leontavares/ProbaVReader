import h5py
import numpy as np
import sys

RADIOMETRY_VNIR = {'BLUE': 'LEVEL3/RADIOMETRY/BLUE/TOC',
                   'RED': 'LEVEL3/RADIOMETRY/RED/TOC',
                   'NIR': 'LEVEL3/RADIOMETRY/NIR/TOC', }

GEOMETRY_VNIR = {'VZA': 'LEVEL3/GEOMETRY/VNIR/VZA',
                 'VAA': 'LEVEL3/GEOMETRY/VNIR/VAA',
                 'SZA': 'LEVEL3/GEOMETRY/SZA',
                 'SAA': 'LEVEL3/GEOMETRY/SAA', }

RADIOMETRY_SWIR = {'SWIR': 'LEVEL3/RADIOMETRY/SWIR/TOC', }

GEOMETRY_SWIR = {'VZA': 'LEVEL3/GEOMETRY/SWIR/VZA',
                 'VAA': 'LEVEL3/GEOMETRY/SWIR/VAA',
                 'SZA': 'LEVEL3/GEOMETRY/SZA',
                 'SAA': 'LEVEL3/GEOMETRY/SAA', }

DISPATCHER_VNIR = {'RADIOMETRY': RADIOMETRY_VNIR,
                   'GEOMETRY': GEOMETRY_VNIR,
                   }

DISPATCHER_SWIR = {'RADIOMETRY': RADIOMETRY_SWIR,
                   'GEOMETRY': GEOMETRY_SWIR,
                   }

DISPATCHER = {'VNIR': DISPATCHER_VNIR,
              'SWIR': DISPATCHER_SWIR}


def probav_toc_hdf5_reader(fname, dataset, camera='VNIR'):
    '''

    :param fname: your filename
    :param dataset: the name of the dataset you want to load (raiometry or geometry). PROBA-V TOC
    files provide the following datasets:
        * VNIR camera:
                BLUE
                RED
                NIR
                VZA
                VAA
                SAA
                SAA
        * SWIR camera:
                SWIR
                VZA
                VAA
                SZA
                SAA
    Note: SZA and SZA are the same for both cameras.
    :param camera: VNIR or SWIR
    :return: numpy array with the dataset loaded, dictionary with scaling info
    '''
    print(f'loading {dataset} for {camera} camera')
    scaling_info = {}
    try:
        dataset = DISPATCHER[camera]['RADIOMETRY'][dataset]
    except KeyError:

        try:
            dataset = DISPATCHER[camera]['GEOMETRY'][dataset]
        except KeyError:
            print (f'{dataset} does not exist for {camera} camera')
            sys.exit(1)



    with h5py.File(fname, 'r') as f:
        array = np.array(f[dataset])
        scaling_info['scale_factor'] = f[dataset].attrs['scale_factor'][0]
        scaling_info['add_offset'] = f[dataset].attrs['add_offset'][0]

    return array, scaling_info

