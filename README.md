![license](https://img.shields.io/badge/license-MIT-blue) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/laurentperrinet/lambda2color/main)
[![PyPI version](https://badge.fury.io/py/lambda2color.svg)](https://badge.fury.io/py/lambda2color)


# lambda2color: convert a given light wavelength into the corresponding RGB color

This is a simple library to transform a given light wavelength into the corresponding RGB color.

It is based on the different sensitivities to a novel color space called the [CIE 193 " XYZ" color space](https://en.wikipedia.org/wiki/CIE_1931_color_space) and defined by the CIE colour matching function for 380 - 780 nm in 5 nm intervals :

![CIE colour matching function](cmf.png)

This allows to simply compute for instance the color of different monochromatic lights:

![Rainbow](spectrum.png)

For more advanced uses, see for instance this blog post computing [the color of the sky](https://laurentperrinet.github.io/sciblog/posts/2020-07-04-colors-of-the-sky.html).