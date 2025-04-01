# Hackathon-Demo-2025

## How to Run the Demo (python3 on Mac, py on Windows)
1. Create a .env file in the root folder with `DEEPSEEK_API_KEY=<YOUR_DEEPSEEK_API_KEY_HERE>`
2. Create a virtual environment in python. E.g., `python3 -m venv myenv`
3. Activate the virtual environment E.g., `source myenv/bin/activate`
4. Install requirements `pip3 install -r requirements.txt`
5. Run `python3 main.py` in a terminal
6. Run `python3 proxy_server.py` in another terminal
7. Serve index.html on port 8000 by typing `python -m http.server` in the root folder in another terminal
8. Point your browser to `http://127.0.0.1:8000/index.html` to use the frontend UI

Note: The response from DeepSeek-R1 can take a few minutes before appearing.

The data analyzed is a small subset of data from this synthetic dataset from Kaggle: https://www.kaggle.com/datasets/ealaxi/paysim1

![image](https://github.com/user-attachments/assets/5d1f689b-9c14-4192-b0f0-08dbaf2940be)

## Next Steps
- Build presentation
- Improve this proof of concept demo

## Other
- How can we make this faster?
- Can we prevent malicious attacks?
- Can we make alerts load in the UI that aren't static but from a data source checked asynchronously?
- Can this easily be integrated with the Appian data fraud analysts actually use?
- What else?
