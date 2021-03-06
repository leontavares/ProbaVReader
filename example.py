

import matplotlib.pyplot as plt

from ProbaVReader import probav_toc_hdf5_reader



if __name__ == '__main__':

    fname_300m = '/data/MTDA/PROBAV_L3_S1_TOC_333M/2020/20200616/PROBAV_S1_TOC_20200616_333M_V101/PROBAV_S1_TOC_X17Y03_20200616_333M_V101.HDF5'

    fname_100m = '/data/MTDA/PROBAV_L3_S5_TOC_100M/2020/20200616/PROBAV_S5_TOC_20200616_100M_V101/PROBAV_S5_TOC_X17Y03_20200616_100M_V101.HDF5'


    array, sc_info = probav_toc_hdf5_reader(fname_300m, 'NIR', camera='VNIR')


    # sc_info is adictionary with the scale_factor and add_offset to descale the dataset
    print(sc_info)
    # accessing scale_factor
    print(sc_info['scale_factor'])


    plt.close('all')

    plt.imshow(array)

