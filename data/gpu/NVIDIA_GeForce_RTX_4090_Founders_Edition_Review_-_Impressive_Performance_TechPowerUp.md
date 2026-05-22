# NVIDIA GeForce RTX 4090 Founders Edition Review - Impressive Performance | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: NVIDIA Logo]

NVIDIA GeForce RTX 4090 "Ada Lovelace" turns the page, introducing a new generation of graphics hardware that promises not just fast gaming performance, but also makes real time ray tracing practically "free." In this RTX 4090 Founders Edition review we'll see that besides a big generational performance uplift, Ada also promises revolutionary improvements to NVIDIA's DLSS capability—generating entire frames only using AI, without involving the GPU's main graphics rendering machinery. This in itself is so significant, that the company is referring to it as "neural rendering," and placing it alongside the two other key graphics rendering techniques—rasterization and ray tracing. With the new GeForce RTX 4090, NVIDIA is promising a generational performance uplift of the kind we were seeing when Moore's Law still worked for GPUs—nearly 50% generation over generation. 


The GeForce "Ada" graphics architecture, named after Ada Lovelace, considered to be the first computer programmer; heralds the 3rd generation RTX real time ray tracing technology, which combines classic raster graphics with certain real-time ray traced elements to significantly improve visual realism. Generationally, Ada enables visual artists and game developers to add even more ray traced effects to their games, and introduces new fixed function hardware to render them. The "Ada" CUDA cores in addition to significant frequency and IPC uplifts over "Ampere," introduce Shader Execution Reordering, a new SIMD optimization that improves the performance of the shader-side of ray tracing by three times, and in-game framerates by 25%. Ada also introduces the 4th generation Tensor Cores, with support for even more math formats such as FP8, improving tensor math performance uplifts by five times over the previous generation. Bringing this all together is the new TSMC 5 nm EUV foundry node that is capable of GPU clock speeds as high as 4 GHz for this generation. 


NVIDIA carved the GeForce RTX 4090 out of the 5 nm "AD102" silicon, its largest for this generation. It is endowed with a massive 16,384 CUDA cores (out of 18,432 present on the silicon), 512 out of 568 Tensor cores, 128 out of 142 RT cores, 512 TMUs and 192 ROPs. The card uses the same 24 GB of GDDR6X memory as the RTX 3090, which ticks at the same 21 Gbps speed as the RTX 3090 Ti, producing 1008 GB/s of bandwidth. There are several innovations made at the silicon level, which we'll detail on the next page of this review; enabling NVIDIA to actually generationally lower the memory bandwidth, as you'll see in the RTX 4080 series, and the other SKUs from this generation. 


The GeForce RTX 4090 is NVIDIA's flagship graphics card for this generation. The company is changing the launch order this time. With the RTX 30-series, NVIDIA launched the RTX 3080 as flagship first, and added the RTX 3090 / 3090 Ti later, as a halo product to replace the TITAN. With Ada, the RTX 4090 debuts this generation, with the RTX 4080 series slated for November 2022. The RTX 40-series launches in an interesting time in the market—cryptocurrency mining is dead, and with it, demand for high-margin flagship GPUs from miners. The PC industry is in a state of slump due to weakened demand; most of the tech industry is trading red; and people's disposable incomes are strained. NVIDIA is positioning the RTX 4090 at $1,599 (baseline MSRP), and pricing for most custom-design boards should be within a few hundred Dollars.


The NVIDIA GeForce RTX 4090 Founders Edition in this review follows a long line of well-designed graphics cards by NVIDIA that are technically custom-design, but are de-facto reference. With this generation, NVIDIA improves upon the Dual Axial Flow Through cooling architecture it introduced with the RTX 30-series "Ampere." While the GPU uses a PCI-Express Gen 4 host interface, its power architecture meets the PCIe Gen 5 standard, with the new 12+4 pin ATX 12VHPWR power connector being standardized across the RTX 4090 series, including with custom-design cards from partners. NVIDIA is placing the RTX 4090 at the baseline price of $1,599. This is the only card we are allowed to publish reviews of today (October 11), you'll have to check back tomorrow for reviews of custom-design 4090s—we'll test eight models, from all the big manufacturers.


| | Price | Cores | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
| RTX 2080 | $400 | 2944 | 64 | 1515 MHz | 1710 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 3060 Ti | $450 | 4864 | 80 | 1410 MHz | 1665 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RX 6700 XT | $410 | 2560 | 64 | 2424 MHz | 2581 MHz | 2000 MHz | Navi 22 | 17200M | 12 GB, GDDR6, 192-bit |
| RX 6750 XT | $470 | 2560 | 64 | 2495 MHz | 2600 MHz | 2250 MHz | Navi 22 | 17200M | 12 GB, GDDR6, 192-bit |
| RTX 2080 Ti | $550 | 4352 | 88 | 1350 MHz | 1545 MHz | 1750 MHz | TU102 | 18600M | 11 GB, GDDR6, 352-bit |
| RTX 3070 | $530 | 5888 | 96 | 1500 MHz | 1725 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RTX 3070 Ti | $600 | 6144 | 96 | 1575 MHz | 1770 MHz | 1188 MHz | GA104 | 17400M | 8 GB, GDDR6X, 256-bit |
| RX 6800 | $580 | 3840 | 96 | 1815 MHz | 2105 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6800 XT | $600 | 4608 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3080 | $660 | 8704 | 96 | 1440 MHz | 1710 MHz | 1188 MHz | GA102 | 28000M | 10 GB, GDDR6X, 320-bit |
| RTX 3080 Ti | $850 | 10240 | 112 | 1365 MHz | 1665 MHz | 1188 MHz | GA102 | 28000M | 12 GB, GDDR6X, 384-bit |
| RX 6900 XT | $680 | 5120 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6950 XT | $950 | 5120 | 128 | 2100 MHz | 2310 MHz | 2250 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3090 | $950 | 10496 | 112 | 1395 MHz | 1695 MHz | 1219 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
| RTX 3090 Ti | $1200 | 10752 | 112 | 1560 MHz | 1950 MHz | 1313 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
| RTX 4090 | $1600 | 16384 | 176 | 2235 MHz | 2520 MHz | 1313 MHz | AD102 | 76300M | 24 GB, GDDR6X, 384-bit |
