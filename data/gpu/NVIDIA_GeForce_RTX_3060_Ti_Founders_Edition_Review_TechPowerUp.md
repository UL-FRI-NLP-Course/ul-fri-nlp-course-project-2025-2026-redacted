# NVIDIA GeForce RTX 3060 Ti Founders Edition Review | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: NVIDIA Logo]

NVIDIA today released the GeForce RTX 3060 Ti, its fourth gaming graphics card based on their latest Ampere graphics architecture, targeting a wider market with its reduced price point. The RTX 3060 Ti debuts at a starting price of $400 and logically succeeds the RTX 2060 Super from the previous generation, which too launched at this price. We have with us for review the NVIDIA GeForce RTX 3060 Ti Founders Edition graphics card. NVIDIA designed the RTX 3060 Ti to offer smooth AAA gaming at the 1440p resolution, with additional horsepower for RTX raytracing. It should also serve as a gateway to 4K UHD resolution without raytracing or DLSS enabled, and should cater to the e-sports crowd, offering 1080p gaming at higher refresh rates, such as 144 Hz. 


The GeForce RTX 3060 Ti is based on the same 8 nm "GA104" silicon as the RTX 3070, but with less of the shaders on the silicon enabled. It still ends up with more than double the number of CUDA cores as the RTX 2060 Super. NVIDIA claims that the RTX 3060 Ti is faster than the previous-generation RTX 2080 Super, which is a $700 high-end graphics card that fits the bill for 1440p + raytracing. All this is made possible because of the design goal with "Ampere"—to make RTX-on gameplay as fast as RTX-off gameplay on previous-generation cards given RTX raytracing remains an extremely compute-intensive technology that impacts performance in a big way. The obvious dividend of this approach would be a significant boost in non-raytraced (purely raster 3D) performance.


NVIDIA's GeForce Ampere graphics architecture marks the introduction of the 2nd generation RTX real-time raytracing technology. Pure raytraced 3D graphics may still be outside our reach, but it's possible to combine traditional raster 3D graphics with certain real-time raytraced elements, such as lighting, shadows, reflections, and global illumination. Even this much takes an enormous amount of compute power, and so NVIDIA innovated fixed-function hardware we will detail on the next page. The 2nd generation RTX combines new "Ampere" CUDA cores that offer concurrent FP32+INT32 math operations, with 2nd generation RT cores, which offer higher BVH traversal and intersection performance and new hardware that enabled raytraced motion blur; and the new 3rd generation Tensor core that leverages the sparsity phenomenon in deep-learning neural nets to improve AI inference performance by an order of magnitude over the previous generation. 


NVIDIA carved the GeForce RTX 3060 Ti out of the "GA104" silicon by enabling 38 out of 48 streaming multiprocessors physically present on the silicon, resulting in 4,864 CUDA cores, 38 2nd generation RT cores, 152 3rd generation Tensor cores, 152 TMUs, and 80 ROPs. The CUDA core count has been increased by a staggering 123% over the RTX 2060 Super. The GPU clock speeds are roughly the same as those on the RTX 2060 Super, and yet typical board power isn't much higher with NVIDIA rating it at 200 W. This should mean that custom-design graphics cards with single 8-pin PCIe power connectors should be possible. The GPU is endowed with the same exact memory configuration as the RTX 3070: 8 GB of GDDR6 memory running at 14 Gbps across a 256-bit wide memory interface. This works out to 448 GB/s of bandwidth. 


The NVIDIA GeForce RTX 3060 Ti Founders Edition is a beautiful rendition of the RTX 3060 Ti by its makers. The Founders Edition series of graphics cards by NVIDIA aren't exactly meant to serve as a baseline for the company's add-in card (AIC) partners to build on, but rather sets a high benchmark in product design for board partners to aspire to reach or beat. The RTX 3060 Ti Founders Edition looks almost identical in design to the RTX 3070 Founders Edition, but the color of the metal cooler frame differs slightly. 


With its RTX 30-series Founders Edition cards, NVIDIA reduced the role of the cooler shroud to the frame, and lets exposed heatsinks make up most of the card's outer design. The card is longer than the PCB underneath, so airflow from the second fan flows unimpeded through the heatsink and out through a large vent on the backplate. The card uses the same 12-pin Molex MicroFit 3.0 power input as the other RTX 30-series FE cards, and an adapter is included to convert a single 8-pin PCIe input. In this review, we explore whether the RTX 3060 Ti is all you'll ever need if you're gaming at 1440p or below.


| | Price | Shader Units | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
| RTX 2060 | $300 | 1920 | 48 | 1365 MHz | 1680 MHz | 1750 MHz | TU106 | 10800M | 6 GB, GDDR6, 192-bit |
| RX 5700 | $330 | 2304 | 64 | 1465 MHz | 1625 MHz | 1750 MHz | Navi 10 | 10300M | 8 GB, GDDR6, 256-bit |
| GTX 1080 | $330 | 2560 | 64 | 1607 MHz | 1733 MHz | 1251 MHz | GP104 | 7200M | 8 GB, GDDR5X, 256-bit |
| RTX 2060 Super | $380 | 2176 | 64 | 1470 MHz | 1650 MHz | 1750 MHz | TU106 | 10800M | 8 GB, GDDR6, 256-bit |
| RX Vega 64 | $400 | 4096 | 64 | 1247 MHz | 1546 MHz | 953 MHz | Vega 10 | 12500M | 8 GB, HBM2, 2048-bit |
| GTX 1080 Ti | $650 | 3584 | 88 | 1481 MHz | 1582 MHz | 1376 MHz | GP102 | 12000M | 11 GB, GDDR5X, 352-bit |
| RX 5700 XT | $370 | 2560 | 64 | 1605 MHz | 1755 MHz | 1750 MHz | Navi 10 | 10300M | 8 GB, GDDR6, 256-bit |
| RTX 2070 | $340 | 2304 | 64 | 1410 MHz | 1620 MHz | 1750 MHz | TU106 | 10800M | 8 GB, GDDR6, 256-bit |
| RTX 2070 Super | $450 | 2560 | 64 | 1605 MHz | 1770 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| Radeon VII | $680 | 3840 | 64 | 1802 MHz | N/A | 1000 MHz | Vega 20 | 13230M | 16 GB, HBM2, 4096-bit |
| RTX 2080 | $600 | 2944 | 64 | 1515 MHz | 1710 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 2080 Super | $690 | 3072 | 64 | 1650 MHz | 1815 MHz | 1940 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 3060 Ti | $400 | 4864 | 80 | 1410 MHz | 1665 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RTX 2080 Ti | $1000 | 4352 | 88 | 1350 MHz | 1545 MHz | 1750 MHz | TU102 | 18600M | 11 GB, GDDR6, 352-bit |
| RTX 3070 | $500 | 5888 | 96 | 1500 MHz | 1725 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RX 6800 | $580 | 3840 | 96 | 1815 MHz | 2105 MHz | 2000 MHz | Navi 21 | 23000M | 16 GB, GDDR6, 256-bit |
| RX 6800 XT | $650 | 4608 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 23000M | 16 GB, GDDR6, 256-bit |
| RTX 3080 | $700 | 8704 | 96 | 1440 MHz | 1710 MHz | 1188 MHz | GA102 | 28000M | 10 GB, GDDR6X, 320-bit |
