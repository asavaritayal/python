
# 1. Install python3.6
RUN apt-get update && \
    apt-get install python3.6

# 2. Install venv
pip3 install virtualenv

# 3. Create antenv
python3.6 -m venv antenv --copies

# 4. Activate antenv
source antenv/bin/activate

# 6. Install user requirements
pip install -r requirements.txt