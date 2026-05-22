# AMD Radeon RX 6800 Review | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

We have with us the Radeon RX 6800. The fun-size sibling to the company's top RX 6800 XT, the two new high-end GPUs from AMD are out to eat NVIDIA's lunch in the enthusiast segment. The RX 6800 is based on the silicon the PC enthusiast community for long fabled as "Big Navi," and as AMD's long overdue response to NVIDIA's high-end as it was first to the market with 7 nm GPUs and used the new node to great effect in bringing down Intel's near-monopoly. NVIDIA's decision to introduce real-time raytracing to the PC gaming segment with the GeForce RTX 20-series "Turing" caught AMD by surprise as it sat down to design RDNA 2. By this point, the RX 5700 series "Navi" was taped out, and when it released in mid-2019, it did enough to disrupt NVIDIA's performance segment under $500, but couldn't take on the high-end. We watched AMD's late-October 2020 announcement stream with moderate expectations for RDNA 2, but were shocked with what ensued as AMD claimed the RDNA 2-powered RX 6800 series to compete against NVIDIA's recently launched RTX 3080 and RTX 2080 Ti (RTX 3070), and with full DirectX 12 Ultimate readiness, which means support for raytracing.


Real-time raytracing is an extremely hardware-intensive feature. For its RTX 30-series "Ampere" that introduces second-generation RTX, NVIDIA's design goal was to double the shader units, making RTX-on performance of this generation as fast as the RTX-off performance of "Turing." The same was expected of AMD if it intended to compete in the high-end segment, and it seems the company delivered on this engineering goal with the RX 6800 featuring 60 RDNA 2 compute units, or 3,840 stream processors, about 67 percent more than those of the RX 5700. The RX 6800 is carved out from the same 7 nm "Navi 21" silicon as the RX 6800 XT and future RX 6900 XT. AMD enables 60 out of 80 compute units physically present on the die. Interestingly, the memory sub-system is unchanged, with 16 GB of JEDEC-standard 16 Gbps GDDR6 memory across a 256-bit wide memory bus. The memory bandwidth of the RX 6800 is higher than with the RTX 3070, which has to make do with 8 GB of 14 Gbps memory, though a lot slower than the 19 Gbps 320-bit GDDR6X at the disposal of the RTX 3080. AMD found a clever way to improve its effective memory bandwidth by deploying a fairly big on-die component it calls Infinity Cache, which we will detail in the Architecture section. 


AMD is recommending the Radeon RX 6800 for the same use case NVIDIA is targeting with the RTX 3070—maxed out gaming with raytracing at 1440p, but with the ability to play at 4K Ultra HD with fairly high settings. Interestingly, AMD is pricing the RX 6800 at $579, a steep $80 premium over the RTX 3070. Perhaps AMD is feeling confident about beating the NVIDIA card given its marketing slides show it being consistently faster than the RTX 2080 Ti, which is roughly as fast as the RTX 3070. AMD's decision to give the RX 6800 the full 16 GB of memory available on its pricier sibling could also be bearing down on the price. Interesting is also that despite a steep increase in shader counts, a doubling in memory amount, and use of the same 7 nm node, AMD is rating the typical board power of the RX 6800 at just 250 W, which means AMD has made serious advances in power management. All these and more will be put to the test in this review to tell you if AMD is back in the high-end graphics card market, and if consumers can expect a price war and cooling down of graphics card prices.


| | Price | Shader Units | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
| RX Vega 64 | $400 | 4096 | 64 | 1247 MHz | 1546 MHz | 953 MHz | Vega 10 | 12500M | 8 GB, HBM2, 2048-bit |
| GTX 1080 Ti | $650 | 3584 | 88 | 1481 MHz | 1582 MHz | 1376 MHz | GP102 | 12000M | 11 GB, GDDR5X, 352-bit |
| RX 5700 XT | $370 | 2560 | 64 | 1605 MHz | 1755 MHz | 1750 MHz | Navi 10 | 10300M | 8 GB, GDDR6, 256-bit |
| RTX 2070 | $340 | 2304 | 64 | 1410 MHz | 1620 MHz | 1750 MHz | TU106 | 10800M | 8 GB, GDDR6, 256-bit |
| RTX 2070 Super | $450 | 2560 | 64 | 1605 MHz | 1770 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| Radeon VII | $680 | 3840 | 64 | 1802 MHz | N/A | 1000 MHz | Vega 20 | 13230M | 16 GB, HBM2, 4096-bit |
| RTX 2080 | $600 | 2944 | 64 | 1515 MHz | 1710 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 2080 Super | $690 | 3072 | 64 | 1650 MHz | 1815 MHz | 1940 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 2080 Ti | $1000 | 4352 | 88 | 1350 MHz | 1545 MHz | 1750 MHz | TU102 | 18600M | 11 GB, GDDR6, 352-bit |
| RTX 3070 | $500 | 5888 | 96 | 1500 MHz | 1725 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RX 6800 | $580 | 3840 | 96 | 1815 MHz | 2105 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6800 XT | $650 | 4608 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3080 | $700 | 8704 | 96 | 1440 MHz | 1710 MHz | 1188 MHz | GA102 | 28000M | 10 GB, GDDR6X, 320-bit |
| RTX 3090 | $1500 | 10496 | 112 | 1395 MHz | 1695 MHz | 1219 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
