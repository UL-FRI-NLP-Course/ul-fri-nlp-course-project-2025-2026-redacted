"""
convert_structured_data.py

Converts structured CSV/JSON hardware datasets into natural-language text chunks
suitable for indexing alongside the review markdown files.

Outputs one chunk per line to data/structured_chunks/{cpu,gpu}/.
"""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_IN = ROOT / "data" / "more_data"
DATA_OUT = ROOT / "data" / "structured_chunks"

CPU_OUT = DATA_OUT / "cpu"
GPU_OUT = DATA_OUT / "gpu"

AMD_CPU_FAMILIES = {"Ryzen", "Ryzen Threadripper"}
AMD_DESKTOP_SOCKETS = {"AM4", "AM5", "sTRX40", "sTR5"}

INTEL_DESKTOP_SOCKETS = {"FCLGA1700", "FCLGA1851", "FCLGA1200", "FCLGA1151", "FCLGA1150", "FCLGA2066"}

AMD_GPU_SERIES_KEEP = {"RX 5000", "RX 6000", "RX 7000", "RX 9000"}


def _v(val: str) -> str:
    return val.strip() if val and val.strip() else ""


def _line(*parts: str) -> str | None:
    text = " ".join(p for p in parts if p)
    return text if len(text) >= 20 else None


# ── AMD CPU specs ──────────────────────────────────────────────────────────────

def convert_amd_cpus() -> list[str]:
    path = DATA_IN / "Processor Specifications.csv"
    lines = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if _v(row.get("Family", "")) not in AMD_CPU_FAMILIES:
                continue
            if not any(sock in _v(row.get("CPU Socket", "")) for sock in AMD_DESKTOP_SOCKETS):
                continue

            name = _v(row.get("Name", ""))
            cores = _v(row.get("# of CPU Cores", ""))
            threads = _v(row.get("# of Threads", ""))
            base = _v(row.get("Base Clock", ""))
            boost = _v(row.get("Max. Boost Clock", ""))
            l3 = _v(row.get("L3 Cache", ""))
            tdp = _v(row.get("Default TDP", ""))
            socket = _v(row.get("CPU Socket", ""))
            mem_type = _v(row.get("System Memory Type", ""))
            mem_spec = _v(row.get("System Memory Specification", ""))
            oc = _v(row.get("Unlocked for Overclocking", ""))
            igpu = _v(row.get("Graphics Model", ""))

            if not name:
                continue

            parts = [f"{name} specifications:"]
            if cores:
                parts.append(f"{cores} cores,")
            if threads:
                parts.append(f"{threads} threads,")
            if base:
                parts.append(f"base {base},")
            if boost:
                parts.append(f"boost {boost},")
            if l3:
                parts.append(f"L3 cache {l3},")
            if tdp:
                parts.append(f"TDP {tdp},")
            if socket:
                parts.append(f"socket {socket},")
            if mem_type:
                mem_str = mem_type
                if mem_spec:
                    mem_str += f" ({mem_spec})"
                parts.append(f"memory {mem_str},")
            if oc and oc.lower() == "yes":
                parts.append("unlocked for overclocking,")
            if igpu:
                parts.append(f"integrated graphics {igpu}.")
            else:
                if parts[-1].endswith(","):
                    parts[-1] = parts[-1][:-1] + "."

            line = _line(" ".join(parts))
            if line:
                lines.append(line)

    return lines


def convert_intel_cpus() -> list[str]:
    path = DATA_IN / "intel-cpus.csv"
    lines = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            socket = _v(row.get("Sockets Supported", ""))
            if not any(s in socket for s in INTEL_DESKTOP_SOCKETS):
                continue

            name = _v(row.get("CpuName", ""))
            p_cores = _v(row.get("# of Performance-cores", ""))
            e_cores = _v(row.get("# of Efficient-cores", ""))
            total_cores = _v(row.get("# of Cores", ""))
            threads = _v(row.get("# of Threads", ""))
            max_turbo = _v(row.get("Max Turbo Frequency", ""))
            base_freq = _v(row.get("Processor Base Frequency", ""))
            cache = _v(row.get("Cache", ""))
            tdp = _v(row.get("TDP", ""))
            tdp_up = _v(row.get("Configurable TDP-up", ""))
            mem_types = _v(row.get("Memory Types", ""))
            max_mem = _v(row.get("Max Memory Size (dependent on memory type)", ""))
            launch = _v(row.get("Launch Date", ""))

            if not name:
                continue

            parts = [f"{name} specifications:"]

            # Core count: hybrid or traditional
            if p_cores and e_cores:
                parts.append(f"{p_cores}P + {e_cores}E cores,")
            elif total_cores:
                parts.append(f"{total_cores} cores,")
            if threads:
                parts.append(f"{threads} threads,")
            if base_freq:
                parts.append(f"base {base_freq},")
            if max_turbo:
                parts.append(f"boost up to {max_turbo},")
            if cache:
                parts.append(f"cache {cache},")
            if tdp:
                tdp_str = tdp
                if tdp_up:
                    tdp_str += f" (up to {tdp_up})"
                parts.append(f"TDP {tdp_str},")
            if socket:
                parts.append(f"socket {socket},")
            if mem_types:
                mem_str = mem_types
                if max_mem:
                    mem_str += f", max {max_mem}"
                parts.append(f"memory {mem_str},")
            if launch:
                parts.append(f"launched {launch}.")
            else:
                if parts[-1].endswith(","):
                    parts[-1] = parts[-1][:-1] + "."

            line = _line(" ".join(parts))
            if line:
                lines.append(line)

    return lines


# ── CPU benchmarks ─────────────────────────────────────────────────────────────

def convert_cpu_benchmarks() -> list[str]:
    path = DATA_IN / "benchmark-cpus.csv"
    lines = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            mt = _v(row.get("MultithreadRating", ""))
            if not mt:
                continue

            name = _v(row.get("CpuName", ""))
            st = _v(row.get("SingleThreadRating", ""))
            socket = _v(row.get("Socket", ""))
            cores = _v(row.get("Cores", ""))
            threads = _v(row.get("Threads", ""))
            tdp = _v(row.get("TDP", ""))
            clock = _v(row.get("ClockSpeed", ""))
            turbo = _v(row.get("TurboSpeed", ""))

            if not name:
                continue

            parts = [f"{name} PassMark benchmark:"]
            parts.append(f"multi-thread score {mt},")
            if st:
                parts.append(f"single-thread score {st},")
            if cores:
                parts.append(f"{cores} cores,")
            if threads:
                parts.append(f"{threads} threads,")
            if clock:
                parts.append(f"base {clock},")
            if turbo:
                parts.append(f"boost {turbo},")
            if socket:
                parts.append(f"socket {socket},")
            if tdp and tdp != "-1 W":
                parts.append(f"TDP {tdp}.")
            else:
                if parts[-1].endswith(","):
                    parts[-1] = parts[-1][:-1] + "."

            line = _line(" ".join(parts))
            if line:
                lines.append(line)

    return lines



def convert_amd_gpus() -> list[str]:
    path = DATA_IN / "Graphics Specifications.csv"
    lines = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            series = _v(row.get("Series", ""))
            if not any(keep in series for keep in AMD_GPU_SERIES_KEEP):
                continue

            name = _v(row.get("Name", ""))
            board_type = _v(row.get("Board Type", ""))
            cu = _v(row.get("Compute Units", ""))
            sp = _v(row.get("Stream Processors", ""))
            boost = _v(row.get("Boost Frequency", ""))
            game_clk = _v(row.get("Game Frequency", ""))
            ray = _v(row.get("Ray Accelerators", ""))
            vram = _v(row.get("Max Memory Size", ""))
            mem_type = _v(row.get("Memory Type", ""))
            mem_bus = _v(row.get("Memory Interface", ""))
            mem_bw = _v(row.get("Memory Bandwidth", ""))
            cache = _v(row.get("AMD Infinity Cache Technology", ""))
            tbp = _v(row.get("Typical Board Power (Desktop)", ""))
            psu = _v(row.get("Minimum PSU Recommendation", ""))

            if not name:
                continue

            # Name already contains "AMD", avoid doubling
            display_name = name if name.startswith("AMD") else f"AMD {name}"
            parts = [f"{display_name} specifications:"]
            if board_type and "Desktop" in board_type:
                parts.append("desktop card,")
            if cu:
                parts.append(f"{cu} compute units,")
            if sp:
                parts.append(f"{sp} stream processors,")
            if boost:
                parts.append(f"boost {boost},")
            if game_clk:
                parts.append(f"game clock {game_clk},")
            if ray:
                parts.append(f"{ray} ray accelerators,")
            if vram and mem_type:
                parts.append(f"{vram} {mem_type},")
            elif vram:
                parts.append(f"{vram} VRAM,")
            if mem_bus:
                parts.append(f"{mem_bus} memory bus,")
            if mem_bw:
                parts.append(f"{mem_bw} memory bandwidth,")
            if cache:
                parts.append(f"{cache} Infinity Cache,")
            if tbp:
                parts.append(f"TBP {tbp},")
            if psu:
                parts.append(f"min PSU {psu}.")
            else:
                if parts[-1].endswith(","):
                    parts[-1] = parts[-1][:-1] + "."

            line = _line(" ".join(parts))
            if line:
                lines.append(line)

    return lines



def convert_gpu_benchmarks() -> list[str]:
    path = DATA_IN / "benchmark-gpus.csv"
    lines = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            g3d = _v(row.get("G3DMark", ""))
            if not g3d:
                continue

            name = _v(row.get("GpuName", ""))
            g2d = _v(row.get("G2DMark", ""))
            vram = _v(row.get("MaxMemory", ""))
            core_clk = _v(row.get("CoreClock", ""))
            mem_clk = _v(row.get("MemoryClock", ""))
            tdp = _v(row.get("TDP", ""))

            if not name:
                continue

            parts = [f"{name} PassMark benchmark:"]
            parts.append(f"G3DMark score {g3d},")
            if g2d:
                parts.append(f"G2DMark {g2d},")
            if vram:
                parts.append(f"{vram} VRAM,")
            if core_clk:
                parts.append(f"core clock {core_clk},")
            if mem_clk:
                parts.append(f"memory clock {mem_clk},")
            if tdp:
                parts.append(f"TDP {tdp}.")
            else:
                if parts[-1].endswith(","):
                    parts[-1] = parts[-1][:-1] + "."

            line = _line(" ".join(parts))
            if line:
                lines.append(line)

    return lines


def convert_steam() -> list[str]:
    path = DATA_IN / "steamdb_requirements.json"
    lines = []
    with open(path, encoding="utf-8") as f:
        games = json.load(f)

    for game in games:
        name = _v(game.get("name", ""))
        if not name:
            continue

        min_req = game.get("pc_minimum") or {}
        rec_req = game.get("pc_recommended") or {}

        if not min_req and not rec_req:
            continue

        parts = [f"{name} PC system requirements —"]

        min_parts = []
        if _v(min_req.get("Processor", "")):
            min_parts.append(f"CPU {_v(min_req['Processor'])}")
        if _v(min_req.get("Graphics", "")):
            min_parts.append(f"GPU {_v(min_req['Graphics'])}")
        if _v(min_req.get("Memory", "")):
            min_parts.append(f"RAM {_v(min_req['Memory'])}")
        if _v(min_req.get("Storage", "")):
            min_parts.append(f"storage {_v(min_req['Storage'])}")

        rec_parts = []
        if _v(rec_req.get("Processor", "")):
            rec_parts.append(f"CPU {_v(rec_req['Processor'])}")
        if _v(rec_req.get("Graphics", "")):
            rec_parts.append(f"GPU {_v(rec_req['Graphics'])}")
        if _v(rec_req.get("Memory", "")):
            rec_parts.append(f"RAM {_v(rec_req['Memory'])}")
        if _v(rec_req.get("Storage", "")):
            rec_parts.append(f"storage {_v(rec_req['Storage'])}")

        if min_parts:
            parts.append("minimum: " + ", ".join(min_parts) + ";")
        if rec_parts:
            parts.append("recommended: " + ", ".join(rec_parts) + ".")
        elif min_parts:
            parts[-1] = parts[-1].rstrip(";") + "."

        line = _line(" ".join(parts))
        if line:
            lines.append(line)

    return lines


# ── Main ───────────────────────────────────────────────────────────────────────

def write_chunks(lines: list[str], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  {len(lines):>6,} chunks → {path.relative_to(ROOT)}")


def main() -> None:
    print("Converting structured data to text chunks...\n")

    print("CPU index:")
    write_chunks(convert_amd_cpus(),       CPU_OUT / "amd_cpu_specs.txt")
    write_chunks(convert_intel_cpus(),     CPU_OUT / "intel_cpu_specs.txt")
    write_chunks(convert_cpu_benchmarks(), CPU_OUT / "cpu_benchmarks.txt")
    steam = convert_steam()
    write_chunks(steam, CPU_OUT / "steam_requirements.txt")

    print("\nGPU index:")
    write_chunks(convert_amd_gpus(),       GPU_OUT / "amd_gpu_specs.txt")
    write_chunks(convert_gpu_benchmarks(), GPU_OUT / "gpu_benchmarks.txt")
    write_chunks(steam, GPU_OUT / "steam_requirements.txt")

    print("\nDone.")


if __name__ == "__main__":
    main()
