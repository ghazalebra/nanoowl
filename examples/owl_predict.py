(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples/tree_demo$ cd ..
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples$ cd ..
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ pip freeze > requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ ls
assets    LICENSE.md        onnxruntime_gpu-1.20.2-cp310-cp310-linux_aarch64.whl  setup.py     torch-2.3.0-cp310-cp310-linux_aarch64.whl
data      nanoowl           owlvit_image_encoder.onnx                             simple.onnx  torch2trt
docker    nanoowl.egg-info  README.md                                             test         torchvision-0.18.0a0+6043bc2-cp310-cp310-linux_aarch64.whl
examples  nanoowlenv        requirements.txt                                      test.py
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ vim requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ vim requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ rm requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ pipreqs --force
-bash: pipreqs: command not found
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ pip install pipreqs
Collecting pipreqs
  Downloading pipreqs-0.5.0-py3-none-any.whl.metadata (7.9 kB)
Collecting docopt==0.6.2 (from pipreqs)
  Downloading docopt-0.6.2.tar.gz (25 kB)
  Preparing metadata (setup.py) ... done
Collecting ipython==8.12.3 (from pipreqs)
  Downloading ipython-8.12.3-py3-none-any.whl.metadata (5.7 kB)
Collecting nbconvert<8.0.0,>=7.11.0 (from pipreqs)
  Downloading nbconvert-7.16.6-py3-none-any.whl.metadata (8.5 kB)
Collecting yarg==0.1.9 (from pipreqs)
  Downloading yarg-0.1.9-py2.py3-none-any.whl.metadata (4.6 kB)
Collecting backcall (from ipython==8.12.3->pipreqs)
  Downloading backcall-0.2.0-py2.py3-none-any.whl.metadata (2.0 kB)
Collecting decorator (from ipython==8.12.3->pipreqs)
  Downloading decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
Collecting jedi>=0.16 (from ipython==8.12.3->pipreqs)
  Downloading jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting matplotlib-inline (from ipython==8.12.3->pipreqs)
  Downloading matplotlib_inline-0.1.7-py3-none-any.whl.metadata (3.9 kB)
Collecting pickleshare (from ipython==8.12.3->pipreqs)
  Downloading pickleshare-0.7.5-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30 (from ipython==8.12.3->pipreqs)
  Downloading prompt_toolkit-3.0.51-py3-none-any.whl.metadata (6.4 kB)
Collecting pygments>=2.4.0 (from ipython==8.12.3->pipreqs)
  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting stack-data (from ipython==8.12.3->pipreqs)
  Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
Collecting traitlets>=5 (from ipython==8.12.3->pipreqs)
  Downloading traitlets-5.14.3-py3-none-any.whl.metadata (10 kB)
Collecting pexpect>4.3 (from ipython==8.12.3->pipreqs)
  Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: requests in ./nanoowlenv/lib/python3.10/site-packages (from yarg==0.1.9->pipreqs) (2.32.4)
Collecting beautifulsoup4 (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)
Collecting bleach!=5.0.0 (from bleach[css]!=5.0.0->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading bleach-6.2.0-py3-none-any.whl.metadata (30 kB)
Collecting defusedxml (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Requirement already satisfied: jinja2>=3.0 in ./nanoowlenv/lib/python3.10/site-packages (from nbconvert<8.0.0,>=7.11.0->pipreqs) (3.1.6)
Collecting jupyter-core>=4.7 (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading jupyter_core-5.8.1-py3-none-any.whl.metadata (1.6 kB)
Collecting jupyterlab-pygments (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)
Requirement already satisfied: markupsafe>=2.0 in ./nanoowlenv/lib/python3.10/site-packages (from nbconvert<8.0.0,>=7.11.0->pipreqs) (3.0.2)
Collecting mistune<4,>=2.0.3 (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading mistune-3.1.3-py3-none-any.whl.metadata (1.8 kB)
Collecting nbclient>=0.5.0 (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading nbclient-0.10.2-py3-none-any.whl.metadata (8.3 kB)
Collecting nbformat>=5.7 (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)
Requirement already satisfied: packaging in ./nanoowlenv/lib/python3.10/site-packages (from nbconvert<8.0.0,>=7.11.0->pipreqs) (25.0)
Collecting pandocfilters>=1.4.1 (from nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)
Requirement already satisfied: typing-extensions in ./nanoowlenv/lib/python3.10/site-packages (from mistune<4,>=2.0.3->nbconvert<8.0.0,>=7.11.0->pipreqs) (4.14.0)
Requirement already satisfied: wcwidth in ./nanoowlenv/lib/python3.10/site-packages (from prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30->ipython==8.12.3->pipreqs) (0.2.13)
Collecting webencodings (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
Collecting tinycss2<1.5,>=1.1.0 (from bleach[css]!=5.0.0->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading tinycss2-1.4.0-py3-none-any.whl.metadata (3.0 kB)
Collecting parso<0.9.0,>=0.8.4 (from jedi>=0.16->ipython==8.12.3->pipreqs)
  Downloading parso-0.8.4-py2.py3-none-any.whl.metadata (7.7 kB)
Collecting platformdirs>=2.5 (from jupyter-core>=4.7->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading platformdirs-4.3.8-py3-none-any.whl.metadata (12 kB)
Collecting jupyter-client>=6.1.12 (from nbclient>=0.5.0->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading jupyter_client-8.6.3-py3-none-any.whl.metadata (8.3 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in ./nanoowlenv/lib/python3.10/site-packages (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert<8.0.0,>=7.11.0->pipreqs) (2.9.0.post0)
Collecting pyzmq>=23.0 (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading pyzmq-27.0.0-cp310-cp310-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl.metadata (6.0 kB)
Collecting tornado>=6.2 (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading tornado-6.5.1-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (2.8 kB)
Collecting fastjsonschema>=2.15 (from nbformat>=5.7->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading fastjsonschema-2.21.1-py3-none-any.whl.metadata (2.2 kB)
Collecting jsonschema>=2.6 (from nbformat>=5.7->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading jsonschema-4.24.0-py3-none-any.whl.metadata (7.8 kB)
Requirement already satisfied: attrs>=22.2.0 in ./nanoowlenv/lib/python3.10/site-packages (from jsonschema>=2.6->nbformat>=5.7->nbconvert<8.0.0,>=7.11.0->pipreqs) (25.3.0)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=2.6->nbformat>=5.7->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading jsonschema_specifications-2025.4.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=2.6->nbformat>=5.7->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading referencing-0.36.2-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.7.1 (from jsonschema>=2.6->nbformat>=5.7->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading rpds_py-0.25.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (4.1 kB)
Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython==8.12.3->pipreqs)
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
Requirement already satisfied: six>=1.5 in ./nanoowlenv/lib/python3.10/site-packages (from python-dateutil>=2.8.2->jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert<8.0.0,>=7.11.0->pipreqs) (1.17.0)
Collecting soupsieve>1.2 (from beautifulsoup4->nbconvert<8.0.0,>=7.11.0->pipreqs)
  Downloading soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in ./nanoowlenv/lib/python3.10/site-packages (from requests->yarg==0.1.9->pipreqs) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in ./nanoowlenv/lib/python3.10/site-packages (from requests->yarg==0.1.9->pipreqs) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./nanoowlenv/lib/python3.10/site-packages (from requests->yarg==0.1.9->pipreqs) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in ./nanoowlenv/lib/python3.10/site-packages (from requests->yarg==0.1.9->pipreqs) (2025.6.15)
Collecting executing>=1.2.0 (from stack-data->ipython==8.12.3->pipreqs)
  Downloading executing-2.2.0-py2.py3-none-any.whl.metadata (8.9 kB)
Collecting asttokens>=2.1.0 (from stack-data->ipython==8.12.3->pipreqs)
  Downloading asttokens-3.0.0-py3-none-any.whl.metadata (4.7 kB)
Collecting pure-eval (from stack-data->ipython==8.12.3->pipreqs)
  Downloading pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
Downloading pipreqs-0.5.0-py3-none-any.whl (33 kB)
Downloading ipython-8.12.3-py3-none-any.whl (798 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 798.3/798.3 kB 12.2 MB/s eta 0:00:00
Downloading yarg-0.1.9-py2.py3-none-any.whl (19 kB)
Downloading nbconvert-7.16.6-py3-none-any.whl (258 kB)
Downloading mistune-3.1.3-py3-none-any.whl (53 kB)
Downloading prompt_toolkit-3.0.51-py3-none-any.whl (387 kB)
Downloading bleach-6.2.0-py3-none-any.whl (163 kB)
Downloading tinycss2-1.4.0-py3-none-any.whl (26 kB)
Downloading jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 22.5 MB/s eta 0:00:00
Downloading parso-0.8.4-py2.py3-none-any.whl (103 kB)
Downloading jupyter_core-5.8.1-py3-none-any.whl (28 kB)
Downloading nbclient-0.10.2-py3-none-any.whl (25 kB)
Downloading jupyter_client-8.6.3-py3-none-any.whl (106 kB)
Downloading nbformat-5.10.4-py3-none-any.whl (78 kB)
Downloading fastjsonschema-2.21.1-py3-none-any.whl (23 kB)
Downloading jsonschema-4.24.0-py3-none-any.whl (88 kB)
Downloading jsonschema_specifications-2025.4.1-py3-none-any.whl (18 kB)
Downloading pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
Downloading platformdirs-4.3.8-py3-none-any.whl (18 kB)
Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 22.4 MB/s eta 0:00:00
Downloading pyzmq-27.0.0-cp310-cp310-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl (666 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 666.2/666.2 kB 14.4 MB/s eta 0:00:00
Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
Downloading rpds_py-0.25.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (386 kB)
Downloading tornado-6.5.1-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (443 kB)
Downloading traitlets-5.14.3-py3-none-any.whl (85 kB)
Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Downloading beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)
Downloading soupsieve-2.7-py3-none-any.whl (36 kB)
Downloading decorator-5.2.1-py3-none-any.whl (9.2 kB)
Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)
Downloading matplotlib_inline-0.1.7-py3-none-any.whl (9.9 kB)
Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
Downloading asttokens-3.0.0-py3-none-any.whl (26 kB)
Downloading executing-2.2.0-py2.py3-none-any.whl (26 kB)
Downloading pure_eval-0.2.3-py3-none-any.whl (11 kB)
Building wheels for collected packages: docopt
  DEPRECATION: Building 'docopt' using the legacy setup.py bdist_wheel mechanism, which will be removed in a future version. pip 25.3 will enforce this behaviour change. A possible replacement is to use the standardized build interface by setting the `--use-pep517` option, (possibly combined with `--no-build-isolation`), or adding a `pyproject.toml` file to the source tree of 'docopt'. Discussion can be found at https://github.com/pypa/pip/issues/6334
  Building wheel for docopt (setup.py) ... done
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13783 sha256=393c258e688b96a1dc0f586a55dd7d53a765a4c0778de361984cd0829571539a
  Stored in directory: /home/ghebr/.cache/pip/wheels/fc/ab/d4/5da2067ac95b36618c629a5f93f809425700506f72c9732fac
Successfully built docopt
Installing collected packages: webencodings, pure-eval, ptyprocess, pickleshare, fastjsonschema, docopt, backcall, traitlets, tornado, tinycss2, soupsieve, rpds-py, pyzmq, pygments, prompt-toolkit, platformdirs, pexpect, parso, pandocfilters, mistune, jupyterlab-pygments, executing, defusedxml, decorator, bleach, asttokens, yarg, stack-data, referencing, matplotlib-inline, jupyter-core, jedi, beautifulsoup4, jupyter-client, jsonschema-specifications, ipython, jsonschema, nbformat, nbclient, nbconvert, pipreqs
Successfully installed asttokens-3.0.0 backcall-0.2.0 beautifulsoup4-4.13.4 bleach-6.2.0 decorator-5.2.1 defusedxml-0.7.1 docopt-0.6.2 executing-2.2.0 fastjsonschema-2.21.1 ipython-8.12.3 jedi-0.19.2 jsonschema-4.24.0 jsonschema-specifications-2025.4.1 jupyter-client-8.6.3 jupyter-core-5.8.1 jupyterlab-pygments-0.3.0 matplotlib-inline-0.1.7 mistune-3.1.3 nbclient-0.10.2 nbconvert-7.16.6 nbformat-5.10.4 pandocfilters-1.5.1 parso-0.8.4 pexpect-4.9.0 pickleshare-0.7.5 pipreqs-0.5.0 platformdirs-4.3.8 prompt-toolkit-3.0.51 ptyprocess-0.7.0 pure-eval-0.2.3 pygments-2.19.2 pyzmq-27.0.0 referencing-0.36.2 rpds-py-0.25.1 soupsieve-2.7 stack-data-0.6.3 tinycss2-1.4.0 tornado-6.5.1 traitlets-5.14.3 webencodings-0.5.1 yarg-0.1.9
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ pipreqs --force
INFO: Not scanning for jupyter notebooks.
Traceback (most recent call last):
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/bin/pipreqs", line 8, in <module>
    sys.exit(main())
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 609, in main
    init(args)
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 533, in init
    candidates = get_all_imports(
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 136, in get_all_imports
    contents = read_file_content(file_name, encoding)
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 181, in read_file_content
    contents = f.read()
  File "/usr/lib/python3.10/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 81: invalid start byte
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ pipreqs . --force
INFO: Not scanning for jupyter notebooks.
Traceback (most recent call last):
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/bin/pipreqs", line 8, in <module>
    sys.exit(main())
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 609, in main
    init(args)
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 533, in init
    candidates = get_all_imports(
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 136, in get_all_imports
    contents = read_file_content(file_name, encoding)
  File "/home/ghebr/Desktop/nanoowl/nanoowlenv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 181, in read_file_content
    contents = f.read()
  File "/usr/lib/python3.10/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 81: invalid start byte
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ pip freeze > requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ vim requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ vim requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ rm requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ vim requirements.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl$ cd examples
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples$ ls
owl_predict.py  tree_demo  tree_predict.py  url.txt
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples$ cd owl_predict
-bash: cd: owl_predict: No such file or directory
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples$ vim owl_predict.py


    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default="../assets/owl_glove_small.jpg")
    parser.add_argument("--prompt", type=str, default="[an owl, a glove]")
    parser.add_argument("--threshold", type=str, default="0.1,0.1")
    parser.add_argument("--output", type=str, default="../data/owl_predict_out.jpg")
    parser.add_argument("--model", type=str, default="google/owlvit-base-patch32")
    parser.add_argument("--image_encoder_engine", type=str, default="../data/owl_image_encoder_patch32.engine")
    parser.add_argument("--profile", action="store_true")
    parser.add_argument("--num_profiling_runs", type=int, default=30)
    args = parser.parse_args()

    prompt = args.prompt.strip("][()")
    text = prompt.split(',')
    print(text)

    thresholds = args.threshold.strip("][()")
    thresholds = thresholds.split(',')
    if len(thresholds) == 1:
        thresholds = float(thresholds[0])
    else:
        thresholds = [float(x) for x in thresholds]
    print(thresholds)


    predictor = OwlPredictor(
        args.model,
        image_encoder_engine=args.image_encoder_engine
    )

    image = PIL.Image.open(args.image)

    text_encodings = predictor.encode_text(text)

    output = predictor.predict(
        image=image,
        text=text,
        text_encodings=text_encodings,
        threshold=thresholds,
        pad_square=False
    )

    if args.profile:
        torch.cuda.current_stream().synchronize()
        t0 = time.perf_counter_ns()
        for i in range(args.num_profiling_runs):
            output = predictor.predict(
                image=image,
                text=text,
                text_encodings=text_encodings,
                threshold=thresholds,
                pad_square=False
            )
        torch.cuda.current_stream().synchronize()
        t1 = time.perf_counter_ns()
        dt = (t1 - t0) / 1e9
        print(f"PROFILING FPS: {args.num_profiling_runs/dt}")

    image = np.array(image, copy=True)
    image = draw_owl_output(image, output, text=text, draw_text=True)

    # if image is a NumPy array
    if isinstance(image, np.ndarray):
        image = PIL.Image.fromarray(image)

    image.save(args.output)