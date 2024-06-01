### Installation
```bash
pip install git+https://github.com/max-fatouros/custom.git@v0.1.0
```
### Use Case
To implement a matplotlib style at a global level
```python
import matplotlib.pyplot as plt

from custom.mplstyles import PAPER
plt.style.use(PAPER)
```
