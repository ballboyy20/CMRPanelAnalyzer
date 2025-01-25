To run the test you will need to type into the command line 
python3 -m pytest

or if you have installed pytest to the correct path you can just type in 
pytest

into the command line



Dependencies

    you will first need to pip install pytest

    For the test files to be able to read and interact with the source files, you will need to go and run the setup.py file, then do 
    pip install -e . 
    this will make it so that the test file can chat with the source files

    if we end up using open3d cite it here

    @article{Zhou2018,
    author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
    title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
    journal   = {arXiv:1801.09847},
    year      = {2018},
}