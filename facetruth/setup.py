from setuptools import setup, find_packages

setup(
    name='facetruth',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fer==22.4.0',
        'ffpyplayer==4.3.5',
        'matplotlib==3.5.1',
        'mediapipe==0.8.9.1',
        'mss==6.1.0',
        'numpy==1.22.2',
        'opencv_contrib_python==4.5.5.64',
        'scipy==1.8.0',
        'tensorflow==2.10.0',
        'fpdf==1.7.2'
    ],
)