FROM nvidia/cuda:10.1-cudnn7-devel

ENV DEBIAN_FRONTEND noninteractive

# Install apt dependencies
RUN apt-get update && apt-get install -y \
    git-all \
    wget \
    sudo \
    nano \
    curl \
    gpg-agent \
    lsb-release \
    python3-cairocffi \
    protobuf-compiler \
    python3-pil \
    python3-lxml \
    python3-tk \
    python3-opencv \
    python3-matplotlib \
    python3-dev \
    cmake \
    ca-certificates \
    ninja-build && \
    rm -rf /var/lib/apt/lists/*
RUN ln -sv /usr/bin/python3 /usr/bin/python

# create a non-root user
ARG USER_ID=1000
RUN useradd -m --no-log-init --system  --uid ${USER_ID} nlp -g sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER nlp
WORKDIR /home/nlp

ENV PATH="/home/nlp/.local/bin:${PATH}"
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py --user && \
    rm get-pip.py

# install dependencies
RUN pip install --upgrade pip
RUN pip install --user \
    absl-py==0.9.0 \
    attrs==19.3.0 \
    backcall==0.1.0 \
    beautifulsoup4==4.6.0 \
    bleach==3.1.5 \
    cachetools==4.1.0 \
    certifi==2020.4.5.1 \
    chardet==3.0.4 \
    click==7.1.2 \
    colorama==0.4.3 \
    Cython==0.29.19 \
    decorator==4.4.2 \
    defusedxml==0.6.0 \
    entrypoints==0.3 \
    filelock==3.0.12 \
    future==0.18.2 \
    gdown==3.11.0 \
    gluonnlp==0.9.1 \
    google-auth==1.15.0 \
    google-auth-oauthlib==0.4.1 \
    graphviz==0.8.4 \
    grpcio==1.29.0 \
    idna==2.9 \
    importlib-metadata==1.6.0 \
    ipykernel==5.3.0 \
    ipython==7.14.0 \
    ipython-genutils==0.2.0 \
    ipywidgets==7.5.1 \
    jedi==0.17.0 \
    Jinja2==2.11.2 \
    joblib==0.15.1 \
    JPype1==0.7.5 \
    jsonschema==3.2.0 \
    jupyter==1.0.0 \
    jupyter-client==6.1.3 \
    jupyter-console==6.1.0 \
    jupyter-core==4.6.3 \
    jupyterlab==2.2.9 \
    konlpy==0.5.2 \
    lxml==4.5.1 \
    Markdown==3.2.2 \
    MarkupSafe==1.1.1 \
    mistune==0.8.4 \
    mxnet-cu101==1.7.0 \
    nbconvert==5.6.1 \
    nbformat==5.0.6 \
    notebook==6.0.3 \
    numpy==1.18.4 \
    oauthlib==3.1.0 \
    packaging==20.4 \
    pandas==1.0.3 \
    pandocfilters==1.4.2 \
    parso==0.7.0 \
    pexpect==4.8.0 \
    pickleshare==0.7.5 \
    Pillow==7.1.2 \
    prometheus-client==0.8.0 \
    prompt-toolkit==3.0.5 \
    protobuf==3.12.1 \
    ptyprocess==0.6.0 \
    pyasn1==0.4.8 \
    pyasn1-modules==0.2.8 \
    Pygments==2.6.1 \
    pyparsing==2.4.7 \
    pyrsistent==0.16.0 \
    PySocks==1.7.1 \
    python-dateutil==2.8.1 \
    pytz==2020.1 \
    pyzmq==19.0.1 \
    qtconsole==4.7.4 \
    QtPy==1.9.0 \
    regex==2020.5.14 \
    requests==2.23.0 \
    requests-oauthlib==1.3.0 \
    rsa==4.0 \
    sacremoses==0.0.43 \
    scikit-learn==0.23.1 \
    scipy==1.4.1 \
    Send2Trash==1.5.0 \
    sentencepiece==0.1.91 \
    six==1.15.0 \
    tensorboard==2.2.2 \
    tensorboard-plugin-wit==1.6.0.post3 \
    terminado==0.8.3 \
    testpath==0.4.4 \
    threadpoolctl==2.0.0 \
    tokenizers==0.7.0 \
    tornado==6.0.4 \
    tqdm==4.46.0 \
    traitlets==4.3.3 \
    transformers==2.1.1 \
    tweepy==3.8.0 \
    urllib3==1.25.9 \
    wcwidth==0.1.9 \
    webencodings==0.5.1 \
    Werkzeug==1.0.1 \
    widgetsnbextension==3.5.1 \
    zipp==3.1.0

RUN pip install --user torch==1.5.1 torchvision==0.6.1 -f https://download.pytorch.org/whl/cu101/torch_stable.html
RUN pip install --user tensorflow-gpu==1.15.4

WORKDIR /
