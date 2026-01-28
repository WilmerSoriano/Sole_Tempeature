FROM python:3.11-slim

# Install system deps for PyQt GUI
RUN apt-get update && apt-get install -y \
    libgl1 \
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    qtbase5-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy my code
COPY . .

# Allow GUI forwarding (WSLg), because windows...
ENV DISPLAY=:0

CMD ["python", "app.py"]
