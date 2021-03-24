# %%

import psf
def make_psf():
    args = dict(dims=(4, 4), ex_wavelen=577, em_wavelen=603,
                num_aperture=0.8, refr_index=1,)
    obsvol = psf.PSF(psf.ISOTROPIC | psf.WIDEFIELD, **args) # psf.GAUSSIAN - gaussian emmision
    print(obsvol, end='')  # doctest:+ELLIPSIS
    return obsvol
psf_obj = make_psf()
psf_obj.imshow()
# %%
# %%
