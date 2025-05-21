FROM python:3.13

WORKDIR /app

RUN apt-get update && apt-get install npm -y
RUN apt-get install -y \
   texlive-latex-base \
   texlive-latex-recommended \
   texlive-latex-extra \
   texlive-lang-cyrillic \
   texlive-fonts-recommended
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY package.json .
COPY package-lock.json .

RUN pip install uv && \
    uv venv && \
    uv pip install -r requirements.txt
RUN npm install

COPY . .

RUN npm run build

EXPOSE 5000

ENTRYPOINT [".venv/bin/python", "-m", "server"]