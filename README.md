# Bachelor's Thesis: Topological Data Analysis for Dataset Refinement
Bachelor's Thesis (TFG): Topological Data Analysis (TDA) for Dataset Refinement. Applies computational tools from Algebraic Topology to remove noise and redundancies in Point Clouds while preserving the fundamental topological features. Includes self-developed algorithm, along with Python code for its experimental validation.

## 📄 Final Report and Theoretical Basis (Documentation)

The **complete project documentation** and the theoretical foundation are available in the final report, which details the construction of Simplicial Homology, concepts of Topological Data Analysis such as Persistente Homology and Bottleneck Distance, and the algorithm description and explanation for topological filtering applied, along with its experimental validation and conclusions.

* **[Complete TFG Report: Topological Data Analysis for Dataset Refinement](report/TFGFINAL.pdf)**
    * This document serves as the academic and theoretical foundation for the code.

---

 ## 💻 Project Structure and Experimental Code

All code logic, methodology, and implementation details are thoroughly explained in the **Appendix** of the final report.

* **[Appendix:Python code](report/TFGFINAL.pdf)**

* **[Complete TFG Report: Topological Data Analysis for Dataset Refinement](report/TFGFINAL.pdf)**
The source code used for the experimental section of the thesis resides in the **`/src`** folder and is divided into 4 main modules covering the process end-to-end:

| File in `/src` | Functional Purpose |
| :--- | :--- |
| `data_generation.py` | Creation of the synthetic point cloud (e.g., the torus) or loading of the initial dataset. |
| `persistent_homology.py` | Implementation of Algebraic Topology tools, calculation of Persistent Homology and the Persistence Diagram. |
| `filtering_algorithm.py` | Implementation of the data refinement logic based on topological impact and Bottleneck Distance. |
| `visualization_3d.py` | Scripts for 3D visualization of the original point cloud and the filtered dataset (before/after). |

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

## 🎓 Authorship and Supervision

This repository documents the Bachelor's Thesis in Mathematics presented at the University of Zaragoza.

* **Author:** Carlos Lafuente Carreras
* **Thesis Director:** Miguel Ángel Marco Buzunáriz
* **University:** Universidad de Zaragoza
* **Presentation Date:** July 11, 2025
