# Bachelor's Thesis: Topological Data Analysis for Dataset Refinement
Bachelor's Thesis (TFG): Topological Data Analysis (TDA) for Dataset Refinement. Applies computational tools from Algebraic Topology to remove noise and redundancies in Point Clouds while preserving the fundamental topological features. Includes self-developed algorithm, along with Python code for its experimental validation.

## 📄 Final Report and Theoretical Basis (Documentation)

The **complete project documentation** and the theoretical foundation are available in the final report, which details the construction of Simplicial Homology, concepts of Topological Data Analysis such as Persistente Homology and Bottleneck Distance, and the algorithm description and explanation for topological filtering applied, along with its experimental validation and conclusions.

* **[Complete TFG Report: Topological Data Analysis for Dataset Refinement](report/MEMORIA.pdf)**
    * This document serves as the academic and theoretical foundation for the code.

---

 ## 💻 Project Structure and Experimental Code

All code logic and implementation details are thoroughly explained in the **Appendix** of the final report.
* **[Appendix: Python code](report/APENDICE TFG.pdf)**

The **Appendix** covers:
* The required **external libraries** and environment setup.
* The exact **generation method** for the test dataset (e.g., the torus).
* The **general topological filtering algorithm** (applicable to any dimension).
* The **analysis and comparison** of the final results.
* The **visualization** process for the filtered point clouds.


The source code used for the experimental section of the thesis resides in the **`/src`** folder and is composed of several scripts that implement the analysis phases.

| File in `/src` | Purpose and Included Algorithms |
| :--- | :--- |
| `base_pipeline.py` | **Base Pipeline:** Contains **Test Data Generation**, initial **Visualization**, and **Persistence Diagram Calculation** for general analysis. It's also included in next scripts |
| `filter_h0.py` | **TFG - Dimension 0:** Complete filtering pipeline and quantitative analysis through Bottleneck Distance for **Dimension 0** persistent homology. |
| `filter_h1.py` | **TFG - Dimension 1:** Complete filtering pipeline and quantitative analysis through Bottleneck Distance for **Dimension 1** persistent homology. |
| `filter_h2.py` | **TFG - Dimension 2:** Complete filtering pipeline and quantitative analysis through Bottleneck Distance for **Dimension 2** persistent homology. |
| `filter_h1h2.py` | **TFG - Dimension 1 and 2:** Complete filtering pipeline and quantitative analysis through Bottleneck Distance for **both 1 and 2 Dimensions** persistent homology. |
| `sequential_filter_advanced.py` | **High-Cost Advanced Algorithm (EXTRA):** Implements the **point-by-point** sequential filtering method (re-evaluating the set after each removal). Achieves **better results** than the TFG's batch method, but at an **exponentially higher computational cost and time**. |

---

## ⚙️ Installation and Usage

### 1. Requirements

The project requires **Python 3.x** and the scientific and topological libraries listed in `requirements.txt`.

```bash
# 1. Clone the repository
git clone [https://github.com/YourUsername/TFG-Topologia-Datos-Aplicada.git](https://github.com/YourUsername/TFG-Topologia-Datos-Aplicada.git)
cd TFG-Topologia-Datos-Aplicada

# 2. Create and install the virtual environment
python -m venv .venv

# 3. Install dependencies
# (Ensure you create this requirements.txt file with all necessary libraries)
pip install -r requirements.txt

```

### 2. Usage

```bash
python src/base_pipeline.py
python src/filter_h0.py
python src/filter_h1.py
python src/filter_h2.py
python src/filter_h1h2.py
python src/sequential_filter_advanced.py
```

## 🎓 Authorship and Supervision

This repository documents the Bachelor's Thesis in Mathematics presented at the University of Zaragoza.

* **Author:** Carlos Lafuente Carreras
* **Thesis Director:** Miguel Ángel Marco Buzunáriz
* **University:** Universidad de Zaragoza
* **Presentation Date:** July 11, 2025
