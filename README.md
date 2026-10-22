# Problem Set 1 - Question 2
This repository downloads yearly GDP data (current US$) for the UK, USA, Brazil, Japan, China, Germany and Switzerland from the World Bank API, and explores and plots it over 2000-2022.

## How to run the code
*Pre-Requisites*: You need [pixi](https://pixi.sh) installed

1. Clone the repository and move into it:
   ```
   git clone https://github.com/ar2367-cam/ps1_q2_gdp_data.git
   cd ps1_q2_gdp_data
   ```
2. Create the environment from `pixi.toml` / `pixi.lock`:
   ```
   pixi install
   ```
3. Run the notebook: open `gdp_analysis.ipynb` in VS Code, click "Select Kernel" (top right), choose "Python Environments" and pick the interpreter in `.pixi/envs/default`, then run all cells.

Run everything from the repository root so that the functions created in the 'fed' folder can be used.

Note: `pixi.toml` currently lists only the `win-64` platform. On macOS or Linux, run `pixi workspace platform add osx-arm64` (or `linux-64`) before `pixi install`.
