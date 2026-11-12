# 16-bit CPU · Single-cycle processor

A single-cycle processor with a custom instruction set, implemented in **Logisim-evolution**, with a **Python** assembler and example programs.

**Author:** Marcos Isaias Daubermann.

![Overview of the single-cycle processor in Logisim-evolution](docs/images/processor.png)

## Project at a glance

The project covers ISA and control signal design, processor construction, and program translation into hexadecimal.

- **16-bit architecture:** instructions, registers, and program counter.
- **16 registers**, with `r0` fixed at zero.
- **11 instructions:** arithmetic and logic operations, memory access, and conditional branches.
- **Separate instruction and data memories**, implemented using pairs of 8-bit RAM modules.
- **Python assembler** to translate `.tsm` files into hexadecimal `.x` instructions.

## Getting started

### 1. Assemble an example

You need **Python 3**, with no external dependencies. From the repository root:

```bash
cd compiler
python3 compiler.py
```

When the prompt `Ingrese el nombre del archivo sin extensión:` (enter the filename without its extension) appears, enter:

```text
sumatoria
```

The program reads `programs/sumatoria.tsm` and writes—or overwrites—`bin/sumatoria.x`:

```text
5 2 0 0
1 3 3 1
7 1 1 1
a e 2 1
7 5 0 5
6 3 5 5
```

You can also enter `final` to assemble the other included example. **Always run from `compiler/`**: the program uses paths relative to the working directory.

### 2. Explore the processor

Open [`hardware/CPU_Daubermann_Marcos.circ`](hardware/CPU_Daubermann_Marcos.circ) in **Logisim-evolution**. Version used: **3.8.0**.

The main circuit is `main`. From there, you can explore the program counter, register file, control unit, ALU, and memories.

The [architecture guide](docs/arquitectura.md) describes the processor components, with diagrams and ISA details.

## Repository structure

```text
.
├── README.md
├── hardware/
│   ├── CPU_Daubermann_Marcos.circ
│   └── instrucciones_memoria/
│       ├── instrucciones_memoria1
│       └── instrucciones_memoria2
├── compiler/
│   ├── README.md
│   ├── compiler.py
│   ├── programs/
│   │   ├── sumatoria.tsm
│   │   └── final.tsm
│   └── bin/
│       ├── sumatoria.x
│       └── final.x
└── docs/
    ├── arquitectura.md
    └── images/
```

The `.x` output files let you inspect each program's hexadecimal encoding.

## Example: summation

The program sums the integers from zero through the value stored at address `0` in data memory and stores the result at address `10`.

```text
carga r2, r0, r0
suma r3, r3, r1
sumai r1, r1, 1
mayorig -2, r2, r1
sumai r5, r0, 5
almacena r3, r5, r5
```

With `r1` and `r3` initially set to zero, the program accumulates the sum in `r3`. The final instruction stores that value at address `r5 + r5 = 10`. The example combines loads, arithmetic, a relative branch, and a store.

![Summation program encoding in instruction memory](docs/images/sumatoria-memory.png)

## Documentation

- [Architecture and ISA](docs/arquitectura.md): components, diagrams, and instruction encoding.
